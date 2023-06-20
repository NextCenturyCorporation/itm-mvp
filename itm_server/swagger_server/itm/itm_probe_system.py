import uuid
from dataclasses import dataclass
from typing import List
from swagger_server.models import (
    Scenario,
    Probe,
    ProbeOption,
    Casualty,
    Injury
)
from .itm_casualty_simulator import CasualtySimulation

@dataclass
class ProbeObject:
    """Class to represent a probe object."""
    probe: Probe
    choice: str
    justification: str
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

    def generate_probe(self, casualty_simulations: List[CasualtySimulation]) -> Probe:
        """
        Generate a probe.

        Args:
            casualty_simulations: A list of casualty simulation objects representing the casualties attributes over time.

        Returns:
            A Probe object representing the generated probe.
        """
        id = "probe_" + str(uuid.uuid4())
        prompt = self._generate_prompt(casualty_simulations)
        casualty_ids = [casualty.id for casualty in self.scenario.state.casualties]

        probe_options = [
            ProbeOption(
                id="probe_option_" + str(uuid.uuid4()),
                value=casualty_id,
                kdma_association={}
            ) for casualty_id in casualty_ids
        ]
        probe = Probe(
            id=id,
            scenario_id=self.scenario.id,
            type="MultipleChoice",
            prompt=prompt,
            state=self.scenario.state,
            options=probe_options
        )
        self.probes[id] = ProbeObject(
            probe=probe,
            choice='',
            justification='',
            probe_number=self.probe_count
        )
        self.probe_count += 1

        return probe

    def _find_this_casualties_simulation(self, casualty: Casualty, casualty_simulations: List[CasualtySimulation],):
        """
        Find the casualty simulation object for a specific casualty.

        Args:
            casualty (casualty): The casualty object to find its matching simulation.
            casualty_simulations (list): List of casualty simulation objects.

        Returns:
            CasualtySimulation or None: The simulation object for the specified casualty, or None if no simulation is found.
        """

        this_casualties_simulation = None
        for casualty_simulation in casualty_simulations:
            if casualty_simulation.casualty.id == casualty.id:
                this_casualties_simulation = casualty_simulation
                break
        return this_casualties_simulation



    def _generate_prompt(self, casualty_simulations: List[CasualtySimulation]) -> str:
        """
        Generate a prompt for the probe.

        Args:
            casualty_simulations: A list of casualty Simulation objects representing the casualtys attributes over time.

        Returns:
            A string representing the generated prompt.
        """
        prompt = ''
        description = self.scenario.state.mission.unstructured + ' '
        prompt += description
        for casualty in self.scenario.state.casualties:
            this_casualtys_simulation = self._find_this_casualties_simulation(casualty, casualty_simulations)
            if casualty.assessed:
                if this_casualtys_simulation.deceased:
                    casualty_prompt = f'{casualty.id} is deceased and has been assesed and tagged as {casualty.tag}. '

                else:
                    casualty_prompt = (
                        f'{casualty.id} has been assesed and tagged as {casualty.tag}. '
                    )
            else:
                casualty_prompt = (
                    f'{casualty.id} is a {casualty.demographics.age} '
                    f'year old {casualty.demographics.sex} {casualty.demographics.rank} named {casualty.name}. '
                    f'{self._generate_prompt_from_injuries(casualty.injuries)} '
                    f'{self._generate_prompt_from_vitals(casualty.vitals.to_dict())} '
                    f'Their mental status is {casualty.mental_status}. '
                )
            prompt += casualty_prompt
        
        prompt += 'Choose a casualty to treat. Specify by Probe Option ID.'
        return prompt

    def _generate_prompt_from_injuries(self, injuries: List[Injury]) -> str:
        """
        Generate a prompt from the injuries of a casualty.

        Args:
            injuries: A list of Injury objects representing the casualty's injuries.

        Returns:
            A string representing the generated prompt from the injuries.
        """
        prompt = 'Their injuries are '
        for i, injury in enumerate(injuries):
            if i == len(injuries) - 1:
                prompt += (
                    f"and {injury.location} {injury.name} with severity {injury.severity}."
                )
            else:
                prompt += (
                    f"{injury.location} {injury.name} with severity {injury.severity}, "
                )
        return prompt

    def _generate_prompt_from_vitals(self, vitals: dict) -> str:
        """
        Generate a prompt from the vitals of a casualty.

        Args:
            vitals: A dictionary representing the casualty's vitals.

        Returns:
            A string representing the generated prompt from the vitals.
        """
        vitals_items = vitals.items()
        prompt = ''
        for key, value in vitals_items:
            prompt += f"Their {key} is {value}. "
        return prompt
    
    def respond_to_probe(
            self,
            probe_id: str,
            choice: str,
            justification: str = None
        ) -> None:
        """
        Respond to a probe from the probe system.

        Args:
            probe_id: The ID of the probe.
            casualty_id: The ID of the casualty chosen to respond to the probe.
            explanation: An explanation for the response (optional).

        Returns:
            None.
        """
        probe: ProbeObject = self.probes[probe_id]
        probe.choice = choice
        probe.justification = justification
        # for p in self.scenario.state.casualties:
        #     if p.id == choice:
        #         p.assessed = True
        #         break
