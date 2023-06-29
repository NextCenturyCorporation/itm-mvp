import connexion
from swagger_server.models.probe_response import ProbeResponse
from ..itm import ITMScenarioSession

ITM_SESSION = ITMScenarioSession()
"""
The internal controller for ITM MVP
"""

def check_vitals(casualty_id):  # noqa: E501
    """Assess and retrieve all casualty vital signs

    Retrieve all vital signs of the specified casualty.  Not required for MVP, but anticipated as an example of finer-grained choices that may be available post-MVP # noqa: E501

    :param casualty_id: The ID of the casualty to query
    :type casualty_id: str

    :rtype: Vitals
    """
    return ITM_SESSION.get_vitals(casualty_id=casualty_id)


def get_alignment_target(scenario_id):  # noqa: E501
    """Retrieve alignment target for the scenario

    Retrieve alignment target for the scenario with the specified id # noqa: E501

    :param scenario_id: The ID of the scenario for which to retrieve alignment target
    :type scenario_id: str

    :rtype: AlignmentTarget
    """
    return ITM_SESSION.get_alignment_target(scenario_id=scenario_id)


def get_heart_rate(casualty_id):  # noqa: E501
    """Check casualty heart rate

    Check the heart rate of the specified casualty.  Not required for MVP, but anticipated as an example of finer-grained choices that may be available post-MVP # noqa: E501

    :param casualty_id: The ID of the casualty to for which to request heart rate
    :type casualty_id: str

    :rtype: int
    """
    return ITM_SESSION.get_heart_rate(casualty_id=casualty_id)


def get_probe(scenario_id):  # noqa: E501
    """Request a probe

    Request the next probe of the scenario with the specified id # noqa: E501

    :param scenario_id: The ID of the scenario for which to request a probe
    :type scenario_id: str

    :rtype: Probe
    """
    return ITM_SESSION.get_probe(scenario_id=scenario_id)


def get_scenario_state(scenario_id):  # noqa: E501
    """Retrieve scenario state

    Retrieve state of the scenario with the specified id # noqa: E501

    :param scenario_id: The ID of the scenario for which to retrieve status
    :type scenario_id: str

    :rtype: State
    """
    return ITM_SESSION.get_scenario_state(scenario_id=scenario_id)


def respond_to_probe(body=None):  # noqa: E501
    """Respond to a probe

    Respond to a probe with a decision chosen from among its options # noqa: E501

    :param body: the selection by a DM of an option in response to a probe
    :type body: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        body = ProbeResponse.from_dict(connexion.request.get_json())
    return ITM_SESSION.respond_to_probe(body=body)


def start_scenario(adm_name, scenario_id=None):  # noqa: E501
    """Get the next scenario

    Get the next scenario in a session with the specified ADM name, returning a Scenario object and unique id # noqa: E501

    :param adm_name: A self-assigned ADM name.  Can add authentication later.
    :type adm_name: str
    :param scenario_id: a scenario id to start, used internally by TA3
    :type scenario_id: str

    :rtype: Scenario
    """
    # 204 doesnt work :(
    # return 'No more scenarios', 204\
    return ITM_SESSION.start_scenario(
        adm_name=adm_name,
        scenario_id=scenario_id
    )


def start_session(adm_name, session_type, max_scenarios=None):  # noqa: E501
    """Start a new session

    Start a new session with the specified ADM name # noqa: E501

    :param adm_name: A self-assigned ADM name.  Can add authentication later.
    :type adm_name: str
    :param session_type: the type of session to start (test, eval, or a ta1 name)
    :type session_type: str
    :param max_scenarios: the maximum number of scenarios requested
    :type max_scenarios: int

    :rtype: str
    """
    ITM_SESSION.start_session(
        adm_name=adm_name,
        session_type=session_type,
        max_scenarios=max_scenarios,
        used_start_session=True
    )
    return f'Session started with session type: {session_type} and max scenarios {max_scenarios}'


def tag_casualty(casualty_id, tag):  # noqa: E501
    """Tag a casualty with a triage category

    Apply a triage tag to the specified casualty with the specified tag # noqa: E501

    :param casualty_id: The ID of the casualty to tag
    :type casualty_id: str
    :param tag: The tag to apply to the casualty, chosen from triage categories
    :type tag: str

    :rtype: str
    """
    return ITM_SESSION.tag_casualty(casualty_id=casualty_id, tag=tag)
