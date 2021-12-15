from sys import argv
from pathlib import Path
import glob
# from aoc2020.common.cli import args


def from_file(file):
    with open(file, 'r') as f:
        return f.read().strip()


def from_arg_file():
    assert len(argv) > 1
    file = Path(argv[1])
    return from_file(file)


def from_example(path: str or Path, n: int):
    """
    Reads a specific example file from directory.
    :param path:
    :param n:
    :return:
    """
    path = Path(path)
    if path.is_file():
        path = path.parent

    path = path / f"example_input{n}.txt"
    return from_file(path)


def from_examples(path: str or Path):
    """
    Reads all examples into a list, following a glob.
    :param path:
    :return:
    """
    path = Path(path)
    if path.is_file():
        path = path.parent

    path = f"{path}/example_input*"
    return [from_file(example) for example in glob.glob(path)]
