import time
import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import List
from swagger_server.models.scenario import Scenario
from swagger_server.models.probe import Probe
from swagger_server.models.patient import Patient
from swagger_server.models.scenario_state import ScenarioState

@dataclass
class ProbeObject:
    probe: Probe
    patient_id_chosen: str
    explanation: str
    probe_number: int

class ITMProbeSystem:

    def __init__(self):
        self.scenario: Scenario = None
        self.probe_count = 0
        self.probes = {}


    def generate_random_id(self):
        return str(uuid.uuid4())
    

    def generate_probe(self) -> Probe:
        id = "probe_" + self.generate_random_id()
        question = self.generate_question()
        patient_ids = [patient.id for patient in self.scenario.patients]
        probe = Probe(
            id=id,
            question=question,
            patient_ids=patient_ids
        )
        self.probes[id] = ProbeObject(
            probe=probe,
            patient_id_chosen='',
            explanation='',
            probe_number=self.probe_count
        )
        self.probe_count += 1
        return probe


    def generate_question(self) -> str:
        question = ''
        description = self.scenario.description + '. '
        question += description
        for patient in self.scenario.patients:
            patient_question = (
                f'Patient {patient.id} is a {patient.age} '
                f'year old {patient.sex} named {patient.name}. '
                f'Their injuries are {patient.injuries}, '
                f'vitals are {patient.vitals}, '
                f'and mental status is {patient.mental_status}. '
            )
            question += patient_question
        
        question += 'Choose a patient to treat. Specify by patient ID." \n'
        return question
    
    def respond_to_probe(
            self,
            probe_id: str,
            patient_id: str,
            explanation: str = None
        ) -> None:
        probe: ProbeObject = self.probes[probe_id]
        probe.patient_id_chosen = patient_id
        probe.explanation = explanation

        for p in self.scenario.patients:
            if p.id == patient_id:
                p.assessed = True
                break
