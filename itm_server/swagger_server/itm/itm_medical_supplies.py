from dataclasses import dataclass
from typing import List, Dict
from swagger_server.models.medical_supply import MedicalSupply


@dataclass
class MedicalSupplyDetails:
    """Class to represent Medical Supply details"""
    medical_supply: MedicalSupply = None
    time_to_apply: float = 0


class ITMMedicalSupplies:
    """
    Class for managing medical supplies in the ITM system.
    """

    def __init__(self):
        """
        Initialize an instance of ITMMedicalSupplies.
        """
        self.medical_supply_details: Dict[str, MedicalSupplyDetails] = {}

    def setup_medical_supply(self, medical_supplies: List[MedicalSupply], time_to_apply: float) -> None:
        """
        Set up medical supplies with their corresponding details.

        Args:
            medical_supplies: A list of MedicalSupply objects representing the available medical supplies.
            time_to_apply: The time taken to apply each medical supply in minutes.

        Returns:
            None
        """
        for medical_supply in medical_supplies:
            medical_supply_details = MedicalSupplyDetails(
                medical_supply=medical_supply,
                time_to_apply=time_to_apply
            )
            self.medical_supply_details[medical_supply.name] = medical_supply_details
