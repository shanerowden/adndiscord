from adndiscord.pathconf import PATHS

def check_paths(paths: list = PATHS):
    """
    Given a list of Path objects, will check every path for existence and return first path obj not found
    or False if there is no problem with pathing. uses from adndiscord.pathconf.PATHS by default.
    """
    try:
        for path in paths.values():
            if not path.exists():
                log(f'DOES NOT EXIST: {path}')
                return path
        else:
            return False
    except (FileNotFoundError, PermissionError) as e:
        log(e)
        
        
def terminate(msg: str, code: int = 1):
    """
    Terminate application with exit code and message to stdout
    """
    print(f"TERMINATING WITH {code}: {msg}")
    exit(code)
    
def log(msg, level="debug"):
    from logging import debug as log_d
    from logging import info as log_i
    from logging import debug as log_w

    print(f"Logging {level.upper()}: {msg}")
    if level == "debug":
        log_d(msg)
    elif level == "warning":
        log_w(msg)
    elif level == "info":
        log_i(msg)
    else:
        log_i(f"LOG LEVEL ERROR: {msg}")
