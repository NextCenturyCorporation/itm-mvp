from enum import Enum
from swagger_client.models import Scenario, State, ProbeResponse
from .itm_scenario_runner import ScenarioRunner


class CommandOption(Enum):
    START = "start (s)"
    ALIGNMENT_TARGETS = "alignment targets (a)"
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
        self.current_probe_options = {}

    def get_full_string_and_shortcut(self, parts):
        if isinstance(parts, CommandOption):
            parts = parts.value
        parts = parts.split()
        full = parts[0]
        shortcut = [parts[1][1]]
        return [full] + shortcut

    def get_probe_option_id(self):
        probe_option_id = input(
            f"Enter Probe option Number from the list:\n"
            f"{[f'({i + 1}, {option.id})' for i, option in enumerate(self.current_probe_options)]}: "
        )
        try:
            probe_option_index = int(probe_option_id) - 1
            probe_option_id = self.current_probe_options[probe_option_index].id
        except ValueError:
            return self.get_probe_option_id()
        except IndexError:
            return self.get_probe_option_id()
        return probe_option_id

    def get_patient_id(self):
        patient_id = input(
            f"Enter Casualty Number from the list:\n"
            f"{[f'({i + 1}, {patient.id})' for i, patient in enumerate(self.patients)]}: "
        )
        try:
            patient_index = int(patient_id) - 1
            patient_id = self.patients[patient_index].id
        except ValueError:
            return self.get_patient_id()
        except IndexError:
            return self.get_patient_id()
        return patient_id
    
    def get_medical_supplies(self):
        medical_supply = input(
            f"Enter Medical Supply Number or Name from the list:\n"
            f"{[f'({i + 1}, {medical_supply.type})' for i, medical_supply in enumerate(self.medical_supplies)]}: "
        )
        try:
            medical_supply_index = int(medical_supply) - 1
            medical_supply = self.medical_supplies[medical_supply_index].type
        except ValueError:
            pass
        return medical_supply

    def get_justification(self):
        justification = input(
            f"Enter optional justification, or <Enter> to skip: "
        )
        return justification

    def start_scenario_operation(self, temp_username):
        response: Scenario = self.itm.start_scenario(temp_username)
        self.scenario_id = response.id
        self.scenario = response
        state: State = response.state
        self.patients = state.casualties
        self.medical_supplies = response.state.supplies
        return response

    def alignment_targets_operation(self):
        if self.scenario_id == None:
            response = "No active scenario; please start a scenario first."
        else:
            response = self.itm.get_alignment_target(self.scenario_id)
        return response

    def probe_scenario_operation(self):
        if self.scenario_id == None:
            response = "No active scenario; please start a scenario first."
        else:
            response = self.itm.get_probe(scenario_id=self.scenario_id)
            self.current_probe_id = response.id
            self.current_probe_options = response.options
        return response

    def respond_probe_operation(self):
        if self.scenario_id == None:
            response = "No active scenario; please start a scenario first."
        elif self.current_probe_id == '':
            response = "No active probe; please request a probe first."
        else:
            command_2 = input(
                f"Enter a Probe ID. To use the last received Probe ID "
                f"{self.current_probe_id}, enter 'p': "
            )
            if command_2 == 'p':
                command_2 = self.current_probe_id
            command_3 = self.get_probe_option_id()
            command_4 = self.get_justification()
            body=ProbeResponse(
                scenario_id=self.scenario_id,
                probe_id=command_2,
                choice=command_3
            )
            if len(command_4) > 0:
                body.justification = command_4
            response = self.itm.respond_to_probe(body)
        return response

    def status_scenario_operation(self):
        if self.scenario_id == None:
            response = "No active scenario; please start a scenario first."
        else:
            response = self.itm.get_scenario_state(scenario_id=self.scenario_id)
            self.medical_supplies = response.supplies
        return response

    def vitals_scenario_operation(self):
        if self.scenario_id == None:
            response = "No active scenario; please start a scenario first."
        else:
            command_2 = self.get_patient_id()
            response = self.itm.get_vitals(
                casualty_id=command_2
            )
        return response

    def heart_rate_scenario_operation(self):
        if self.scenario_id == None:
            response = "No active scenario; please start a scenario first."
        else:
            command_2 = self.get_patient_id()
            response = self.itm.get_heart_rate(
                casualty_id=command_2
            )
        return response

    def get_tagType(self):
        command_3 = input(
            f"Enter tag from following options "
            f"{[tag.value for tag in TagTypes]}: "
        ).lower()
        if len(command_3) == 1:
            found = False
            for tag in [tag.value for tag in TagTypes]:
                tag_type = self.get_full_string_and_shortcut(tag)
                if command_3 == tag_type[1]:
                    command_3 = tag_type[0]
                    found = True
                    break
            if found:
                return command_3
            else:
                return self.get_tagType()
        else:
            return self.get_tagType()

    def tag_scenario_operation(self):
        if self.scenario_id == None:
            response = "No active scenario; please start a scenario first."
        else:
            command_2 = self.get_patient_id()
            command_3 = self.get_tagType()
            response = self.itm.tag_patient(
                casualty_id=command_2,
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
        elif command_1 in self.get_full_string_and_shortcut(CommandOption.ALIGNMENT_TARGETS):
            response = self.alignment_targets_operation()
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
        if response != None:
            print(response)

        if command_1 in self.get_full_string_and_shortcut(CommandOption.END):
            self.scenario_complete = True
            print("Ending Session...")
        if isinstance(response, State):
            if response.scenario_complete:
                self.scenario_complete = True
                print("Scenario Complete: Ending Session...")
