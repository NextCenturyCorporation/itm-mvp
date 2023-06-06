import time
import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import List
from swagger_server.models.scenario import Scenario
from swagger_server.models.probe import Probe
from swagger_server.models.patient import Patient
from swagger_server.models.injury import Injury
from .itm_patient_simulator import PatientSimulation

@dataclass
class ProbeObject:
    """Class to represent a probe object."""
    probe: Probe
    patient_id_chosen: str
    explanation: str
    probe_number: int

class ITMProbeSystem:
    """Class to represent and manipulate the probe system."""

    def __init__(self):
        """
        Initialize an instance of ITMProbeSystem.
        """
        self.scenario: Scenario = None
        self.probe_count = 0
        self.probes = {}

    def generate_probe(self, patient_simulations: List[PatientSimulation]) -> Probe:
        """
        Generate a probe.

        Args:
            patient_simulations: A list of Patient Simulation objects representing the patients attributes over time.

        Returns:
            A Probe object representing the generated probe.
        """
        id = "probe_" + str(uuid.uuid4())
        question = self._generate_question(patient_simulations)
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

    def _find_this_patients_simulation(self, patient: Patient, patient_simulations: List[PatientSimulation],):
        """
        Find the patient simulation object for a specific patient.

        Args:
            patient (Patient): The patient object to find its matching simulation.
            patient_simulations (list): List of patient simulation objects.

        Returns:
            PatientSimulation or None: The simulation object for the specified patient, or None if no simulation is found.
        """

        this_patients_simulation = None
        for patient_simulation in patient_simulations:
            if patient_simulation.patient.id == patient.id:
                this_patients_simulation = patient_simulation
                break
        return this_patients_simulation



    def _generate_question(self, patient_simulations: List[PatientSimulation]) -> str:
        """
        Generate a question for the probe.

        Args:
            patient_simulations: A list of Patient Simulation objects representing the patients attributes over time.

        Returns:
            A string representing the generated question.
        """
        question = ''
        description = self.scenario.description + '. '
        question += description
        for patient in self.scenario.patients:
            this_patients_simulation = self._find_this_patients_simulation(patient, patient_simulations)
            if this_patients_simulation.deceased:
                patient_question = f'{patient.id} is deceased. '
                if patient.assessed:
                    patient_question = patient_question.replace('. ', ' ')
                    patient_question += f'and has been assessed and tagged as {patient.tag}. '

            elif patient.assessed:
                patient_question = (
                    f'{patient.id} has been assesed and tagged as {patient.tag}. '
                )
            else:
                patient_question = (
                    f'{patient.id} is a {patient.age} '
                    f'year old {patient.sex} named {patient.name}. '
                    f'{self._generate_question_from_injuries(patient.injuries)} '
                    f'{self._generate_question_from_vitals(patient.vitals.to_dict())} '
                    f'Their mental status is {patient.mental_status}. '
                )
            question += patient_question
        
        question += 'Choose a patient to treat. Specify by patient ID.'
        return question

    def _generate_question_from_injuries(self, injuries: List[Injury]) -> str:
        """
        Generate a question from the injuries of a patient.

        Args:
            injuries: A list of Injury objects representing the patient's injuries.

        Returns:
            A string representing the generated question from the injuries.
        """
        question = 'Their injuries are '
        for i, injury in enumerate(injuries):
            if i == len(injuries) - 1:
                question += (
                    f"and {injury.location} {injury.name}."
                )
            else:
                question += (
                    f"{injury.location} {injury.name}, "
                )
        return question

    def _generate_question_from_vitals(self, vitals: dict) -> str:
        """
        Generate a question from the vitals of a patient.

        Args:
            vitals: A dictionary representing the patient's vitals.

        Returns:
            A string representing the generated question from the vitals.
        """
        vitals_items = vitals.items()
        question = ''
        for key, value in vitals_items:
            question += f"Their {key} is {value}. "
        return question
    
    def respond_to_probe(
            self,
            probe_id: str,
            patient_id: str,
            explanation: str = None
        ) -> None:
        """
        Respond to a probe from the probe system.

        Args:
            probe_id: The ID of the probe.
            patient_id: The ID of the patient chosen to respond to the probe.
            explanation: An explanation for the response (optional).

        Returns:
            None.
        """
        probe: ProbeObject = self.probes[probe_id]
        probe.patient_id_chosen = patient_id
        probe.explanation = explanation

        for p in self.scenario.patients:
            if p.id == patient_id:
                p.assessed = True
                break
