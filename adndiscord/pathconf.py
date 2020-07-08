from pathlib import Path

USER_HOME = Path.home()
# PROJECTS_DIR = USER_HOME / "Projects"
# PROJECT_NAME = "adndiscord"
PROJECT_ROOT = Path.cwd()

PATHS = {
    'PROJECT_ROOT': PROJECT_ROOT,
    'LOG_FILE': Path(PROJECT_ROOT / "log.txt").resolve()
}


PATHS_TO_TOUCH = [
    PATHS['LOG_FILE'],
]
