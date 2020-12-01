import unittest
from common.logging import log
from aoc_common import puzzle_input
from aoc_common import intcode_computer
from aoc_common.intcode_computer.computer_test import ComputerTest
import logging


if __name__ == '__main__':

    intcode_computer_logger = logging.getLogger("IntcodeComputer")
    intcode_computer_logger.setLevel(logging.INFO)

    unittest.main(exit=False, verbosity=0)

    computer = intcode_computer.IntcodeComputer()
    initial_memory = intcode_computer.util.parse_memory_string(puzzle_input)

    # initialize computer
    computer.memory.reset()
    computer.memory.load(initial_memory)
    computer.memory[1] = 12
    computer.memory[2] = 2

    # run
    computer.run()
    answer = computer.memory[0]
    log.info(f"Part One = {answer}")

    for noun in range(99):
        for verb in range(99):
            computer.memory.reset()
            computer.memory.load(initial_memory)
            computer.memory[1] = noun
            computer.memory[2] = verb
            computer.run()
            if computer.memory[0] == 19690720:
                answer = 100 * noun + verb
                log.info(f"Part Two = {answer}")
                break
        if computer.memory[0] == 19690720:
            break
    else:
        log.fatal("Wut.")
