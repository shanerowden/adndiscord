from adndiscord.pathconf import PATHS, PATHS_TO_TOUCH
from adndiscord.utils import check_paths, terminate, log
from adndiscord.attributes import AbilityScoreGen
from logging import basicConfig, DEBUG, INFO, WARNING

def init():
    # Initialize Paths
    for path in PATHS_TO_TOUCH:
        path.touch()
    bad_path = check_paths()
    if bad_path:
        terminate(f"Path does not exist. {bad_path}")
    
    # Initialize Logging
    basicConfig(filename=PATHS['LOG_FILE'], level=DEBUG)
    
def main():
    return AbilityScoreGen()


if __name__ == "__main__":
    init()
    test = main()
else:
    init()

