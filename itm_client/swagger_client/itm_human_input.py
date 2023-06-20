import sys
from itm import ITMHumanScenarioRunner

def main():
    if "-h" in sys.argv or "--h" in sys.argv:
        print("Usage:")
        print("  --db   : Put the output in the MongoDB (ensure that the itm_dashboard docker container is running) and save a json output file locally inside itm_server/itm_mvp_local_output/")
        print("  -r    : Use a randomly generate scene")
        print("  -y    : Use a premade yaml scene. This is the default if neither -r or -y is specified")
        return

    scene_type = ""
    if "-r" in sys.argv:
        scene_type = "_random_"
    if "-y" in sys.argv:
        scene_type = ""
    
    use_db = ""
    if "--db" in sys.argv:
        use_db += "_db_"
    
    runner = ITMHumanScenarioRunner(use_db, scene_type)
    runner.run()

if __name__ == "__main__":
    main()