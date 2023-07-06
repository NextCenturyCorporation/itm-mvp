import sys
import argparse
from itm import ITMHumanScenarioRunner

def main():

    parser = argparse.ArgumentParser(description='Runs Human input simulator.')
    parser.add_argument('--db', action='store_true', default=False, help=\
                        "Put the output in the MongoDB (ensure that the itm_dashboard docker container is running) and save a json output file locally inside itm_server/itm_mvp_local_output/")
    parser.add_argument('--session', nargs='*', default=[], metavar=('session_type', 'scenario_count'), help=\
                        'Specify session type and scenario count. '
                        'Session type can be test, adept, or soartech. '
                        'If you want to run through all available scenarios without repeating do not use the scenario_count argument')
    parser.add_argument('--eval', action='store_true', default=False, help=\
                        'Run an evaluation session. '
                        'Supercedes --session and is the default if nothing is specified. '
                        'Implies --db.')

    args = parser.parse_args()
    use_db = "_db_" if args.db else ""
    if args.session:
        if args.session[0] not in ['soartech', 'adept', 'test']:
            parser.error("Invalid session type. It must be one of 'soartech', 'adept', or 'test'.")
        else:
            session_type = args.session[0]
    else:
        session_type = 'eval'
    scenario_count = int(args.session[1]) if len(args.session) > 1 else 0
    if args.eval:
        session_type = 'eval'
    runner = ITMHumanScenarioRunner(use_db, session_type, scenario_count)
    runner.run()

if __name__ == "__main__":
    main()
