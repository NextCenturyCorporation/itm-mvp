import copy
import uuid
import yaml
from typing import List, Tuple

from .itm_casualty_simulator import CasualtySimulation
from .itm_supplies import ITMSupplies, SupplyDetails

from swagger_server.models.alignment_target import AlignmentTarget
from swagger_server.models.alignment_target_kdma_values import AlignmentTargetKdmaValues
from swagger_server.models.casualty import Casualty
from swagger_server.models.demographics import Demographics
from swagger_server.models.environment import Environment
from swagger_server.models.injury import Injury
from swagger_server.models.mission import Mission
from swagger_server.models.scenario import Scenario
from swagger_server.models.state import State
from swagger_server.models.supplies import Supplies
from swagger_server.models.threat_state import ThreatState
from swagger_server.models.triage_category import TriageCategory
from swagger_server.models.vitals import Vitals


class YAMLScenarioConverter:
    """Class for converting YAML data to ITM scenarios."""

    def __init__(self, yaml_path: str):
        """
        Initialize the class with YAML data from a file path.

        Args:
            yaml_path: The file path to the YAML data.
        """
        with open(yaml_path, 'r') as file:
            self.yaml_data = yaml.safe_load(file)

    def generate_scenario_from_yaml(self) -> \
            Tuple[Scenario, List[CasualtySimulation], List[ITMSupplies], SupplyDetails, AlignmentTarget]:
        """
        Generate a Scenario and casualty simulations from the YAML data.

        Returns:
            A tuple containing the generated Scenario, a list of CasualtySimulation objects, and SupplysDetails objects.
        """
        state, casualty_simulations, supplies_details = self._generate_state()
        triage_categories = self._generate_triage_categories()
        scenario = Scenario(
            id="scenario_" + str(uuid.uuid4()),
            name=self.yaml_data['name'],
            start_time=str(0),
            state=state,
            triage_categories=triage_categories
        )
        alignment_targets = self.yaml_data['alignment_target']
        alignment_target = AlignmentTarget(
            id="alignment_target_" + str(uuid.uuid4()),
            kdma_values=[
                AlignmentTargetKdmaValues(kdma=at['kdma'], value=at['value'])
                for at in alignment_targets]
        )
        probe_count = self.yaml_data['probe_count']
        return (scenario, casualty_simulations, supplies_details, alignment_target, probe_count)
    
    def _generate_state(self):
        unstructured = self.yaml_data['unstructured']
        mission = self._generate_mission()
        environment = self._generate_environment()
        threat_state = self._generate_threat_state()
        supplies_details = ITMSupplies()
        supplies = [
            self._generate_supplies(supply_data, supplies_details)
            for supply_data in self.yaml_data['supplies']
        ]
        casualty_simulations = [
            self._generate_casualty_simulations(casualty_data)
            for casualty_data in self.yaml_data['casualties']
        ]
        state = State(
            unstructured=unstructured,
            elapsed_time=0,
            scenario_complete=False,
            mission=mission,
            environment=environment,
            threat_state=threat_state,
            supplies=supplies,
            casualties=[casualty.casualty for casualty in casualty_simulations]
        )
        return state, casualty_simulations, supplies_details

    def _generate_mission(self):
        mission = self.yaml_data['mission']
        return Mission(
            unstructured=mission['unstructured'],
            mission_type=mission['mission_type']
        )
    
    def _generate_environment(self) -> Environment:
        """
        Generate an Environment instance from the YAML data.

        Args:
            environment_data: The YAML data representing an environment.

        Returns:
            An Environment object representing the generated environment.
        """
        environment = self.yaml_data['environment']
        return Environment(
            unstructured=environment['unstructured'],
            weather=environment['weather'],
            location=environment['location'],
            visibility=environment['visibility'],
            noise_ambient=environment['noise_ambient'],
            noise_peak=environment['noise_peak']
        )
    
    def _generate_threat_state(self):
        threat_state = self.yaml_data['threat_state']
        return ThreatState(
            unstructured=threat_state['unstructured'],
            threats=threat_state['threats']
        )

    def _generate_supplies(self, supply_data, supply_details: ITMSupplies) -> Supplies:
        """
        Generate a Supplies instance from the YAML data.

        Args:
            supply_data: The YAML data representing a supply.
            supply_details: The ITMSupplies object to store a supply details.

        Returns:
            A Supplies object representing the generated supply.
        """
        supplies = Supplies(
            type=supply_data['type'],
            quantity=supply_data['quantity']
        )
        supply_details.get_supplies()[supplies.type] = \
            SupplyDetails(
                supply=supplies,
                time_to_apply=supply_data['hidden_attributes']['time_to_apply_in_minutes']
            )
        return supplies

    def _generate_casualty(self, casualty_data) -> Casualty:
        """
        Generate a casualty instance from the YAML data.

        Args:
            casualty_data: The YAML data representing a casualty.

        Returns:
            A casualty object representing the generated casualty.
        """
        demograpics_data = casualty_data['demographics']
        demograpics = Demographics(
            age=demograpics_data['age'],
            sex=demograpics_data['sex'],
            rank=demograpics_data['rank']
        )
        injuries = [
            Injury(
                name=injury['name'],
                location=injury['location'],
                severity=injury['severity']
            )
            for injury in casualty_data['injuries']
        ]
        vital_data = casualty_data['vitals']
        vitals = Vitals(
            hrpmin=vital_data['hrpmin'],
            mm_hg=vital_data['mmHg'],
            rr=vital_data['RR'],
            sp_o2=vital_data['SpO2%'],
            pain=vital_data['pain']
        )
        casualty = Casualty(
            id="casualty_" + str(uuid.uuid4()),
            unstructured=casualty_data['unstructured'],
            name=casualty_data['name'],
            demographics=demograpics,
            injuries=injuries,
            vitals=vitals,
            mental_status=casualty_data['mental_status'],
            assessed=False,
            tag=None
        )
        return casualty

    def _generate_casualty_simulations(self, casualty_data) -> CasualtySimulation:
        """
        Generate a CasualtySimulation instance from the YAML data.

        Args:
            casualty_data: The YAML data representing a casualty simulation.

        Returns:
            A CasualtySimulation object representing the generated casualty simulation.
        """
        casualty = self._generate_casualty(casualty_data=casualty_data)
        hidden_attributes = casualty_data['hidden_attributes']
        vitals_changes = hidden_attributes['vitals_changes_over_time']
        casualty_simulation = CasualtySimulation(
            casualty=casualty,
            correct_tag=hidden_attributes['correct_tag'],
            start_vitals=copy.deepcopy(casualty.vitals),
            current_vitals=copy.deepcopy(casualty.vitals),
            treatments_applied=[],
            treatments_needed=hidden_attributes['treatements_needed'],
            hrpmin_change=vitals_changes['hrpmin'],
            mmhg_change=vitals_changes['mmHg'],
            rr_change=vitals_changes['RR'],
            spo2_change=vitals_changes['SpO2%'],
            stable=hidden_attributes['stable'],
            deceased=hidden_attributes['deceased'],
            deceased_after_minutes=hidden_attributes['deceased_after_minutes']
        )
        return casualty_simulation

    def _generate_triage_categories(self) -> List[TriageCategory]:
        return [
            TriageCategory("minimal", "", "")
        ]
