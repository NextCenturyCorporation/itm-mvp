import time
import uuid
from datetime import datetime
from typing import List
from swagger_server.models.probe import Probe
from swagger_server.models.vitals import Vitals
from swagger_server.models.patient import Patient
from swagger_server.models.scenario import Scenario
from swagger_server.models.scenario_state import ScenarioState
from .itm_probe_system import ITMProbeSystem
from .itm_patient_simulator import ITMPatientSimulator
from .itm_yaml_scenario_converter import YAMLScenarioConverter
from .itm_scenario_generator import ITMScenarioGenerator


class ITMScenarioSession:
    """Class for representing and manipulating a simulation scenario session."""

    def __init__(self):
        """Initialize an ITMScenarioSession."""
        self.session_id = str(uuid.uuid4())
        self.username = ''
        self.time_started = 0
        self.time_elapsed = 0
        self.formatted_start_time = None
        self.scenario: Scenario = None
        self.probe_system = ITMProbeSystem()
        self.patient_simulator = ITMPatientSimulator()

    def generate_random_id(self):
        """Generate a random UUID as a string."""
        return str(uuid.uuid4())

    def get_elapsed_time(self) -> float:
        """Return the elapsed time since the session started."""
        if self.time_started:
            self.time_elapsed = time.time() - self.time_started
        return round(self.time_elapsed, 2)

    def check_scenario_id(self, scenario_id):
        """Check if the provided scenario ID matches the session's scenario ID."""
        # TODO change this
        if not scenario_id == self.scenario.id:
            return Exception('Invalid Scenario ID')

    def get_patient_heart_rate(self, scenario_id: str, patient_id: str) -> int:
        """Get the heart rate of a patient in the scenario."""
        self.check_scenario_id(scenario_id)
        patients: List[Patient] = Scenario.patients
        for patient in patients:
            if patient.id == patient_id:
                return patient.vitals.heart_rate

    def get_patient_vitals(self, scenario_id: str, patient_id: str) -> Vitals:
        """Get the vitals of a patient in the scenario."""
        self.check_scenario_id(scenario_id)
        patients: List[Patient] = Scenario.patients
        for patient in patients:
            if patient.id == patient_id:
                return patient.vitals

    def get_probe(self, scenario_id: str) -> Probe:
        """Get a probe from the probe system."""
        # Simulate time by updating all patient vital when asking for a probe
        self.patient_simulator.update_vitals()
        self.check_scenario_id(scenario_id)
        probe = self.probe_system.generate_probe()
        return probe

    def get_scenario_state(self, scenario_id: str) -> ScenarioState:
        """Get the current state of the scenario."""
        self.check_scenario_id(scenario_id)
        scenario_state = ScenarioState(
            id="state_" + self.generate_random_id(),
            name=self.scenario.name,
            elapsed_time=self.get_elapsed_time(),
            patients=self.scenario.patients,
            medical_supplies=self.scenario.medical_supplies
        )
        return scenario_state

    def respond_to_probe(self, probe_id: str, patient_id: str,
                         explanation: str = None) -> ScenarioState:
        """Respond to a probe from the probe system."""
        # Simulate time by updating all patient vital when treating a probe
        self.patient_simulator.update_vitals()
        self.probe_system.respond_to_probe(
            probe_id=probe_id, patient_id=patient_id, explanation=explanation)
        # TODO change medical supply from explanation to something else
        self.patient_simulator.treat_patient(
            patient_id=patient_id, medical_supply=explanation)
        return self.get_scenario_state(self.scenario.id)

    def start_scenario(self, username: str) -> Scenario:
        """Start a new scenario."""
        self.username = username

        # TODO dont do this hack
        if username.endswith("_random"):
            self.scenario = ITMScenarioGenerator().generate_scenario()
        else:
            yaml_path = "swagger_server/itm/itm_scenario_configs/"
            yaml_file = "test_scenario.yaml"
            yaml_converter = YAMLScenarioConverter(yaml_path + yaml_file)
            self.scenario, patient_simulations = yaml_converter.generate_scenario_from_yaml()
            self.patient_simulator.setup_patients(self.scenario, patient_simulations)

        self.time_started = time.time()
        iso_timestamp = datetime.fromtimestamp(time.time())
        self.scenario.start_time = iso_timestamp
        self.formatted_start_time = iso_timestamp

        self.probe_system.scenario = self.scenario

        return self.scenario
