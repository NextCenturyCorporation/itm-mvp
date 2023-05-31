import swagger_client
from enum import Enum
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient
from swagger_client.models import Scenario
from abc import ABC, abstractmethod


class CommandOption(Enum):
    START = "start"
    PROBE = "probe"
    STATUS = "status"
    VITALS = "vitals"
    RESPOND = "respond"
    HEART_RATE = "heart rate"
    END = "end"


class ScenarioRunner(ABC):
    def __init__(self):
        self.itm = self.setup_itm_session()
        self.username = ""
        self.scenario: Scenario = None

    def setup_itm_session(self):
        config = Configuration()
        config.host = "http://127.0.0.1:8080"
        api_client = ApiClient(configuration=config)
        return swagger_client.DefaultApi(api_client=api_client)


    @abstractmethod
    def run(self):
        pass
