from swagger_client.models import (
    Scenario,
    Environment,
    Patient,
    Vitals,
    MedicalSupply,
    TriageCategory
)
from .itm_scenario_runner import ScenarioRunner, CommandOption


class ITMHumanScenarioRunner(ScenarioRunner):

    def __init__(self):
        super().__init__()
        self.username = "ITM Human Decision Maker"
        self.session_active = True
        self.scenario_id = None


    def run(self):
        while self.session_active:

            command_1 = input(f"Enter a Command from the following options {[command_option.value for command_option in CommandOption]}: ").lower()

            if command_1 == CommandOption.START.value:
                response: Scenario = self.itm.start_scenario("Test")
                self.scenario_id = response.id
                self.scenario = response
                print(response)

            if command_1 == CommandOption.PROBE.value:
                response = self.itm.get_probe(
                    scenario_id=self.scenario_id
                )
                print(response)

            if command_1 == CommandOption.RESPOND.value:
                command_2 = input("Enter Probe ID: ")
                command_3 = input("Enter Patient ID: ")
                command_4 = input("Enter Explanation: ")
                response = self.itm.respond_to_probe(
                    probe_id=command_2,
                    patient_id=command_3,
                    explanation=command_4
                )
                print(response)

            if command_1 == CommandOption.STATUS.value:
                response = self.itm.get_scenario_state(
                    scenario_id=self.scenario_id
                )
                print(response)

            if command_1 == CommandOption.VITALS.value:
                command_2 = input("Enter Patient ID: ")
                response = self.itm.get_patient_vitals(
                    scenario_id=self.scenario_id,
                    patient_id=command_2
                )
                print(response)

            if command_1 == CommandOption.HEART_RATE.value:
                command_2 = input("Enter Patient ID: ")
                response = self.itm.get_patient_heart_rate(
                    scenario_id=self.scenario_id,
                    patient_id=command_2
                )
                print(response)

            if command_1 == CommandOption.END:
                self.session_active = False
                print("Ending Session...")
    
        print("ITM Scenario Ended")
