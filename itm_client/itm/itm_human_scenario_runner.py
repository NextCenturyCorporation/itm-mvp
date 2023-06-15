from enum import Enum
from swagger_client.models import Scenario, ScenarioState
from .itm_scenario_runner import ScenarioRunner


class CommandOption(Enum):
    START = "start (s)"
    PROBE = "probe (p)"
    STATUS = "status (u)"
    VITALS = "vitals (v)"
    RESPOND = "respond (r)"
    HEART_RATE = "heart (h)"
    TAG = "tag (t)"
    END = "end (e)"


class TagTypes(Enum):
    MINIMAL = "minimal (m)"
    DELAYED = "delayed (d)"
    IMMEDIATE = "immediate (i)"
    EXPECTANT = "expectant (e)"
    DECEASED = "deceased (x)"


class ITMHumanScenarioRunner(ScenarioRunner):
    def __init__(self, save_to_db, scene_type):
        super().__init__()
        self.username = scene_type + "ITM Human" + save_to_db
        self.scenario_complete = False
        self.scenario_id = None
        self.patients = {}
        self.medical_supplies = {}
        self.current_probe_id = ''

    def get_full_string_and_shortcut(self, parts):
        if isinstance(parts, CommandOption):
            parts = parts.value
        parts = parts.split()
        full = parts[0]
        shortcut = [parts[1][1]]
        return [full] + shortcut

    def get_patient_id(self):
        patient_id = input(
            f"Enter Patient Number or ID from the list:\n"
            f"{[f'({i + 1}, {patient.id})' for i, patient in enumerate(self.patients)]}: "
        )
        try:
            patient_index = int(patient_id) - 1
            patient_id = self.patients[patient_index].id
        except ValueError:
            pass
        return patient_id
    
    def get_medical_supplies(self):
        medical_supply = input(
            f"Enter Medical Supply Number or Name from the list:\n"
            f"{[f'({i + 1}, {medical_supply.name})' for i, medical_supply in enumerate(self.medical_supplies)]}: "
        )
        try:
            medical_supply_index = int(medical_supply) - 1
            medical_supply = self.medical_supplies[medical_supply_index].name
        except ValueError:
            pass
        return medical_supply

    def start_scenario_operation(self, temp_username):
        response: Scenario = self.itm.start_scenario(temp_username)
        self.scenario_id = response.id
        self.scenario = response
        self.patients = response.patients
        self.medical_supplies = response.medical_supplies
        return response

    def probe_scenario_operation(self):
        response = self.itm.get_probe(scenario_id=self.scenario_id)
        self.current_probe_id = response.id
        return response

    def respond_probe_operation(self):
        command_2 = input(
            f"Enter a Probe ID. To use the last received Probe ID "
            f"{self.current_probe_id}, enter 'p': "
        )
        command_3 = self.get_patient_id()
        command_4 = self.get_medical_supplies()
        if command_2 == 'p':
            command_2 = self.current_probe_id
        try:
            patient_index = int(command_3) - 1
            patient_id = self.patients[patient_index].id
        except ValueError:
            patient_id = command_3
        response = self.itm.respond_to_probe(
            probe_id=command_2,
            patient_id=patient_id,
            explanation=command_4
        )
        return response

    def status_scenario_operation(self):
        response = self.itm.get_scenario_state(scenario_id=self.scenario_id)
        self.medical_supplies = response.medical_supplies
        return response

    def vitals_scenario_operation(self):
        command_2 = self.get_patient_id()
        response = self.itm.get_patient_vitals(
            scenario_id=self.scenario_id,
            patient_id=command_2
        )
        print(response)
        return response

    def heart_rate_scenario_operation(self):
        command_2 = self.get_patient_id()
        response = self.itm.get_patient_heart_rate(
            scenario_id=self.scenario_id,
            patient_id=command_2
        )
        return response

    def tag_scenario_operation(self):
        command_2 = self.get_patient_id()
        command_3 = input(
            f"Enter tag from following options "
            f"{[tag.value for tag in TagTypes]}: "
        )
        if len(command_3) == 1:
            for tag in [tag.value for tag in TagTypes]:
                tag_type = self.get_full_string_and_shortcut(tag)
                if command_3 == tag_type[1]:
                    command_3 = tag_type[0]
                    break
        response = self.itm.tag_patient(
            scenario_id=self.scenario_id,
            patient_id=command_2,
            tag=command_3
        )
        return response

    def run(self):
        while not self.scenario_complete:
            command_1 = input(
                f"Enter a Command from the following options "
                f"{[command_option.value for command_option in CommandOption]}: "
            ).lower()
            response = None
            self.perform_operations(command_1, response)
        print("ITM Scenario Ended")

    def perform_operations(self, command_1, response):
        if command_1 in self.get_full_string_and_shortcut(CommandOption.START):
            response = self.start_scenario_operation(self.username)
        elif command_1 in self.get_full_string_and_shortcut(CommandOption.PROBE):
            response = self.probe_scenario_operation()
        elif command_1 in self.get_full_string_and_shortcut(CommandOption.RESPOND):
            response = self.respond_probe_operation()
        elif command_1 in self.get_full_string_and_shortcut(CommandOption.STATUS):
            response = self.status_scenario_operation()
        elif command_1 in self.get_full_string_and_shortcut(CommandOption.VITALS):
            response = self.vitals_scenario_operation()
        elif command_1 in self.get_full_string_and_shortcut(CommandOption.HEART_RATE):
            response = self.heart_rate_scenario_operation()
        elif command_1 in self.get_full_string_and_shortcut(CommandOption.TAG):
            response = self.tag_scenario_operation()
        print(response)

        if command_1 in self.get_full_string_and_shortcut(CommandOption.END):
            self.scenario_complete = True
            print("Ending Session...")
        if isinstance(response, ScenarioState):
            if response.scenario_complete:
                self.scenario_complete = True
                print("Scenario Complete: Ending Session...")
