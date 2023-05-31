import time
import uuid
from datetime import datetime
from typing import List
from swagger_server.models.scenario import Scenario
from swagger_server.models.vitals import Vitals
from swagger_server.models.probe import Probe
from swagger_server.models.patient import Patient
from swagger_server.models.scenario_state import ScenarioState
from .itm_scenario_generator import ITMScenarioGenerator
from .itm_probe_system import ITMProbeSystem


class ITMScenarioSession:

    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.username = ''
        self.scenario: Scenario = None
        self.time_started = 0
        self.time_elapsed = 0
        self.formatted_start_time = None
        self.probe_system = ITMProbeSystem()


    def generate_random_id(self):
        return str(uuid.uuid4())


    def get_elapsed_time(self):
        if self.time_started:
            self.time_elapsed = time.time() - self.time_started
        return round(self.time_elapsed, 2)


    def check_scenario_id(self, scenario_id):
        if not scenario_id == self.scenario.id:
            return Exception('Invalid Scenario ID')


    def get_session_id(self):
        return self.session_id


    def get_patient_heart_rate(
            self,
            scenario_id: str,
            patient_id: str
        ) -> int:
        self.check_scenario_id(scenario_id)
        patients: List[Patient] = Scenario.patients
        for patient in patients:
            if patient.id == patient_id:
                return patient.vitals.heart_rate


    def get_patient_vitals(
            self,
            scenario_id: str,
            patient_id: str
        ) -> Vitals:
        self.check_scenario_id(scenario_id)
        patients: List[Patient] = Scenario.patients
        for patient in patients:
            if patient.id == patient_id:
                return patient.vitals


    def get_probe(self, scenario_id: str) -> Probe:
        self.check_scenario_id(scenario_id)
        probe = self.probe_system.generate_probe()
        return probe

    
    def get_scenario_state(self, scenario_id: str) -> ScenarioState:
        self.check_scenario_id(scenario_id)
        scenario_state = ScenarioState(
            id="state_" + self.generate_random_id(),
            name=self.scenario.name,
            elapsed_time=self.get_elapsed_time(),
            patients=self.scenario.patients,
            medical_supplies=self.scenario.medical_supplies
        )
        print(self.probe_system.probes)
        return scenario_state


    def respond_to_probe(
            self,
            probe_id: str,
            patient_id: str,
            explanation: str = None
        ) -> ScenarioState:
        self.probe_system.respond_to_probe(
            probe_id=probe_id,
            patient_id=patient_id,
            explanation=explanation
        )
        return self.get_scenario_state(self.scenario.id)


    def start_scenario(self, username: str) -> Scenario:
        self.username = username
        self.scenario = ITMScenarioGenerator().generate_scenario()
        self.time_started = time.time()
        
        iso_timestamp = datetime.fromtimestamp(time.time())
        self.scenario.start_time = iso_timestamp
        self.formatted_start_time = iso_timestamp

        self.probe_system.scenario = self.scenario

        return self.scenario
    