import os
from pathlib import Path


def make_dir(directory: Path) -> Path:
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def make_file(directory: Path, filename: str):
    try:
        file_path = Path(directory, filename)
        with open(file_path, "w"):
            pass  # Create empty file
    except OSError as e:
        raise OSError(f"Error when creating the file '{file_path}': {e}")


def get_data_dir():
    cur_dir = Path(__file__).resolve().parent.parent
    data_dir: Path = make_dir(cur_dir.joinpath("data"))
    return data_dir


def get_logs_dir():
    data_dir = get_data_dir()
    logs_dir: Path = make_dir(data_dir.joinpath("logs"))
    return logs_dir
