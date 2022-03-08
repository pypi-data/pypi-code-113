import os
from pathlib import Path

import yaml

DEFAULT_DBT_PROFILE_PATH = os.path.join(str(Path.home()), ".dbt", "profiles.yml")


def read_yaml(path):
    with open(path, "r", encoding="utf-8") as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def read_dbt_profile(file_path, profile_name="default", target="dev"):
    profiles = read_yaml(file_path)

    if profile_name not in profiles:
        raise ValueError(f"Profile `{profile_name}` not found.")

    profile = profiles[profile_name]

    if target not in profile["outputs"]:
        raise ValueError(f"Target `{target}` not found.")

    return profile["outputs"][target]


def write_file(file_path, text):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)
