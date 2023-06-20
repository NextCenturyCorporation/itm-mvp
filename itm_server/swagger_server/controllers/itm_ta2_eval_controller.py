import connexion
from swagger_server.models.probe_response import ProbeResponse
from ..itm import ITMScenarioSession


def get_alignment_target(scenario_id):
    """Retrieve alignment target for the scenario

    Retrieve alignment target for the scenario with the specified id # noqa: E501

    :param scenario_id: The ID of the scenario for which to retrieve alignment target
    :type scenario_id: str

    :rtype: AlignmentTarget
    """
    return itm_session.get_alignment_target(scenario_id=scenario_id)


def get_heart_rate(casualty_id):
    """Check casualty heart rate

    Check the heart rate of the specified casualty.  Not implemented for MVP, but anticipated as an example of finer grained choice than \&quot;Treat patient B\&quot;. # noqa: E501

    :param casualty_id: The ID of the casualty to for which to request heart rate
    :type casualty_id: str

    :rtype: int
    """
    return itm_session.get_heart_rate(casualty_id=casualty_id)


def get_probe(scenario_id):
    """Request a probe

    Request the next probe of the scenario with the specified id # noqa: E501

    :param scenario_id: The ID of the scenario for which to request a probe
    :type scenario_id: str

    :rtype: Probe
    """
    return itm_session.get_probe(scenario_id=scenario_id)


def get_scenario_state(scenario_id):
    """Retrieve scenario state

    Retrieve state of the scenario with the specified id # noqa: E501

    :param scenario_id: The ID of the scenario for which to retrieve status
    :type scenario_id: str

    :rtype: State
    """
    return itm_session.get_scenario_state(scenario_id=scenario_id)


def get_vitals(casualty_id):
    """Assess and retrieve all casualty vital signs

    Retrieve all vital signs of the specified casualty.  Not implemented for MVP, but anticipated as an example of finer grained choice than \&quot;Treat patient B\&quot;. # noqa: E501

    :param casualty_id: The ID of the casualty to query
    :type casualty_id: str

    :rtype: Vitals
    """
    return itm_session.get_vitals(casualty_id=casualty_id)


def respond_to_probe(body):
    """Respond to a probe

    Respond to a probe with a decision chosen from among its options # noqa: E501

    :param body: the selection by a DM of an option in response to a probe
    :type body: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        body = ProbeResponse.from_dict(connexion.request.get_json())
    return itm_session.respond_to_probe(body=body)


def start_scenario(adm_name):
    """Start a new scenario

    Start a new scenario with the specified ADM name, returning a Scenario object and unique id # noqa: E501

    :param adm_name: A self-assigned ADM name.  Can add authentication later.
    :type adm_name: str

    :rtype: Scenario
    """
    global itm_session
    itm_session = ITMScenarioSession()
    return itm_session.start_scenario(adm_name=adm_name)


def tag_patient(casualty_id, tag):
    """Tag a casualty with a triage category

    Apply a triage tag to the specified casualty with the specified tag # noqa: E501

    :param casualty_id: The ID of the casualty to tag
    :type casualty_id: str
    :param tag: The tag to apply to the casualty, chosen from triage categories
    :type tag: str

    :rtype: str
    """
    return itm_session.tag_casualty(casualty_id=casualty_id, tag=tag)
