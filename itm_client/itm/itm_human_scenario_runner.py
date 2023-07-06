from json import loads
from enum import Enum
from swagger_client.models import Scenario, State, ProbeResponse
from swagger_client.rest import ApiException
from .itm_scenario_runner import ScenarioRunner
import traceback


class CommandOption(Enum):
    SESSION = "start_session (s)"
    SCENARIO = "get_scenario (g)"
    ALIGNMENT_TARGETS = "alignment_targets (a)"
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
    def __init__(self, save_to_db, session_type, max_scenarios=-1):
        super().__init__()
        self.username = session_type + "ITM Human" + save_to_db
        self.session_type = session_type
        if max_scenarios > 0:
            self.max_scenarios = max_scenarios
        else:
            self.max_scenarios = None
        self.scenario_complete = False
        self.session_complete = False
        self.session_id = None
        self.scenario_id = None
        self.patients = {}
        self.medical_supplies = {}
        self.current_probe_id = ''
        self.current_probe_text = ''
        self.current_probe_options = {}
        self.current_probe_answered = False

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
            f"{[f'({i + 1}, {option.value})' for i, option in enumerate(self.current_probe_options)]}: "
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
        if self.scenario_id == None:
            response: Scenario = self.itm.start_scenario(temp_username)
            self.current_probe_answered = False
            self.current_probe_id = ''
            self.session_id = 'foobar' # ensure we don't start a new session
            if response.session_complete == False:
                self.scenario_id = response.id
                self.scenario = response
                state: State = response.state
                self.patients = state.casualties
                self.medical_supplies = response.state.supplies
            else:
                self.session_complete = True
        else:
            response = "Scenario is already started."
        return response

    def start_session_operation(self, temp_username):
        if self.session_id == None:
            if self.max_scenarios == None:
                response: Scenario = self.itm.start_session(temp_username, self.session_type)
            else:
                response: Scenario = self.itm.start_session(temp_username, self.session_type, max_scenarios=self.max_scenarios)
            self.session_id = 'foobar' # later, the API will return a session_id
        else:
            response = "Session is already started."
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
            self.current_probe_text = response.prompt
            self.current_probe_options = response.options
            self.current_probe_answered = False
        return response

    def respond_probe_operation(self):
        if self.scenario_id == None:
            response = "No active scenario; please start a scenario first."
        elif self.current_probe_id == '':
            response = "No active probe; please request a probe first."
        elif self.current_probe_answered == True:
            response = "You have already responded to that probe."
        else:
            print("Probe prompt: \"", self.current_probe_text, "\"")
            command_3 = self.get_probe_option_id()
            command_4 = self.get_justification()
            body=ProbeResponse(
                scenario_id=self.scenario_id,
                probe_id=self.current_probe_id,
                choice=command_3
            )
            if len(command_4) > 0:
                body.justification = command_4
            response = self.itm.respond_to_probe(body=body)
            if response.scenario_complete == True:
                self.scenario_complete = True
                self.scenario_id = None
            else:
                self.current_probe_answered = True
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
            response = self.itm.check_vitals(
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
            response = self.itm.tag_casualty(
                casualty_id=command_2,
                tag=command_3
            )
        return response

    def run(self):
        while not self.session_complete:
            command_1 = input(
                f"Enter a Command from the following options "
                f"{[command_option.value for command_option in CommandOption]}: "
            ).lower()
            response = None
            self.perform_operations(command_1, response)
        print("ITM Session Ended")

    def perform_operations(self, command_1, response):
        try:
            if command_1 in self.get_full_string_and_shortcut(CommandOption.SESSION):
                response = self.start_session_operation(self.username)
            elif command_1 in self.get_full_string_and_shortcut(CommandOption.SCENARIO):
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
        except ApiException as e:
            exception_body = loads(e.body.decode('utf-8')) # Parse the string as a JSON object
            print("ApiException: ", e.status, e.reason, f"Detail: \"{exception_body['detail']}\"")
        except Exception as e:
            print("Exception: ", e)
            traceback.print_exc()

        if response != None:
            print(response)

        if command_1 in self.get_full_string_and_shortcut(CommandOption.END):
            self.session_complete = True
            print("Ending Session...")
        elif isinstance(response, Scenario):
            if response.session_complete == True:
                self.session_complete = True # if there are no more scenarios, then the session is over
                print("Session Complete: Ending Session...")