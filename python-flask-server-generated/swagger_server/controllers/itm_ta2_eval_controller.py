import connexion
import six

from swagger_server.models.alignment_target import AlignmentTarget  # noqa: E501
from swagger_server.models.probe import Probe  # noqa: E501
from swagger_server.models.probe_response import ProbeResponse  # noqa: E501
from swagger_server.models.scenario import Scenario  # noqa: E501
from swagger_server.models.state import State  # noqa: E501
from swagger_server.models.vitals import Vitals  # noqa: E501
from swagger_server import util


def check_vitals(casualty_id):  # noqa: E501
    """Assess and retrieve all casualty vital signs

    Retrieve all vital signs of the specified casualty.  Not required for MVP, but anticipated as an example of finer-grained choices that may be available post-MVP # noqa: E501

    :param casualty_id: The ID of the casualty to query
    :type casualty_id: str

    :rtype: Vitals
    """
    return 'do some magic!'


def get_alignment_target(scenario_id):  # noqa: E501
    """Retrieve alignment target for the scenario

    Retrieve alignment target for the scenario with the specified id # noqa: E501

    :param scenario_id: The ID of the scenario for which to retrieve alignment target
    :type scenario_id: str

    :rtype: AlignmentTarget
    """
    return 'do some magic!'


def get_heart_rate(casualty_id):  # noqa: E501
    """Check casualty heart rate

    Check the heart rate of the specified casualty.  Not required for MVP, but anticipated as an example of finer-grained choices that may be available post-MVP # noqa: E501

    :param casualty_id: The ID of the casualty to for which to request heart rate
    :type casualty_id: str

    :rtype: int
    """
    return 'do some magic!'


def get_probe(scenario_id):  # noqa: E501
    """Request a probe

    Request the next probe of the scenario with the specified id # noqa: E501

    :param scenario_id: The ID of the scenario for which to request a probe
    :type scenario_id: str

    :rtype: Probe
    """
    return 'do some magic!'


def get_scenario_state(scenario_id):  # noqa: E501
    """Retrieve scenario state

    Retrieve state of the scenario with the specified id # noqa: E501

    :param scenario_id: The ID of the scenario for which to retrieve status
    :type scenario_id: str

    :rtype: State
    """
    return 'do some magic!'


def respond_to_probe(body=None):  # noqa: E501
    """Respond to a probe

    Respond to a probe with a decision chosen from among its options # noqa: E501

    :param body: the selection by a DM of an option in response to a probe
    :type body: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        body = ProbeResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def start_scenario(adm_name):  # noqa: E501
    """Start a new scenario

    Start a new scenario with the specified ADM name, returning a Scenario object and unique id # noqa: E501

    :param adm_name: A self-assigned ADM name.  Can add authentication later.
    :type adm_name: str

    :rtype: Scenario
    """
    return 'do some magic!'


def tag_casualty(casualty_id, tag):  # noqa: E501
    """Tag a casualty with a triage category

    Apply a triage tag to the specified casualty with the specified tag # noqa: E501

    :param casualty_id: The ID of the casualty to tag
    :type casualty_id: str
    :param tag: The tag to apply to the casualty, chosen from triage categories
    :type tag: str

    :rtype: str
    """
    return 'do some magic!'
