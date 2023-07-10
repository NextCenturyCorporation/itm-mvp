import argparse
from itm import ADMScenarioRunner

def main():
    parser = argparse.ArgumentParser(description='Runs ADM scenarios.')
    parser.add_argument('--db', action='store_true', default=False, help=\
                        'Put the scene in the MongoDB and save a json output file locally inside itm_server/itm_mvp_local_output/')
    parser.add_argument('-r', action='store_true', default=False, help='Use a randomly generated scene')
    parser.add_argument('-y', action='store_true', default=False, help='Use a premade yaml scene')
    parser.add_argument('--session', nargs='*', default=[], metavar=('session_type', 'scenario_count'), help=\
                        'Specify session type and scenario count. '
                        'Session type can be test, adept, or soartech. '
                        'If you want to run through all available scenarios without repeating do not use the scenario_count argument')
    parser.add_argument('--eval', action='store_true', default=False, help=\
                        'Run an eval session')

    args = parser.parse_args()

    scene_type = "_random_" if args.r else ""
    use_db = "_db_" if args.db else ""
    session_type = args.session[0] if args.session else ""
    scenario_count = int(args.session[1]) if len(args.session) > 1 else 0

    adm = ADMScenarioRunner(use_db, scene_type, session_type, scenario_count, args.eval)
    adm.run()

if __name__ == "__main__":
    main()
