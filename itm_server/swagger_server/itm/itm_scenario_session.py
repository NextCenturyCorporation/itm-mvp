import time
import uuid
import random
import os
import connexion
from typing import List, Union
from copy import deepcopy

from swagger_server.models import (
    AlignmentTarget,
    Casualty,
    Probe,
    ProbeOption,
    ProbeResponse,
    Scenario,
    State,
    Vitals,
)
from .itm_database.itm_mongo import MongoDB
from .itm_session_scenario_object import (
    ITMSessionScenarioObjectHandler,
    ITMSessionScenarioObject
)

HOST = os.getenv('ITM_HOSTNAME') 
if (HOST == None or HOST == ""):
    HOST = "localhost"

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

        # isso is short for ITM Session Scenario Object
        self.session_type = 'test'
        self.current_isso: ITMSessionScenarioObject = None
        self.current_isso_index = 0
        self.session_issos = []
        self.number_of_scenarios = None
        self.scenario: Scenario = None
        self.used_start_session = False

        # ITMProbeGenerator or ITMProbeReader
        self.probe_system = None

        self.last_probe = None
        self.responded_to_last_probe = True
        self.probes_responded_to = []

        # This determines whether the server makes calls to TA1
        self.ta1_integration = False

        # This calls the dashboard's MongoDB
        self.save_to_database = False
        self.mongo_db = MongoDB('dashroot', 'dashr00tp@ssw0rd',
                                '{HOST}', '27017', 'dashboard')
        self.history = []


    def _add_history(self,
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

    def _check_scenario_id(self, scenario_id: str) -> None:
        """
        Check if the provided scenario ID matches the session's scenario ID.

        Args:
            scenario_id: The scenario ID to compare.

        Raises:
            Exception: If the scenario ID does not match.
        """
        if not scenario_id == self.scenario.id:
            return False, 'Scenario ID not found', 404
        return True, '', 0

    def _end_scenario(self):
        """
        End the current scenario and store history to mongo and json file.
        """
        if self.ta1_integration == True:
            alignment_target_session_alignment = \
                self.current_isso.ta1_controller.get_session_alignment()
            self._add_history(
                "TA1 Session Alignment",
                {"Session ID": self.current_isso.ta1_controller.session_id,
                "Target ID": self.current_isso.ta1_controller.alignment_target_id},
                alignment_target_session_alignment
            )
        if not self.save_to_database:
            self.history = []
            self.probes_responded_to = []
            return
        self.mongo_db.insert_data('scenarios', self.scenario.to_dict())
        insert_id = self.mongo_db.insert_data('test', {"history": self.history})
        retrieved_data = self.mongo_db.retrieve_data('test', insert_id)
        # Write the retrieved data to a local JSON file
        self.mongo_db.write_to_json_file(retrieved_data)
        self.history = []
        self.probes_responded_to = []

    def _get_realtime_elapsed_time(self) -> float:
        """
        Return the elapsed time since the session started.

        Returns:
            The elapsed time in seconds as a float.
        """
        if self.time_started:
            self.time_elapsed_realtime = time.time() - self.time_started
        return round(self.time_elapsed_realtime, 2)

    def _get_sub_directory_names(self, directory):
        """
        Return the names of all of the subdirectories inside of the
        parameter directory.

        Args:
            directory: The directory to search inside of for subdirectories.
        """
        directories = []
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                directories.append(item)
        return directories

    def get_alignment_target(self, scenario_id: str) -> AlignmentTarget:
        """
        Get the alignment target for a specific scenario.

        Args:
            scenario_id: The ID of the scenario.

        Returns:
            The alignment target for the specified scenario as an AlignmentTarget object.
        """
        (successful, message, code) = self._check_scenario_id(scenario_id)
        if not successful:
            return message, code
        return self.current_isso.alignment_target_reader.alignment_target


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
                self._add_history(
                    "Get Heart Rate", {"Casualty ID": casualty_id}, response)
                return response
        return 'Casualty ID not found', 404

    def get_probe(self, scenario_id: str) -> Probe:
        """
        Get a probe from the probe system.

        Args:
            scenario_id: The ID of the scenario.

        Returns:
            A Probe object representing the generated probe.
        """
        (successful, message, code) = self._check_scenario_id(scenario_id)
        if not successful:
            return message, code
        if self.responded_to_last_probe:
            probe = self.current_isso.probe_system.generate_probe(self.scenario.state)
            self.scenario.state.unstructured = probe.state.unstructured
            self.last_probe = probe
        else:
            probe = self.last_probe

        self.responded_to_last_probe = False
        self._add_history("Get Probe", {"Scenario ID": scenario_id}, probe.to_dict())
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
        (successful, message, code) = self._check_scenario_id(scenario_id)
        if not successful:
            return message, code
        self._add_history(
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
                self._add_history(
                    "Get Vitals", {"Casualty ID": casualty_id}, response)
                return casualty.vitals
        return 'Casualty ID not found', 404

    def respond_to_probe(self, body: ProbeResponse) -> State:
        """
        Respond to a probe from the probe system.

        Args:
            body: The probe response body as a dict.

        Returns:
            The updated scenario state as a ScenarioState object.
        """
        (successful, message, code) = self._check_scenario_id(body.scenario_id)
        if not successful:
            return message, 400
        if body.probe_id in self.probes_responded_to:
            return f'Already responded to probe with id {body.probe_id}', 400
        if body.choice not in [option.id for option in self.last_probe.options]:
            return 'Choice not valid', 404
        if body.probe_id != self.last_probe.id:
            return 'Probe ID not found', 404

        self.responded_to_last_probe = True
        self.probes_responded_to.append(body.probe_id)
        body.justification = '' if body.justification == None else body.justification
        self.current_isso.probe_system.respond_to_probe(
            probe_id=body.probe_id,
            choice=body.choice,
            justification=body.justification
        )
        time_elapsed_during_treatment = self.current_isso.casualty_simulator.treat_casualty(
            casualty_id=body.choice,
            supply=body.justification
        )
        self.time_elapsed_scenario_time += time_elapsed_during_treatment
        self.current_isso.casualty_simulator.update_vitals(time_elapsed_during_treatment)

        self.current_isso.probe_system.probe_count -= 1
        self.current_isso.probe_system.current_probe_index += 1
        self.scenario.state.elapsed_time = self.time_elapsed_scenario_time
        self.scenario.state.scenario_complete = \
            self.current_isso.probe_system.probe_count <= 0

        self._add_history(
            "Respond to Probe",
            {"Scenario ID": body.scenario_id, "Probe ID": body.probe_id,
             "Choice": body.choice, "Justification": body.justification},
            self.scenario.state.to_dict())

        if self.ta1_integration == True:
            self.current_isso.ta1_controller.post_probe(body)
            probe_response_alignment = \
                self.current_isso.ta1_controller.get_probe_response_alignment(
                body.scenario_id,
                body.probe_id
            )
            self._add_history(
                "TA1 Probe Response Alignment",
                {"Session ID": self.current_isso.ta1_controller.session_id,
                "Scenario ID": body.scenario_id,
                "Target ID": self.current_isso.ta1_controller.alignment_target_id,
                "Probe ID": body.probe_id},
                probe_response_alignment
            )

        if self.scenario.state.scenario_complete:
            self._end_scenario()
        return self.scenario.state

    def start_scenario(self, adm_name: str, scenario_id: str=None) -> Scenario:
        """
        Start a new scenario.

        Args:
            adm_name: The adm name associated with the scenario.

        Returns:
            The started scenario as a Scenario object.
        """
        # TODO this needs to get a specific scenario by id
        if scenario_id:
            raise connexion.ProblemException(status=403, title="Forbidden", detail="Sorry, internal TA3 only")
        
        # TODO this needs to check if we don't have this scenario id
        if scenario_id and not scenario_id not in ['scenario_id_list']:
            return "Scenario ID does not exist", 404
        
        # placeholder for System Overload error code
        system_overload = False
        if system_overload:
            return "System Overload", 418

        # A session has not been started so make a new one
        if not self.used_start_session:
            self.start_session(
                adm_name=adm_name,
                session_type=self.session_type,
                max_scenarios=1,
                used_start_session=False
            )
        try:
            self.current_isso: ITMSessionScenarioObject = self.session_issos[self.current_isso_index]
            self.scenario = self.current_isso.scenario
            self.current_isso_index += 1

            self._add_history(
                "Start Scenario",
                {"ADM Name": self.adm_name},
                self.scenario.to_dict())

            if self.ta1_integration == True:
                session_id = self.current_isso.ta1_controller.new_session()
                self._add_history(
                    "TA1 Alignment Target Session ID", {}, session_id
                )
                scenario_alignment = self.current_isso.ta1_controller.get_alignment_target()
                self._add_history(
                    "TA1 Alignment Target Data",
                    {"Session ID": self.current_isso.ta1_controller.session_id,
                    "Scenario ID": self.current_isso.scenario.id},
                    scenario_alignment
                )

            return self.scenario
        except:
            # Empty Scenario
            return Scenario(session_complete=True, id='', name='',
                            start_time=None, state=None, triage_categories=None)

    def start_session(self, adm_name: str, session_type: str, max_scenarios=None, used_start_session=False) -> Scenario:
        """
        Start a new scenario.

        Args:
            adm_name: The adm name associated with the scenario.
            type: The type of scenarios either soartech, adept, test, or eval
            max_scenarios: The max number of scenarios presented during the session

        Returns:
            The first started scenario as a Scenario object.
        """
        if session_type not in ['test', 'adept', 'soartech', 'eval']:
            return (
                'Invalid session type. Must be "test, adept, soartech, or eval"',
                400
            )

        # placeholder for System Overload error code
        system_overload = False
        if system_overload:
            return 'System Overload', 418

        self.adm_name = adm_name
        self.session_issos = []
        self.session_type = session_type
        self.used_start_session = used_start_session
        self.history = []
        self.probes_responded_to = []


        """
        Note For ITM Darpa Demo. Use the commented out code starting with
        self.session_type = 'soartech' and then comment out this block.
        Using the commented out block instead of this will serve up
        only a soartech scene and integrate it with TA1 and the 
        database
        """
        # Save to database based on adm_name.
        if self.adm_name.endswith("_db_"):
            self.adm_name = self.adm_name.removesuffix("_db_")
            self.save_to_database = True
        if self.session_type == 'eval':
            self.save_to_database = True
            self.ta1_integration = True
            max_scenarios = None

        """
        self.session_type = 'soartech'
        session_type = 'soartech'
        # Save to database based on adm_name. This is good enough for now but should be changed.
        if self.adm_name.endswith("_db_"):
            self.adm_name = self.adm_name.removesuffix("_db_")
            self.save_to_database = True
        if self.session_type in ['eval', 'soartech', 'adept']:
            self.save_to_database = True
            self.ta1_integration = True
            max_scenarios = None
        """

        yaml_paths = []
        yaml_path = "swagger_server/itm/itm_scenario_configs/"
        if session_type == 'soartech' or session_type == 'test' or session_type == 'eval':
            yaml_paths.append(yaml_path + 'soartech/')
        if session_type == 'adept' or session_type == 'test' or session_type == 'eval':
            yaml_paths.append(yaml_path + 'adept/')
        self.number_of_scenarios = max_scenarios

        selected_yaml_directories = [
            f"{path}{folder}/"
            for path in yaml_paths
            for folder in self._get_sub_directory_names(path)]
        if max_scenarios != None and max_scenarios >= 1:
            # fill in extra scenarios with random copies
            inital_selected_yaml_directories = deepcopy(selected_yaml_directories)
            while len(selected_yaml_directories) < max_scenarios:
                random_directory = random.choice(inital_selected_yaml_directories)
                selected_yaml_directories.append(random_directory)
        else:
            max_scenarios = len(selected_yaml_directories)
        random.shuffle(selected_yaml_directories)
        for i in range(max_scenarios):
            scenario_object_handler = ITMSessionScenarioObjectHandler(yaml_path=selected_yaml_directories[i])
            itm_scenario_object = \
                scenario_object_handler.generate_session_scenario_object()
            self.session_issos.append(itm_scenario_object)
        self.current_isso_index = 0

        return f'Session started with session type: {session_type} and max scenarios {max_scenarios}'

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
                self._add_history(
                    "Tag Casualty",
                    {"Casualty ID": casualty_id, "Tag": tag},
                    response)
                return response
        return 'Casualty ID not found', 404
