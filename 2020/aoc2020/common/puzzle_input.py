from sys import argv
from pathlib import Path


def from_file(file):
    with open(file, 'r') as f:
        return f.read()


def from_arg_file():
    assert len(argv) > 1
    file = Path(argv[1])
    return from_file(file)


def from_example(path, n):
    file = Path(path).parent / f"example_input{n}.txt"
    return from_file(file)
