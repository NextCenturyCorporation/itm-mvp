import connexion
import six

from swagger_server.models.probe import Probe  # noqa: E501
from swagger_server.models.scenario import Scenario  # noqa: E501
from swagger_server.models.scenario_state import ScenarioState  # noqa: E501
from swagger_server.models.vitals import Vitals  # noqa: E501
from swagger_server import util
from ..itm import ITMScenarioSession


def get_patient_heart_rate(scenario_id, patient_id):  # noqa: E501
    """Retrieve patient heart rate

    This is just here to discuss whether we will someday have/need this level of granularity, probably not for MVP # noqa: E501

    :param scenario_id: The ID of the scenario containing the specified patient
    :type scenario_id: str
    :param patient_id: The ID of the patient to for which to request heart rate
    :type patient_id: str

    :rtype: int
    """
    return itm_session.get_patient_heart_rate(
        scenario_id=scenario_id,
        patient_id=patient_id
    )


def get_patient_vitals(scenario_id, patient_id):  # noqa: E501
    """Retrieve all patient vital signs

    Retrieve all vital signs of the specified patient in the specified scenario.  May not need this for MVP. # noqa: E501

    :param scenario_id: The ID of the scenario for which to request patient vitals
    :type scenario_id: str
    :param patient_id: The ID of the patient to query
    :type patient_id: str

    :rtype: Vitals
    """
    return itm_session.get_patient_vitals(
        scenario_id=scenario_id,
        patient_id=patient_id
    )


def get_probe(scenario_id):  # noqa: E501
    """Request the next probe

    Request the next probe of the scenario with the specified id # noqa: E501

    :param scenario_id: The ID of the scenario for which to request a probe
    :type scenario_id: str

    :rtype: Probe
    """
    return itm_session.get_probe(
        scenario_id=scenario_id
    )


def get_scenario_state(scenario_id):  # noqa: E501
    """Retrieve scenario state

    Retrieve state of the scenario with the specified id # noqa: E501

    :param scenario_id: The ID of the scenario for which to retrieve status
    :type scenario_id: str

    :rtype: ScenarioState
    """
    return itm_session.get_scenario_state(
        scenario_id=scenario_id
    )


def respond_to_probe(probe_id, patient_id, explanation=None):  # noqa: E501
    """Respond to a probe

    Respond to the specified probe with the specified patient_id (decision) and optional explanation # noqa: E501

    :param probe_id: The ID of the probe to which to respond
    :type probe_id: str
    :param patient_id: The ID of the patient to treat
    :type patient_id: str
    :param explanation: An explanation of the response to the probe
    :type explanation: str

    :rtype: ScenarioState
    """
    return itm_session.respond_to_probe(
        probe_id=probe_id,
        patient_id=patient_id,
        explanation=explanation
    )


def start_scenario(username):  # noqa: E501
    """Start a new scenario

    Start a new scenario with the specified username, returning a Scenario object and unique id # noqa: E501

    :param username: A self-assigned user name.  Can add authentication later.
    :type username: str

    :rtype: Scenario
    """
    global itm_session
    itm_session = ITMScenarioSession()
    return itm_session.start_scenario(
        username=username
    )
