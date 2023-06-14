import time
import uuid
import signal
from datetime import datetime
from typing import List, Union

from swagger_server.models import Probe, Vitals, Patient, Scenario, ScenarioState
from .itm_probe_system import ITMProbeSystem
from .itm_patient_simulator import ITMPatientSimulator
from .itm_yaml_scenario_converter import YAMLScenarioConverter
from .itm_scenario_generator import ITMScenarioGenerator
from .itm_medical_supplies import ITMMedicalSupplies
from .itm_database.itm_mongo import MongoDB


class ITMScenarioSession:
    """
    Class for representing and manipulating a simulation scenario session.
    """

    def __init__(self):
        """
        Initialize an ITMScenarioSession.
        """
        self.session_id = str(uuid.uuid4())
        self.username = ''
        self.time_started = 0
        self.time_elapsed_realtime = 0
        self.time_elapsed_scenario_time = 0
        self.formatted_start_time = None
        self.scenario = None
        self.scenario_complete = False
        self.medical_supply_details = ITMMedicalSupplies()
        self.probe_system = ITMProbeSystem()
        self.patient_simulator = ITMPatientSimulator()
        self.save_to_database = False

        # This calls the dashboard's MongoDB
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

    def get_patient_heart_rate(self, scenario_id: str, patient_id: str) -> int:
        """
        Get the heart rate of a patient in the scenario.

        Args:
            scenario_id: The ID of the scenario.
            patient_id: The ID of the patient.

        Returns:
            The heart rate of the patient as an integer.
        """
        self.check_scenario_id(scenario_id)
        patients: List[Patient] = Scenario.patients
        for patient in patients:
            if patient.id == patient_id:
                response = patient.vitals.heart_rate
                self.add_history(
                    "get_patient_heart_rate", {
                        "scenario_id": scenario_id,
                        "patient_id": patient_id,
                    }, response)
                return response

    def get_patient_vitals(self, scenario_id: str, patient_id: str) -> Vitals:
        """
        Get the vitals of a patient in the scenario.

        Args:
            scenario_id: The ID of the scenario.
            patient_id: The ID of the patient.

        Returns:
            The vitals of the patient as a Vitals object.
        """
        self.check_scenario_id(scenario_id)
        patients: List[Patient] = Scenario.patients
        for patient in patients:
            if patient.id == patient_id:
                response = patient.vitals.to_dict()
                self.add_history(
                    "get_patient_vitals", {
                        "scenario_id": scenario_id,
                        "patient_id": patient_id,
                    }, response)
                return patient.vitals

    def get_probe(self, scenario_id: str) -> Probe:
        """
        Get a probe from the probe system.

        Args:
            scenario_id: The ID of the scenario.

        Returns:
            A Probe object representing the generated probe.
        """
        self.check_scenario_id(scenario_id)
        probe = self.probe_system.generate_probe(
            self.patient_simulator.patient_simulations)
        self.add_history(
            "get_probe", {
                "scenario_id": scenario_id,
            }, probe.to_dict())
        return probe

    def get_scenario_state(self, scenario_id: str) -> ScenarioState:
        """
        Get the current state of the scenario.

        Args:
            scenario_id: The ID of the scenario.

        Returns:
            The current state of the scenario as a ScenarioState object.
        """
        self.check_scenario_id(scenario_id)
        scenario_state = ScenarioState(
            id="state_" + str(uuid.uuid4()),
            name=self.scenario.name,
            elapsed_time=self.time_elapsed_scenario_time,
            patients=self.scenario.patients,
            medical_supplies=self.scenario.medical_supplies,
            scenario_complete=self.scenario_complete
        )
        self.add_history(
            "get_scenario_state", {
                "scenario_id": scenario_id,
            }, scenario_state.to_dict())
        return scenario_state

    def respond_to_probe(self, probe_id: str, patient_id: str,
                         explanation: str = None) -> ScenarioState:
        """
        Respond to a probe from the probe system.

        Args:
            probe_id: The ID of the probe.
            patient_id: The ID of the patient.
            explanation: An explanation for the response (optional).

        Returns:
            The updated scenario state as a ScenarioState object.
        """
        self.probe_system.respond_to_probe(
            probe_id=probe_id, patient_id=patient_id, explanation=explanation)

        time_elapsed_during_treatment = self.patient_simulator.treat_patient(
            patient_id=patient_id,
            medical_supply=explanation,
            medical_supply_details=self.medical_supply_details.medical_supply_details
        )
        self.time_elapsed_scenario_time += time_elapsed_during_treatment
        self.patient_simulator.update_vitals(time_elapsed_during_treatment)

        self.scenario_complete = all(
            [patient.assessed for patient in self.scenario.patients])
        scenario_state = self.get_scenario_state(self.scenario.id)

        self.add_history(
            "respond_to_probe", {
                "probe_id": probe_id,
                "patient_id": patient_id,
                "explanation": explanation
            }, scenario_state.to_dict())

        if self.scenario_complete:
            self.end_scenario()

        return scenario_state

    def start_scenario(self, username: str) -> Scenario:
        """
        Start a new scenario.

        Args:
            username: The username associated with the scenario.

        Returns:
            The started scenario as a Scenario object.
        """
        self.username = username

        # Save to database based on username. This needs to be changed!
        if self.username.endswith("_db_"):
            self.username = self.username.removesuffix("_db_")
            self.save_to_database = True
        # Generate or read scenario based on username.
        # This needs to be changed too!
        if self.username.startswith("_random_"):
            self.username = self.username.removeprefix("_random_")
            self.scenario = ITMScenarioGenerator().generate_scenario()
        else:
            yaml_path = "swagger_server/itm/itm_scenario_configs/"
            yaml_file = "test_scenario.yaml"
            yaml_converter = YAMLScenarioConverter(yaml_path + yaml_file)
            self.scenario, patient_simulations, self.medical_supply_details = \
                yaml_converter.generate_scenario_from_yaml()
            self.patient_simulator.setup_patients(self.scenario, patient_simulations)

        self.time_started = time.time()
        iso_timestamp = datetime.fromtimestamp(time.time())
        self.scenario.start_time = iso_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
        self.formatted_start_time = iso_timestamp

        self.probe_system.scenario = self.scenario
        self.add_history("start_scenario", {
            "username": self.username
        }, self.scenario.to_dict())
        return self.scenario

    def tag_patient(self, scenario_id: str, patient_id: str, tag: str) -> str:
        """
        Tag a patient in the scenario.

        Args:
            scenario_id: The ID of the scenario.
            patient_id: The ID of the patient.
            tag: The tag to assign to the patient.

        Returns:
            A message confirming the tagging of the patient.
        """
        self.check_scenario_id(scenario_id)
        for patient in self.scenario.patients:
            if patient.id == patient_id:
                patient.tag = tag
                response = f"{patient.id} tagged as {tag}."
                self.add_history(
                    "tag_patient", {
                        "scenario_id": scenario_id,
                        "patient_id": patient_id,
                        "tag": tag
                    }, response)
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
        insert_id = self.mongo_db.insert_data('test', {"history": self.history})
        retrieved_data = self.mongo_db.retrieve_data('test', insert_id)
        # Write the retrieved data to a local JSON file
        self.mongo_db.write_to_json_file(retrieved_data)
