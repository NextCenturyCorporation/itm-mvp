from dataclasses import dataclass
from typing import List
from swagger_client.models import (
    Scenario,
    Environment,
    Patient,
    Vitals,
    MedicalSupply,
    TriageCategory
)

@dataclass
class ADMKnowledge:
    scenario_id: str
    last_probe_id: str
    explanation: str
    scenario: Scenario
    patients: List[Patient]
    environment: Environment
    supplies: List[MedicalSupply]

class ADM:
    def __init__(self):
        self.session_active = True
        self.knowledge = ADMKnowledge()


