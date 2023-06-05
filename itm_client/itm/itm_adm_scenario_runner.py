import random
from enum import Enum
from dataclasses import dataclass
from typing import List
from swagger_client.models import (
    Scenario,
    Environment,
    Patient,
    Probe,
    MedicalSupply
)
from .itm_scenario_runner import ScenarioRunner


class TagTypeAndPriority(Enum):
    MINIMAL = ("minimal", 1)
    DELAYED = ("delayed", 2)
    IMMEDIATE = ("immediate", 3)
    EXPECTANT = ("expectant", 4)
    DECEASED = ("deceased", 5)

    def __new__(cls, tag_type, priority):
        obj = object.__new__(cls)
        obj._value_ = tag_type
        obj.priority = priority
        return obj

    @classmethod
    def get_enum_by_priority(cls, priority):
        for tag_type in cls:
            if tag_type.priority == priority:
                return tag_type
        raise ValueError("Invalid priority")


@dataclass
class ADMKnowledge:
    """
    What the ADM keeps track of throughout the scenario.
    """
    # Scenario
    scenario_id: str = None
    scenario: Scenario = None
    scenario_complete: bool = False

    # Info
    description: str = None
    environment: Environment = None

    # Patients
    patients: List[Patient] = None
    all_patient_ids: List[str] = None
    treated_patient_ids: List[str] = None

    # Probes
    current_probe: Probe = None
    explanation: str = None
    probes_received: List[Probe] = None
    probes_answered: int = 0

    # Supplies
    supplies: List[MedicalSupply] = None


class ADMScenarioRunner(ScenarioRunner):

    def __init__(self):
        super().__init__()
        self.username = "ITM Algorithmic Decision Maker"
        self.adm_knowledge: ADMKnowledge = ADMKnowledge()

    def run(self):
        if not self.adm_knowledge.scenario_id:
            self.retrieve_scenario()

        while not self.adm_knowledge.scenario_complete:
            self.get_probe()
            self.answer_probe()
        self.end()

    def end(self):
        print("------------------")
        print(f"Scenario Ended for user: {self.username}")
        print(f"Probes Answered: {self.adm_knowledge.probes_answered}")
        print(f"Treated Patients in Order: {self.adm_knowledge.treated_patient_ids}")
        print("------------------")

    def retrieve_scenario(self):
        scenario: Scenario = self.itm.start_scenario(self.username)
        self.scenario = scenario
        self.adm_knowledge.scenario_id = scenario.id
        self.adm_knowledge.patients = scenario.patients
        self.adm_knowledge.all_patient_ids = \
            [patient.id for patient in scenario.patients]
        self.adm_knowledge.treated_patient_ids = []
        self.adm_knowledge.probes_received = []
        self.adm_knowledge.supplies = scenario.medical_supplies
        self.adm_knowledge.environment = scenario.environment
        self.adm_knowledge.description = scenario.description

    def get_probe(self):
        self.adm_knowledge.current_probe = self.itm.get_probe(
            self.adm_knowledge.scenario_id
        )
        self.adm_knowledge.probes_received.append(
            self.adm_knowledge.current_probe
        )

    def answer_probe(self):
        self.adm_knowledge.probes_answered += 1
        patient_id = random.choice(self.adm_knowledge.patients).id
        explanation = "gauze"

        self.itm.tag_patient(
            scenario_id=self.scenario.id,
            patient_id=patient_id,
            tag=self.assess_patient_priority()
        )

        response = self.itm.respond_to_probe(
            self.adm_knowledge.current_probe.id,
            patient_id,
            explanation=explanation
        )

        self.adm_knowledge.treated_patient_ids.append(patient_id)
        self.adm_knowledge.scenario_complete = response.scenario_complete

    def assess_patient_priority(self):
        patient_priority = random.randint(1, 5)
        tag = TagTypeAndPriority.get_enum_by_priority(patient_priority)
        return tag.value
