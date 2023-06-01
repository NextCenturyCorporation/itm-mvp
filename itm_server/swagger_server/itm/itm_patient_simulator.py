from dataclasses import dataclass
from typing import List
import copy
from swagger_server.models.patient import Patient
from swagger_server.models.scenario import Scenario
from swagger_server.models.vitals import Vitals


@dataclass
class PatientSimulation:
    """Class to represent a patient simulation over time."""
    patient: Patient  # The Patient class represented in the ITM API
    correct_tag: str  # The correct tag type for the patient
    start_vitals: Vitals  # Starting vitals of the patient
    current_vitals: Vitals  # Current vitals of the patient
    treatments_applied: str  # Treatments applied on the patient
    treatments_needed: List[str]  # Treatments needed by the patient
    is_stable: bool  # Dictates whether the vitals should stop changing

    # Changes in vitals over time
    heart_rate_change: int = 0
    blood_pressure_change_systolic: int = 0
    blood_pressure_change_diastolic: int = 0
    respiratory_rate_change: int = 0
    oxygen_level_change: int = 0


class ITMPatientSimulator:
    """Class to represent and manipulate a patient simulator."""
    def __init__(self):
        """Initialize an ITMPatientSimulator."""
        self.scenario: Scenario
        self.patient_simulations: List[PatientSimulation]

    def update_vitals(self) -> None:
        """Update the vitals of all patients in the simulation."""
        for patient in self.patient_simulations:
            if patient.is_stable:
                continue
            patient.current_vitals.heart_rate += patient.heart_rate_change
            patient.current_vitals.respiratory_rate += patient.respiratory_rate_change
            patient.current_vitals.oxygen_level += patient.oxygen_level_change

            systolic, diastolic = map(
                int, patient.current_vitals.blood_pressure.split('/')
            )
            systolic += patient.blood_pressure_change_systolic
            diastolic += patient.blood_pressure_change_diastolic
            patient.current_vitals.blood_pressure = f"{systolic}/{diastolic}"

            patient.patient.vitals = copy.deepcopy(patient.current_vitals)

    def treat_patient(self, patient_id, medical_supply) -> None:
        """Treat a patient with a given medical supply."""
        for patient in self.patient_simulations:
            if patient.patient.id == patient_id:
                patient.is_stable = True
                patient.treatments_applied.append(medical_supply)
                break

    def setup_patients(self, scenario: Scenario,
                       patient_simulations: List[PatientSimulation]) -> None:
        """Set up patients for the simulation."""
        self.scenario = scenario
        self.patient_simulations = patient_simulations
