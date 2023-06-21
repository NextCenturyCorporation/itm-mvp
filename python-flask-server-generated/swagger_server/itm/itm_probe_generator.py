from typing import List
from swagger_server.models import (
    Probe,
    ProbeOption,
    Injury
)
from .itm_casualty_simulator import CasualtySimulation
from .itm_probe_system import ITMProbeSystem, ProbeObject


class ITMProbeGenerator(ITMProbeSystem):
    """Class to represent and manipulate the probe system."""

    def __init__(self):
        """
        Initialize an instance of ITMProbeGenerator.
        """
        super().__init__()


    def generate_probe(self, casualty_simulations: List[CasualtySimulation]) -> Probe:
        """
        Generate a probe.

        Args:
            casualty_simulations: A list of casualty simulation objects representing the casualties attributes over time.

        Returns:
            A Probe object representing the generated probe.
        """
        id = self._get_probe_id()
        prompt = self._generate_prompt(casualty_simulations)
        casualty_ids = [casualty.id for casualty in self.scenario.state.casualties]

        probe_options = [
            ProbeOption(
                id=self._get_probe_option_id(),
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
            this_casualtys_simulation = self._find_this_casualty_simulation(casualty, casualty_simulations)
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
