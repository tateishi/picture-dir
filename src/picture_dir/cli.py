from fire import Fire

from . import core


def hello():
    print("Hello, World.")


def picture_dir(path: str, debug: bool = False) -> None:
    param = core.load_param(path)
    if debug:
        print(param)
    for camera in param["cameras"]:
        directory = core.dir_fullpath(param, camera)
        if debug:
            print(directory)
        core.mkdir(directory)


def main():
    Fire(picture_dir)
