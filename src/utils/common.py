import datetime
import os


def get_current_timestamp() -> int:
    return round(datetime.datetime.now().timestamp())

def create_dir_if_not_exists(path):
    try:
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
    except (FileNotFoundError, PermissionError, OSError) as e:
        raise OSError(f"Failed to create or access the directory for `{path}`: {e}")