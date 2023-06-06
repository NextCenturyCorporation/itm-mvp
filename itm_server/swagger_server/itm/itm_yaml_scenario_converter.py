import copy
import uuid
import yaml
from typing import Tuple, List
from .itm_patient_simulator import PatientSimulation
from .itm_medical_supplies import ITMMedicalSupplies, MedicalSupplyDetails
from swagger_server.models.environment import Environment
from swagger_server.models.injury import Injury
from swagger_server.models.medical_supply import MedicalSupply
from swagger_server.models.patient import Patient
from swagger_server.models.scenario import Scenario
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
            Tuple[Scenario, List[PatientSimulation]]:
        """
        Generate a Scenario and patient simulations from the YAML data.

        Returns:
            A tuple containing the generated Scenario, a list of PatientSimulation objects, and the MedicalSupplyDetails object.
        """
        patient_simulations = [
            self._generate_patient_simulations(patient_data)
            for patient_data in self.yaml_data['patients']
        ]
        medical_supply_details = ITMMedicalSupplies()
        medical_supplies = [
            self._generate_medical_supply(supply_data, medical_supply_details)
            for supply_data in self.yaml_data['medical_supplies']
        ]
        environment = self._generate_environment(
            self.yaml_data['environment']
        )

        scenario = Scenario(
            id="scenario_" + str(uuid.uuid4()),
            name=self.yaml_data['name'],
            description=self.yaml_data['description'],
            start_time=0,
            environment=environment,
            patients=[patient.patient for patient in patient_simulations],
            medical_supplies=medical_supplies,
            triage_categories=[]
        )

        return scenario, patient_simulations, medical_supply_details

    def _generate_patient(self, patient_data) -> Patient:
        """
        Generate a Patient instance from the YAML data.

        Args:
            patient_data: The YAML data representing a patient.

        Returns:
            A Patient object representing the generated patient.
        """
        injuries = [
            Injury(name=injury['name'], location=injury['location'])
            for injury in patient_data['injuries']
        ]
        vitals = Vitals(
            heart_rate=patient_data['vitals']['heart_rate'],
            blood_pressure=patient_data['vitals']['blood_pressure'],
            respiratory_rate=patient_data['vitals']['respiratory_rate'],
            oxygen_level=patient_data['vitals']['oxygen_level']
        )
        patient = Patient(
            id="patient_" + str(uuid.uuid4()),
            name=patient_data['name'],
            age=patient_data['age'],
            sex=patient_data['sex'],
            injuries=injuries,
            vitals=vitals,
            mental_status=patient_data['mental_status'],
            assessed=False,
            tag='none'
        )
        return patient

    def _generate_patient_simulations(self, patient_data) -> PatientSimulation:
        """
        Generate a PatientSimulation instance from the YAML data.

        Args:
            patient_data: The YAML data representing a patient simulation.

        Returns:
            A PatientSimulation object representing the generated patient simulation.
        """
        patient = self._generate_patient(patient_data=patient_data)
        vitals_changes = patient_data['vitals_changes_over_time']
        patient_simulation = PatientSimulation(
            patient=patient,
            correct_tag=patient_data['tag'],
            start_vitals=copy.deepcopy(patient.vitals),
            current_vitals=copy.deepcopy(patient.vitals),
            treatments_applied=[],
            treatments_needed=patient_data['treatements_needed'],
            heart_rate_change=vitals_changes['heart_rate_change'],
            blood_pressure_change_systolic=
                vitals_changes['blood_pressure_change_systolic'],
            blood_pressure_change_diastolic=
                vitals_changes['blood_pressure_change_diastolic'],
            respiratory_rate_change=vitals_changes['respiratory_rate_change'],
            oxygen_level_change=vitals_changes['oxygen_level_change'],
            stable=patient_data['stable'],
            deceased=patient_data['deceased'],
            deceased_after_minutes=patient_data['deceased_after_minutes']
        )
        return patient_simulation

    def _generate_medical_supply(self, supply_data, supply_details) -> MedicalSupply:
        """
        Generate a MedicalSupply instance from the YAML data.

        Args:
            supply_data: The YAML data representing a medical supply.
            supply_details: The ITMMedicalSupplies object to store the medical supply details.

        Returns:
            A MedicalSupply object representing the generated medical supply.
        """
        medical_supply = MedicalSupply(
            name=supply_data['name'],
            description=supply_data['description'],
            quantity=supply_data['quantity']
        )
        supply_details.medical_supply_details[medical_supply.name] = \
            MedicalSupplyDetails(
                medical_supply=medical_supply,
                time_to_apply=supply_data['time_to_apply_in_minutes']
            )
        return medical_supply

    def _generate_environment(self, environment_data) -> Environment:
        """
        Generate an Environment instance from the YAML data.

        Args:
            environment_data: The YAML data representing an environment.

        Returns:
            An Environment object representing the generated environment.
        """
        return Environment(
            weather=environment_data['weather'],
            location=environment_data['location'],
            visibility=environment_data['visibility'],
            noise_ambient=environment_data['noise_ambient'],
            noise_peak=environment_data['noise_peak'],
            threat_level=environment_data['threat_level']
        )
