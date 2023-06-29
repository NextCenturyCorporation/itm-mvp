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

    def __init__(self, save_to_db, scene_type, session_type=None,
                 max_scenarios=1):
        super().__init__()
        self.adm_name = scene_type + "ITM ADM4" + save_to_db
        self.adm_knowledge: ADMKnowledge = None
        self.session_type = session_type
        self.max_scenarios = max_scenarios
        self.scenarios_ran = 0
        self.total_probes_answered = 0

    def run(self):
        self.run_session() if self.session_type else self.run_single_scenario()

    def run_single_scenario(self):
        self.retrieve_scenario()
        while not self.adm_knowledge.scenario_complete:
            self.get_probe()
            self.answer_probe()
        self.end_scenario()

    def run_session(self):
        self.start_session()
        # Run until an empty scenario is returned
        while True:
            is_empty_scenario = self.retrieve_scenario()
            if is_empty_scenario:
                break
            while not self.adm_knowledge.scenario_complete:
                self.get_probe()
                self.answer_probe()
            self.end_scenario()
            self.scenarios_ran += 1
        self.end_session()

    def end_scenario(self):
        print(f"-------- Scenario {self.scenarios_ran} ---------")
        print(f"Probes Answered: {self.adm_knowledge.probes_answered}")
        print(f"Probes Answers in Order: {self.adm_knowledge.probe_choices}\n")
        self.adm_knowledge = ADMKnowledge()

    def end_session(self):
        print("[End Session]")
        print(f"Session Ended for user: {self.adm_name}")
        print(f"Scenarios ran: {self.scenarios_ran}")
        print(f"Total Probes Answered: {self.total_probes_answered}\n")

    def start_session(self):
        print(f"[Start Session]: {self.session_type}")
        self.itm.start_session(adm_name=self.adm_name,
                               session_type=self.session_type,
                               max_scenarios=self.max_scenarios)

    def retrieve_scenario(self):
        self.adm_knowledge = ADMKnowledge() 
        scenario: Scenario = self.itm.start_scenario(self.adm_name)
        if scenario.session_complete:
            return True
        self.set_scenario(scenario)
        self.adm_knowledge.alignment_target = \
            self.itm.get_alignment_target(self.adm_knowledge.scenario.id)
        return False

    def set_scenario(self, scenario):
        self.adm_knowledge.scenario = scenario
        state: State = scenario.state
        self.adm_knowledge.scenario_id = scenario.id
        self.adm_knowledge.casualties = state.casualties
        self.adm_knowledge.all_casualty_ids = [
            casualty.id for casualty in state.casualties]
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
        casualty_choice = random.choice(self.adm_knowledge.all_casualty_ids)
        self.itm.tag_casualty(casualty_id=casualty_choice,
                              tag=self.assess_casualty_priority())
        probe_choice = random.choice(self.adm_knowledge.probe_options)
        body = ProbeResponse(scenario_id=self.adm_knowledge.scenario_id,
                             probe_id=self.adm_knowledge.current_probe.id,
                             choice=probe_choice.id,
                             justification=f"Justifcation {random.randint(0, 1000)}")
        response = self.itm.respond_to_probe(body=body)
        self.adm_knowledge.probe_choices.append(probe_choice.value)
        self.adm_knowledge.scenario_complete = response.scenario_complete
        self.total_probes_answered += 1

    def assess_casualty_priority(self):
        casualty_priority = random.randint(1, 5)
        tag = TagTypeAndPriority.get_enum_by_priority(casualty_priority)
        return tag.value
