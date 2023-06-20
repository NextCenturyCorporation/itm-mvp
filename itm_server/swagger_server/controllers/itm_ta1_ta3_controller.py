import connexion
import six

from swagger_server.models.probe import Probe  # noqa: E501
from swagger_server.models.scenario import Scenario  # noqa: E501
from swagger_server import util


def add_probe(body, api_key, scenario_id):  # noqa: E501
    """Create a new evaluation probe

    Create a new evaluation probe for the specified scenario. # noqa: E501

    :param body: Create a new evaluation probe
    :type body: dict | bytes
    :param api_key: API Key received when logging in.  Can add robust authentication later.
    :type api_key: str
    :param scenario_id: A scenario ID, as returned when adding a scenario
    :type scenario_id: str

    :rtype: str
    """
    if connexion.request.is_json:
        body = Probe.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_scenario(body, api_key):  # noqa: E501
    """Create a new evaluation scenario

    Create a new evaluation scenario # noqa: E501

    :param body: Create a new evaluation scenario
    :type body: dict | bytes
    :param api_key: API Key received when logging in.  Can add robust authentication later.
    :type api_key: str

    :rtype: str
    """
    if connexion.request.is_json:
        body = Scenario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_probe(api_key, probe_id):  # noqa: E501
    """Delete an evaluation probe

    Delete an evaluation probe by id # noqa: E501

    :param api_key: API Key received when logging in.  Can add robust authentication later.
    :type api_key: str
    :param probe_id: A scenario ID, as returned when adding a scenario
    :type probe_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_scenario(api_key, scenario_id):  # noqa: E501
    """Delete an evaluation scenario

    Delete an evaluation scenario by id # noqa: E501

    :param api_key: API Key received when logging in.  Can add robust authentication later.
    :type api_key: str
    :param scenario_id: A scenario ID, as returned when adding a scenario
    :type scenario_id: str

    :rtype: None
    """
    return 'do some magic!'


def ta1login(username):  # noqa: E501
    """Log in with TA3

    Start a new API session with the specified username # noqa: E501

    :param username: A self-assigned user name.  Can add authentication later.
    :type username: str

    :rtype: str
    """
    return 'do some magic!'


def update_probe(body, api_key):  # noqa: E501
    """Update an existing evaluation probe

    Update an existing evaluation probe by Id # noqa: E501

    :param body: new evaluation probe configuration
    :type body: dict | bytes
    :param api_key: API Key received when logging in.  Can add robust authentication later.
    :type api_key: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Probe.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_scenario(body, api_key):  # noqa: E501
    """Update an existing evaluation scenario

    Update an existing evaluation scenario by Id # noqa: E501

    :param body: new evaluation scenario configuration
    :type body: dict | bytes
    :param api_key: API Key received when logging in.  Can add robust authentication later.
    :type api_key: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Scenario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
