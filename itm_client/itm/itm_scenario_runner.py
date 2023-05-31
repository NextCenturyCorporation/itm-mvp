import swagger_client
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient
from swagger_client.models import (
    Scenario,
    Environment,
    Patient,
    Vitals,
    MedicalSupply,
    TriageCategory
)

OPTIONS = ["start", "probe", "status", "vitals", "respond", "heart rate", "end"]

class ITMScenarioRunner:
    def __init__(self):
        self.session_active = True
        self.itm = None
        self.scenario_id = None
        self.scenario: Scenario = None

    def setup_itm_session(self):
        config = Configuration()
        config.host = "http://127.0.0.1:8080"
        api_client = ApiClient(configuration=config)
        self.itm = swagger_client.DefaultApi(api_client=api_client)

    def run(self):
        self.setup_itm_session()
        while self.session_active:

            command_1 = input(f"Enter a Command from the following options {OPTIONS}: ")

            if command_1 == 'start':
                response: Scenario = self.itm.start_scenario("Test")
                self.scenario_id = response.id
                print(response)

            if command_1 == 'probe':
                response = self.itm.get_probe(
                    scenario_id=self.scenario_id
                )
                print(response)

            if command_1 == 'respond':
                command_2 = input("Enter Probe ID: ")
                command_3 = input("Enter Patient ID: ")
                command_4 = input("Enter Explanation: ")
                response = self.itm.respond_to_probe(
                    probe_id=command_2,
                    patient_id=command_3,
                    explanation=command_4
                )
                print(response)

            if command_1 == 'status':
                response = self.itm.get_scenario_state(
                    scenario_id=self.scenario_id
                )
                print(response)

            if command_1 == 'vitals':
                command_2 = input("Enter Patient ID: ")
                response = self.itm.get_patient_vitals(
                    scenario_id=self.scenario_id,
                    patient_id=command_2
                )
                print(response)

            if command_1 == 'heart rate':
                command_2 = input("Enter Patient ID: ")
                response = self.itm.get_patient_heart_rate(
                    scenario_id=self.scenario_id,
                    patient_id=command_2
                )
                print(response)

            if command_1 == 'end':
                self.session_active = False
                print("Ending Session...")
    
        print("ITM Scenario Ended")
