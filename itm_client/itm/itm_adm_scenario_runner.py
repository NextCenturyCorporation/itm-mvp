import random
from enum import Enum
from dataclasses import dataclass
from typing import List
from swagger_client.models import (
    Scenario,
    State,
    Casualty,
    Supplies,
    Environment,
    Probe,
    ProbeOption,
    ProbeResponse,
    AlignmentTarget
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

    # casualties
    casualties: List[Casualty] = None
    all_casualty_ids: List[str] = None
    treated_casualty_ids: List[str] = None

    # Probes
    current_probe: Probe = None
    explanation: str = None
    probes_received: List[Probe] = None
    probes_answered: int = 0

    # Supplies
    supplies: List[Supplies] = None

    alignment_target: AlignmentTarget = None

    probe_options: List[ProbeOption] = None
    probe_choices: List[str] = None



class ADMScenarioRunner(ScenarioRunner):

    def __init__(self, save_to_db, scene_type):
        super().__init__()
        self.adm_name = scene_type + "ITM ADM4" + save_to_db
        self.adm_knowledge: ADMKnowledge = ADMKnowledge()

    def run(self):
        if not self.adm_knowledge.scenario_id:
            self.retrieve_scenario()
            self.adm_knowledge.alignment_target = self.itm.get_alignment_target(self.scenario.id)

        while not self.adm_knowledge.scenario_complete:
            self.get_probe()
            self.answer_probe()
        self.end()

    def end(self):
        print("------------------")
        print(f"Scenario Ended for user: {self.adm_name}")
        print(f"Probes Answered: {self.adm_knowledge.probes_answered}")
        print(f"Probes Answers in Order: {self.adm_knowledge.probe_choices}")
        print("------------------")

    def retrieve_scenario(self):
        scenario: Scenario = self.itm.start_scenario(self.adm_name)
        self.scenario = scenario
        state: State = self.scenario.state
        self.adm_knowledge.scenario_id = scenario.id
        self.adm_knowledge.casualties = state.casualties
        self.adm_knowledge.all_casualty_ids = \
            [casualty.id for casualty in state.casualties]
        self.adm_knowledge.treated_casualty_ids = []
        self.adm_knowledge.probes_received = []
        self.adm_knowledge.probe_choices = []
        self.adm_knowledge.supplies = state.supplies
        self.adm_knowledge.environment = state.environment
        self.adm_knowledge.description = state.mission.unstructured

    def get_probe(self):
        self.adm_knowledge.current_probe = self.itm.get_probe(
            self.adm_knowledge.scenario_id)
        self.adm_knowledge.probes_received.append(
            self.adm_knowledge.current_probe)
        self.adm_knowledge.probe_options = self.adm_knowledge.current_probe.options

    def answer_probe(self):
        self.adm_knowledge.probes_answered += 1
        casualty_choice = random.choice([p for p in self.adm_knowledge.all_casualty_ids])
        self.itm.tag_casualty(
            casualty_id=casualty_choice, tag=self.assess_casualty_priority())
        probe_choice = random.choice([p for p in self.adm_knowledge.probe_options])
        body = ProbeResponse(
            scenario_id=self.adm_knowledge.scenario_id,
            probe_id=self.adm_knowledge.current_probe.id,
            choice=probe_choice.id,
            justification=f"Justifcation {random.randint(0, 1000)}"
        )
        response = self.itm.respond_to_probe(body=body)
        self.adm_knowledge.probe_choices.append(probe_choice.value)
        self.adm_knowledge.scenario_complete = response.scenario_complete

    def assess_casualty_priority(self):
        casualty_priority = random.randint(1, 5)
        tag = TagTypeAndPriority.get_enum_by_priority(casualty_priority)
        return tag.value
