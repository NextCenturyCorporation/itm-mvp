from dataclasses import dataclass
from typing import List, Union
import copy
from swagger_server.models.patient import Patient
from swagger_server.models.scenario import Scenario
from swagger_server.models.vitals import Vitals


@dataclass
class PatientSimulation:
    """Class to represent a patient simulation over time."""
    patient: Patient
    correct_tag: str
    start_vitals: Vitals
    current_vitals: Vitals
    treatments_applied: str
    treatments_needed: List[str]
    stable: bool
    deceased: bool

    # A value less than 0 (ex. -1) ensures the patient does not die
    deceased_after_minutes: float

    heart_rate_index: int = 0
    heart_rate_change: Union[int, List[int]] = 0
    respiratory_rate_index: int = 0
    respiratory_rate_change: Union[int, List[int]] = 0
    oxygen_level_index: int = 0
    oxygen_level_change: Union[int, List[int]] = 0
    systolic_index: int = 0
    blood_pressure_change_systolic: Union[int, List[int]] = 0
    diastolic_index: int = 0
    blood_pressure_change_diastolic: Union[int, List[int]] = 0


class ITMPatientSimulator:
    """Class to represent and manipulate a patient during the simulation."""

    def __init__(self):
        """
        Initialize an instance of ITMPatientSimulator.
        """
        self.scenario: Scenario
        self.patient_simulations: List[PatientSimulation]

    def get_change(self, vital_value, index_attr, patient):
        """
        Get the change value for a vital based on the index attribute.

        Args:
            vital_value: The value of the vital (can be int or list of int).
            index_attr: The index attribute corresponding to the vital.
            patient: The patient simulation object.

        Returns:
            The change value for the vital.
        """
        if isinstance(vital_value, list):
            index = getattr(patient, index_attr)
            if index < len(vital_value):
                change = vital_value[index]
                if index + 1 == len(vital_value):
                    return change
                setattr(patient, index_attr, index + 1)
                return change
        return vital_value

    def get_vital_changes(self, patient: PatientSimulation):
        """
        Get the changes in vital signs for a patient simulation.

        Args:
            patient: The patient simulation object.

        Returns:
            A tuple containing the changes in vital signs.
        """
        heart_rate_change = self.get_change(
            patient.heart_rate_change, 'heart_rate_index', patient)
        resp_rate_change = self.get_change(
            patient.respiratory_rate_change, 'respiratory_rate_index', patient)
        oxygen_change = self.get_change(
            patient.oxygen_level_change, 'oxygen_level_index', patient)
        systolic_change = self.get_change(
            patient.blood_pressure_change_systolic, 'systolic_index', patient)
        diastolic_change = self.get_change(
            patient.blood_pressure_change_diastolic, 'diastolic_index', patient)

        return (heart_rate_change, resp_rate_change, oxygen_change,
                systolic_change, diastolic_change)

    def update_vitals(self, time_elapsed_scenario_time: float) -> None:
        """
        Update the vitals of patient simulations based on elapsed time.

        Args:
            time_elapsed_scenario_time: The elapsed time in the scenario.

        Returns:
            None.
        """
        for patient in self.patient_simulations:
            if patient.stable or patient.deceased:
                continue

            if patient.deceased_after_minutes > 0:
                if time_elapsed_scenario_time >= patient.deceased_after_minutes:
                    patient.deceased = True
                    self.terminate_patient(patient)
                    continue

            vital_changes = self.get_vital_changes(patient)
            patient.current_vitals.heart_rate += vital_changes[0]
            patient.current_vitals.respiratory_rate += vital_changes[1]
            patient.current_vitals.oxygen_level += vital_changes[2]

            systolic, diastolic = map(int,
                                      patient.current_vitals.blood_pressure.split('/'))
            systolic += vital_changes[3]
            diastolic += vital_changes[4]
            patient.current_vitals.blood_pressure = f"{systolic}/{diastolic}"

            patient.patient.vitals = copy.deepcopy(patient.current_vitals)

    def terminate_patient(self, patient: PatientSimulation):
        """
        Terminate a patient by making all of their vital signs
        set to zero.

        Args:
            patient: The patient simulation object to terminate.

        Returns:
            None.
        """
        patient.current_vitals.heart_rate = 0
        patient.current_vitals.respiratory_rate = 0
        patient.current_vitals.oxygen_level = 0
        patient.current_vitals.blood_pressure = "0/0"
        patient.patient.vitals = copy.deepcopy(patient.current_vitals)

    def treat_patient(self, patient_id: str, medical_supply: str,
                      medical_supply_details: dict) -> float:
        """
        Treat a patient with a medical supply.

        Args:
            patient_id: The ID of the patient.
            medical_supply: The name of the medical supply.
            medical_supply_details: The details of all medical supplies.

        Returns:
            The time elapsed during the treatment as a float.
        """
        for patient in self.patient_simulations:
            if patient.patient.id == patient_id:
                patient.stable = True
                patient.treatments_applied.append(medical_supply)
                for supply in self.scenario.medical_supplies:
                    if supply.name == medical_supply:
                        supply.quantity -= 1
                time_elapsed = medical_supply_details[medical_supply].time_to_apply
                return time_elapsed

    def check_on_setup_if_patients_are_deceased(self) -> None:
        """
        Checks if a patient is deceased on a scenario's start. If the patient
        is deceased then the patient's vitals is terminated and their vitals 
        are all set to zero.

        Returns:
            None.
        """
        for patient in self.patient_simulations:
            if patient.deceased:
                self.terminate_patient(patient)
                continue

    def setup_patients(self, scenario: Scenario,
                       patient_simulations: List[PatientSimulation]) -> None:
        """
        Set up patients in the patient simulator.

        Args:
            scenario: The scenario object containing the patients.
            patient_simulations: A list of patient simulation objects.

        Returns:
            None.
        """
        self.scenario = scenario
        self.patient_simulations = patient_simulations
        self.check_on_setup_if_patients_are_deceased()
