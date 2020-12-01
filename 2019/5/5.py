import unittest
from common.logging import root_logger
from aoc_common import puzzle_input
from aoc_common import intcode_computer
from aoc_common.intcode_computer.computer_test import ComputerTest
import logging


if __name__ == '__main__':
    intcode_computer_logger = logging.getLogger("IntcodeComputer")
    intcode_computer_logger.setLevel(logging.INFO)

    unittest.main(exit=False, verbosity=0)

    initial_memory = intcode_computer.util.parse_memory_string(puzzle_input)
    quit()
    # part 1
    computer = intcode_computer.IntcodeComputer(initial_memory)
    computer.run()
    computer.input(1)
    try:
        while True:
            try:
                computer.process()
            except intcode_computer.exceptions.WaitingForOutput:
                answer = computer.output()
                root_logger.info(f"Part One = {answer}")
    except intcode_computer.exceptions.Finished:
        pass

    # part 2
    computer = intcode_computer.IntcodeComputer(initial_memory)
    computer.run()
    computer.input(5)
    try:
        computer.process()
    except intcode_computer.exceptions.WaitingForOutput:
        answer = computer.output()
        root_logger.info(f"Part Two = {answer}")
