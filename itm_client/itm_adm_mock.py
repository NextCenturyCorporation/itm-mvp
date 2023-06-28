import sys
from itm import ADMScenarioRunner

def main():
    if "-h" in sys.argv or "--h" in sys.argv:
        print("Usage:")
        print("  --db   : Put the scene in the MongoDB (ensure that the itm_dashboard docker container is running) and save a json output file locally inside itm_server/itm_mvp_local_output/")
        print("  -r    : Use a randomly generated scene")
        print("  -y    : Use a premade yaml scene. This is the default if neither -r or -y is specified")
        return
    scene_type = ""
    session_type = ""
    scenario_count = 1
    if "-r" in sys.argv:
        scene_type = "_random_"
    if "-y" in sys.argv:
        scene_type = ""
    
    use_db = ""
    if "--db" in sys.argv:
        use_db += "_db_"

    if "--session" in sys.argv:
        session_arg_index = sys.argv.index("--session")
        session_type = sys.argv[session_arg_index + 1]
        scenario_count = int(sys.argv[session_arg_index + 2])

    
    adm = ADMScenarioRunner(use_db, scene_type, session_type, scenario_count)
    adm.run()

if __name__ == "__main__":
    main()
