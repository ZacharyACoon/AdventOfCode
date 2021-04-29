import unittest
from aoc_common import puzzle_input
from aoc_common import intcode_computer
from aoc_common.intcode_computer.computer_test import ComputerTest
import logging
import itertools


def amplifiers(program, phase_sequence):
    amps = []
    last_output = 0
    phases_entered = False
    try:
        while True:
            for i in range(len(phase_sequence)):
                if not phases_entered:
                    amps.append(intcode_computer.IntcodeComputer(program))
                    try:
                        amps[i].process()
                    except intcode_computer.exceptions.WaitingForInput:
                        amps[i].input(phase_sequence[i])

                try:
                    amps[i].process()
                except intcode_computer.exceptions.WaitingForInput:
                    amps[i].input(last_output)

                try:
                    amps[i].process()
                except intcode_computer.exceptions.WaitingForOutput:
                    last_output = amps[i].output(override_exception=True)
            phases_entered = True
    except intcode_computer.exceptions.Finished:
        return last_output


def amplifier_permutations_feedback_max(program, sequence):
    return max(amplifiers(program, permutation) for permutation in itertools.permutations(sequence))


class AmplifierControllerSoftwareTests(ComputerTest):
    def test_amplifier_part1_example1(self):
        example1_program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        example1_sequence = [4,3,2,1,0]
        m = amplifier_permutations_feedback_max(example1_program, example1_sequence)
        self.assertEqual(m, 43210)

    def test_amplifier_part1_example2(self):
        example2_program = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
        example2_sequence = [0,1,2,3,4]
        m = amplifier_permutations_feedback_max(example2_program, example2_sequence)
        self.assertEqual(m, 54321)

    def test_amplifier_part1_example3(self):
        example3_program = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        example3_sequence = [1,0,4,3,2]
        m = amplifier_permutations_feedback_max(example3_program, example3_sequence)
        self.assertEqual(m, 65210)


if __name__ == '__main__':
    intcode_computer_logger = logging.getLogger("IntcodeComputer")
    intcode_computer_logger.setLevel(logging.INFO)
    logging.getLogger().setLevel(logging.INFO)

    unittest.main(exit=False, verbosity=0)

    amplifier_controller_software = puzzle_input
    initial_memory = intcode_computer.util.parse_memory_string(puzzle_input)

    # part 1
    m = amplifier_permutations_feedback_max(initial_memory, [0,1,2,3,4])
    logging.getLogger().error(f"Part One = {m}")

    m = amplifier_permutations_feedback_max(initial_memory, [5,6,7,8,9])
    logging.getLogger().warning(f"Part Two = {m}")
