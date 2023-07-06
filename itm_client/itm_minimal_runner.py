"""
This script is a simple example for running ITM-TA2 evaluation 
scenarios through an ItmTa2EvalApi hosted on a local server.

Sessions are initiated with a specified session type and a maximum scenario limit. 
The script starts a session and then enters a loop:

1. Starts a scenario in that session.
2. Checks if the scenario session_complete property is True.
   If it is, then it ends the session.
3. Requests and answers all probes for that scenario.
4. Checks if the scenario state's 'scenario_complete' property is True.
   If it is, then it ends the scenario.

A response for each probe is randomly selected from the given options. 
Session types can be 'test', 'adept', or 'soartech'. If the 'eval' 
argument is used, then an eval session type is initiated. 
It uses argparse to handle command-line arguments for the
session type, scenario count, and adm_name.

Omitting max_scenarios or setting it to 0 will run only the available scenarios.
Any number higher than 0 (e.g. 1000) will repeat scenarios if there are not
enough unique scenarios available, but is ignored if --eval is specified.

Note: The --eval arg must be supported in the command line and called with
api.start_session(adm_name=args.adm_name, session_type='eval')

Note: The 'answer_probe' function provides random responses to each probe.
The function should be extended with decision-making logic.
"""

import argparse
import swagger_client
import random
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient
from swagger_client.models import Scenario, State, Probe, ProbeResponse

def answer_probe(probe: Probe, scenario_id: str):
    probe_choice = random.choice(probe.options)
    body = ProbeResponse(
        scenario_id=scenario_id, probe_id=probe.id,
        choice=probe_choice.id, justification='Justification'
    )
    return body

def main():
    parser = argparse.ArgumentParser(description='Runs ADM scenarios.')
    parser.add_argument('--adm_name', type=str, required=True, 
                        help='Specify the ADM name')
    parser.add_argument('--session', nargs='*', default=[], 
                        metavar=('session_type', 'scenario_count'), 
                        help='Specify session type and scenario count. '
                        'Session type can be test, adept, or soartech. '
                        'If you want to run through all available scenarios '
                        'without repeating do not use the scenario_count '
                        'argument')
    parser.add_argument('--eval', action='store_true', default=False, 
                        help='Run an evaluation session. '
                        'Supercedes --session and is the default if nothing is specified. '
                        'Implies --db.')

    args = parser.parse_args()
    if args.session:
        if args.session[0] not in ['soartech', 'adept', 'test']:
            parser.error("Invalid session type. It must be one of 'soartech', 'adept', or 'test'.")
        else:
            session_type = args.session[0]
    else:
        session_type = 'eval'
    scenario_count = int(args.session[1]) if len(args.session) > 1 else 0

    config = Configuration()
    config.host = "http://127.0.0.1:8080"
    api_client = ApiClient(configuration=config)
    itm = swagger_client.ItmTa2EvalApi(api_client=api_client)

    if args.eval:
        itm.start_session(
            adm_name=args.adm_name,
            session_type='eval'
        )
    else:
        itm.start_session(
            adm_name=args.adm_name,
            session_type=session_type,
            max_scenarios=scenario_count
        )

    while True:
        scenario: Scenario = itm.start_scenario(args.adm_name)
        if scenario.session_complete:
            break

        state: State = scenario.state
        while not state.scenario_complete:
            probe: Probe = itm.get_probe(scenario.id)
            probe_response_body = answer_probe(probe, scenario.id)
            state = itm.respond_to_probe(body=probe_response_body)
        print(f'scenario: {scenario.id} complete')
    print(f'Session complete')


if __name__ == "__main__":
    main()
