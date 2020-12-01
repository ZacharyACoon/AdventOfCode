import unittest
from aoc_common import puzzle_input, example_input
from aoc_common import intcode_computer
from aoc_common.intcode_computer.computer_test import ComputerTest
from common.logging import root_logger
import logging


def parse_memory_string(s):
    return list(map(int, s))







if __name__ == '__main__':
    intcode_computer_logger = logging.getLogger("IntcodeComputer")
    intcode_computer_logger.setLevel(logging.INFO)
