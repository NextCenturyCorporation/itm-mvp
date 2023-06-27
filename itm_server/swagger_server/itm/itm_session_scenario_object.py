from time import time
from typing import List
from dataclasses import dataclass
from datetime import datetime
from swagger_server.models import Scenario
from .itm_casualty_simulator import ITMCasualtySimulator, CasualtySimulation
from .itm_probe_reader import ITMProbeReader
from .itm_supplies import ITMSupplies
from .itm_scenario_reader import ITMScenarioReader
from .itm_alignment_target_reader import ITMAlignmentTargetReader

@dataclass
class ITMSessionScenarioObject:
    folder_name: str = None
    scenario: Scenario = None
    scenario_reader: ITMScenarioReader = None
    probe_system: ITMProbeReader = None
    alignment_target_reader: ITMAlignmentTargetReader = None
    casualty_simulations: List[CasualtySimulation] = None
    casualty_simulator = None
    supplies: ITMSupplies = None

class ITMSessionScenarioObjectHandler:

    def __init__(self, yaml_path) -> None:
        self.yaml_path = yaml_path

    def generate_session_scenario_object(self):
        # isso is short for ITM Session Scenario Object
        isso = ITMSessionScenarioObject()

        isso.scenario_reader = ITMScenarioReader(self.yaml_path + "scenario.yaml")
        isso.probe_system = ITMProbeReader(self.yaml_path)
        isso.probe_system.scenario = isso.scenario
        ( isso.scenario, isso.casualty_simulations, isso.supplies_details ) = \
            isso.scenario_reader.read_scenario_from_yaml()
        isso.casualty_simulator = ITMCasualtySimulator()
        isso.casualty_simulator.setup_casualties(isso.scenario, isso.casualty_simulations)

        isso.alignment_target_reader = ITMAlignmentTargetReader(self.yaml_path + "alignment_target.yaml")

        isso.scenario.start_time = datetime.fromtimestamp(time()).strftime("%Y-%m-%d %H:%M:%S.%f")

        return isso
