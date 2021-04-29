import unittest
from aoc_common import puzzle_input
from aoc_common import intcode_computer
from aoc_common.intcode_computer.computer_test import ComputerTest
from common.logging import root_logger
import logging


if __name__ == '__main__':
    intcode_computer_logger = logging.getLogger("IntcodeComputer")
    intcode_computer_logger.setLevel(logging.INFO)

    unittest.main(exit=False, verbosity=0)

    initial_memory = intcode_computer.util.parse_memory_string(puzzle_input)

    # part 1
    root_logger.info("Part One")
    computer = intcode_computer.IntcodeComputer(initial_memory)
    computer.run()
    computer.input(1) # test mode
    while True:
        try:
            computer.process()
        except computer.exceptions.WaitingForOutput:
            root_logger.info(computer.output())
        except computer.exceptions.Finished:
            break

    # part 2
    root_logger.info("Part Two")
    computer = intcode_computer.IntcodeComputer(initial_memory)
    computer.run()
    computer.input(2)  # test mode
    while True:
        try:
            computer.process()
        except computer.exceptions.WaitingForOutput:
            root_logger.info(computer.output())
        except computer.exceptions.Finished:
            break
