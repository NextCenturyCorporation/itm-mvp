from dataclasses import dataclass
from typing import List, Dict
from swagger_server.models.medical_supply import MedicalSupply


@dataclass
class MedicalSupplyDetails:
    """Class to represent Medical Supply details"""
    medical_supply: MedicalSupply = None
    time_to_apply: float = 0


class ITMMedicalSupplies():
    def __init__(self):
        self.medical_supply_details: Dict[str, MedicalSupplyDetails] = {}

    def setup_medical_supply(self, medical_supplies, time_to_apply):
        for medical_supply in medical_supplies:
            medical_supply_details = MedicalSupplyDetails(
                medical_supply=medical_supply,
                time_to_apply=time_to_apply
            )
            self.medical_supply_details[medical_supply.name] = \
                medical_supply_details