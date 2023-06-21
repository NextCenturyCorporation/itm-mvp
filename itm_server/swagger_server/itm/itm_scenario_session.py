from datetime import datetime
import time
import uuid
from typing import List, Union

from swagger_server.models import (
    AlignmentTarget,
    AlignmentTargetKdmaValues,
    Casualty,
    Probe,
    ProbeOption,
    ProbeResponse,
    Scenario,
    State,
    Vitals,
)
from .itm_casualty_simulator import ITMCasualtySimulator
from .itm_database.itm_mongo import MongoDB
from .itm_probe_generator import ITMProbeGenerator
from .itm_probe_reader import ITMProbeReader
from .itm_scenario_generator import ITMScenarioGenerator
from .itm_supplies import ITMSupplies
from .itm_scenario_reader import ITMScenarioReader
from .itm_alignment_target_reader import ITMAlignmentTargetReader



class ITMScenarioSession:
    """
    Class for representing and manipulating a simulation scenario session.
    """

    def __init__(self):
        """
        Initialize an ITMScenarioSession.
        """
        self.session_id = str(uuid.uuid4())
        self.adm_name = ''
        self.time_started = 0
        self.time_elapsed_realtime = 0
        self.time_elapsed_scenario_time = 0
        self.formatted_start_time = None
        self.scenario: Scenario = None

        self.supplies_details = ITMSupplies()
        self.casualty_simulator = ITMCasualtySimulator()

        self.alignment_target_reader: ITMAlignmentTargetReader = None

        # ITMProbeGenerator or ITMProbeReader
        self.probe_system = None

        self.last_probe = None
        self.responded_to_last_probe = True
        self.probes_answers_required_to_complete_scenario = 0

        # This calls the dashboard's MongoDB
        self.save_to_database = False
        self.mongo_db = MongoDB('dashroot', 'dashr00tp@ssw0rd',
                                'localhost', '27017', 'dashboard')
        self.history = []

    def get_realtime_elapsed_time(self) -> float:
        """
        Return the elapsed time since the session started.

        Returns:
            The elapsed time in seconds as a float.
        """
        if self.time_started:
            self.time_elapsed_realtime = time.time() - self.time_started
        return round(self.time_elapsed_realtime, 2)

    def check_scenario_id(self, scenario_id: str) -> None:
        """
        Check if the provided scenario ID matches the session's scenario ID.

        Args:
            scenario_id: The scenario ID to compare.

        Raises:
            Exception: If the scenario ID does not match.
        """
        if not scenario_id == self.scenario.id:
            raise Exception('Invalid Scenario ID')

    def get_alignment_target(self, scenario_id: str) -> AlignmentTarget:
        self.check_scenario_id(scenario_id)
        return self.alignment_target_reader.alignment_target

    def get_heart_rate(self, casualty_id: str) -> int:
        """
        Get the heart rate of a casualty_id in the scenario.

        Args:
            scenario_id: The ID of the scenario.
            casualty_id: The ID of the casualty_id.

        Returns:
            The heart rate of the casualty as an integer.
        """
        casualties: List[Casualty] = self.scenario.state.casualties
        for casualty in casualties:
            if casualty.id == casualty_id:
                response = casualty.vitals.hrpmin
                self.add_history(
                    "Get Heart Rate", {"Casualty ID": casualty_id}, response)
                return response

    def get_probe(self, scenario_id: str) -> Probe:
        """
        Get a probe from the probe system.

        Args:
            scenario_id: The ID of the scenario.

        Returns:
            A Probe object representing the generated probe.
        """
        self.check_scenario_id(scenario_id)
        if self.responded_to_last_probe:
            probe = self.probe_system.generate_probe(self.scenario.state)
            self.last_probe = probe
        else:
            probe = self.last_probe

        self.responded_to_last_probe = False
        self.add_history("Get Probe", {"Scenario ID": scenario_id}, probe.to_dict())
        modifed_options = [
            ProbeOption(
                id=p.id, value=p.value, kdma_association={}
            ) for p in probe.options
        ]
        return Probe(
            id=probe.id,
            scenario_id=scenario_id,
            type=probe.type,
            prompt=probe.prompt,
            state=probe.state,
            options=modifed_options
        )

    def get_scenario_state(self, scenario_id: str) -> State:
        """
        Get the current state of the scenario.

        Args:
            scenario_id: The ID of the scenario.

        Returns:
            The current state of the scenario as a ScenarioState object.
        """
        self.check_scenario_id(scenario_id)
        self.add_history(
            "Get Scenario State",
            {"Scenario ID": scenario_id},
            self.scenario.state.to_dict())
        return self.scenario.state
    
    def get_vitals(self, casualty_id: str) -> Vitals:
        """
        Get the vitals of a casualty in the scenario.

        Args:
            scenario_id: The ID of the scenario.
            casualty_id: The ID of the casualty.

        Returns:
            The vitals of the casualty as a Vitals object.
        """
        casualties: List[Casualty] = self.scenario.state.casualties
        for casualty in casualties:
            if casualty.id == casualty_id:
                response = casualty.vitals.to_dict()
                self.add_history(
                    "Get Vitals", {"Casualty ID": casualty_id}, response)
                return casualty.vitals

    def respond_to_probe(self, body: ProbeResponse) -> State:
        """
        Respond to a probe from the probe system.

        Args:
            body: The probe response body as a dict.

        Returns:
            The updated scenario state as a ScenarioState object.
        """
        self.responded_to_last_probe = True
        self.probe_system.respond_to_probe(
            probe_id=body.probe_id,
            choice=body.choice,
            justification=body.justification
        )
        time_elapsed_during_treatment = self.casualty_simulator.treat_casualty(
            casualty_id=body.choice,
            supply=body.justification
        )
        self.time_elapsed_scenario_time += time_elapsed_during_treatment
        self.casualty_simulator.update_vitals(time_elapsed_during_treatment)

        self.probe_system.probe_count -= 1
        self.probe_system.current_probe_index += 1
        self.scenario.state.elapsed_time = self.time_elapsed_scenario_time
        self.scenario.state.scenario_complete = \
            self.probe_system.probe_count <= 0
        self.add_history(
            "Respond to Probe",
            {"Scenario ID": body.scenario_id, "Probe ID": body.probe_id,
            "Choice": body.choice, "Justification": body.justification}, 
            self.scenario.state.to_dict())
        if self.scenario.state.scenario_complete:
            self.end_scenario()
        return self.scenario.state

    def start_scenario(self, adm_name: str) -> Scenario:
        """
        Start a new scenario.

        Args:
            adm_name: The adm name associated with the scenario.

        Returns:
            The started scenario as a Scenario object.
        """
        self.adm_name = adm_name

        # Save to database based on adm_name. This needs to be changed!
        if self.adm_name.endswith("_db_"):
            self.adm_name = self.adm_name.removesuffix("_db_")
            self.save_to_database = True
        # Generate or read scenario based on adm_name.
        # This needs to be changed too!
        if self.adm_name.startswith("_random_"):
            self.adm_name = self.adm_name.removeprefix("_random_")
            self.scenario = ITMScenarioGenerator().generate_scenario()
        else:
            yaml_path = "swagger_server/itm/itm_scenario_configs/scenario_1/"
            
            scenario_file = "scenario.yaml"
            scenario_reader = ITMScenarioReader(yaml_path + scenario_file)
            ( self.scenario, casualty_simulations,
              self.supplies_details ) = \
                scenario_reader.read_scenario_from_yaml()
            self.casualty_simulator.setup_casualties(self.scenario, casualty_simulations)
            
            self.probe_system = ITMProbeReader(yaml_path)
            
            alignment_target_file = "alignment_target.yaml"
            self.alignment_target_reader = ITMAlignmentTargetReader(yaml_path + alignment_target_file)

        self.time_started = time.time()
        iso_timestamp = datetime.fromtimestamp(time.time())
        self.scenario.start_time = iso_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
        self.formatted_start_time = iso_timestamp

        self.probe_system.scenario = self.scenario
        self.add_history(
            "Start Scenario", {"ADM Name": self.adm_name}, self.scenario.to_dict())
        return self.scenario

    def tag_casualty(self, casualty_id: str, tag: str) -> str:
        """
        Tag a casualty in the scenario.

        Args:
            scenario_id: The ID of the scenario.
            casualty_id: The ID of the casualty.
            tag: The tag to assign to the casualty.

        Returns:
            A message confirming the tagging of the casualty.
        """
        for casualty in self.scenario.state.casualties:
            if casualty.id == casualty_id:
                casualty.tag = tag
                response = f"{casualty.id} tagged as {tag}."
                self.add_history(
                    "Tag Casualty",
                    {"Casualty ID": casualty_id, "Tag": tag},
                    response)
                return response

    def add_history(self,
                    command: str,
                    parameters: dict,
                    response: Union[dict, str]) -> None:
        """
        Add a command to the history of the scenario session.

        Args:
            command: The command executed.
            parameters: The parameters passed to the command.
            response: The response from the command.
        """
        history = {
            "command": command,
            "parameters": parameters,
            "response": response
        }
        self.history.append(history)


    def end_scenario(self):
        """
        End the current scenario and store history to mongo and json file.
        """
        if not self.save_to_database:
            return
        self.mongo_db.insert_data('scenarios', self.scenario.to_dict())
        insert_id = self.mongo_db.insert_data('test', {"history": self.history})
        retrieved_data = self.mongo_db.retrieve_data('test', insert_id)
        # Write the retrieved data to a local JSON file
        self.mongo_db.write_to_json_file(retrieved_data)
