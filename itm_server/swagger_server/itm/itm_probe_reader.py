import glob
import os
import yaml
from typing import List, Dict
from dataclasses import dataclass, field
from swagger_server.models import Probe, ProbeOption, State
from .itm_probe_system import ITMProbeSystem


@dataclass
class ProbeYamlKDMAAssociation:
    knowledge: int = None
    denial: str = None
    mission: str = None

    @staticmethod
    def from_dict(obj: Dict):
        if (obj is not None):
            return ProbeYamlKDMAAssociation(
                knowledge=obj.get("knowledge"),
                denial=obj.get("denial"),
                mission=obj.get("mission")
            )
    
    def to_kdma_associtation(self):
        return {
            "knowledge": self.knowledge,
            "denial": self.denial,
            "mission": self.mission
        }
    

@dataclass 
class ProbeYamlOptions:
    id: str = None
    value: str = None
    kdma_association: ProbeYamlKDMAAssociation = None

    @staticmethod
    def from_dict(obj: Dict):
        return ProbeYamlOptions(
            id=obj.get("id"),
            value=obj.get("value"),
            kdma_association=ProbeYamlKDMAAssociation.from_dict(obj.get("kdma_association", {}))
        )
    
    def to_probe_option(self):
        return ProbeOption(
            id=self.id,
            value=self.value,
            kdma_association=self.kdma_association.to_kdma_associtation()
        )


@dataclass
class ProbeYaml:
    id: str = None
    scenario: str = None
    type: str = None
    prompt: str = None
    state: Dict = None
    options: List[ProbeYamlOptions] = field(default_factory=list)

    @staticmethod
    def from_dict(obj: Dict):
        return ProbeYaml(
            id=obj.get("id"),
            scenario=obj.get("scenario"),
            type=obj.get("type"),
            prompt=obj.get("prompt"),
            state=obj.get("state"),
            options=[ProbeYamlOptions.from_dict(option) for option in obj.get("options", [])]
        )
    
    def to_probe(self, state):
        options = [option.to_probe_option() for option in self.options]
        return Probe(
            id=self.id,
            scenario_id=self.scenario,
            type=self.type,
            prompt=self.prompt,
            state=state,
            options=options
        )


class ITMProbeReader(ITMProbeSystem):
    """Class to represent and manipulate the probe system."""

    def __init__(self, yaml_path):
        """
        Initialize an instance of ITMProbeReader.
        """
        super().__init__()
        self.probe_yamls: List[ProbeYaml] = self.read_all_probes_yamls_for_scenario(yaml_path)
        self.current_probe_index = 0
        self.probe_count = len(self.probe_yamls)

    def read_all_probes_yamls_for_scenario(self, yaml_path: str) -> List[ProbeYaml]:
        """
        Reads all probe YAML files from the provided 'yaml_path' directory and 
        its subdirectory named after 'scenario_name', and stores them in a list.
        """
        probe_yamls = []
        probe_files = sorted(glob.glob(os.path.join(yaml_path, 'probe*.yaml')))
        for filepath in probe_files:
            with open(filepath, 'r') as file:
                yaml_text = file.read()
                probe_yaml = self.read_probe_from_yaml(yaml_text)
                probe_yamls.append(probe_yaml)
        return probe_yamls

    def read_probe_from_yaml(self, yaml_text: str):
        probe_dict = yaml.safe_load(yaml_text)
        probe_yaml = ProbeYaml.from_dict(probe_dict)
        return probe_yaml

    def generate_probe(self, state: State) -> Probe:
        current_probe = self.probe_yamls[self.current_probe_index]
        state.unstructured = current_probe.state.get('unstructured', state.unstructured)
        probe = current_probe.to_probe(state)
        self.probes[probe.id] = probe
        
        return probe

