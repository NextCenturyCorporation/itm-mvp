import argparse
from itm import ADMScenarioRunner

def main():
    parser = argparse.ArgumentParser(description='Runs ADM scenarios.')
    parser.add_argument('--db', action='store_true', help=\
                        'Put the scene in the MongoDB and save a json output file locally inside itm_server/itm_mvp_local_output/')
    parser.add_argument('-r', action='store_true', help='Use a randomly generated scene')
    parser.add_argument('-y', action='store_true', help='Use a premade yaml scene')
    parser.add_argument('--session', nargs=2, metavar=('session_type', 'scenario_count'), help=\
                        'Specify session type and scenario count. '
                        'If you want to run through all available scenarios without repeating any use scenario count -1')

    args = parser.parse_args()

    scene_type = "_random_" if args.r else ""
    use_db = "_db_" if args.db else ""
    session_type = args.session[0] if args.session else ""
    scenario_count = int(args.session[1]) if args.session else 1

    adm = ADMScenarioRunner(use_db, scene_type, session_type, scenario_count)
    adm.run()

if __name__ == "__main__":
    main()
