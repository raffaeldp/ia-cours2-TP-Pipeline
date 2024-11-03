import os


def ensure_folder_exists(path: str):
    """
    Check if the current path exist and create a folder if not.
    Args:
        path (str): path of the folder that should be checked.
    """
    if not os.path.exists(path):
        os.makedirs(path)
