import sys
from pathlib import Path

import yaml


def mkdir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def load_param(path: Path):
    with open(path, encoding="utf-8") as reader:
        return yaml.safe_load(reader)


def dir_fullpath(param: dict, camera: str) -> Path:
    return (
        Path(param["place"])
        / f'{param["year"]}年'
        / f'{camera}_{param["date"]}_{param["event"]}'
    )
