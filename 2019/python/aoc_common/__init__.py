from .timed_test_case import TimedTestCase
from .timer import Timer


def get_file_string(path):
    with open(path, 'r') as f:
        return f.read()


def example_input(n):
    return get_file_string(f"example_input_{n}.txt")


puzzle_input = get_file_string('puzzle_input.txt')
