from pathlib import Path

USER_HOME = Path.home()
# PROJECTS_DIR = USER_HOME / "Projects"
# PROJECT_NAME = "adndiscord"
PROJECT_ROOT = Path.cwd()
ADMBOT = 'admbot'
LOG_FILE = 'log.txt'

PATHS = {
    'PROJECT_ROOT': PROJECT_ROOT,
    'LOG_FILE': Path(PROJECT_ROOT / LOG_FILE).resolve(),
    'ADMBOT': PROJECT_ROOT / ADMBOT,
    'COGS_DIR': PROJECT_ROOT / ADMBOT / 'cogs',
}


PATHS_TO_TOUCH = [
    PATHS['LOG_FILE'],
]
