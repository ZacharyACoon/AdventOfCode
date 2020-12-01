import unittest
from . import IntcodeComputer
from . import exceptions


class ComputerTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.computer = IntcodeComputer()

    def _run_to_exception(self, memory=None, exception=exceptions.Finished):
        if memory:
            self.computer = IntcodeComputer(memory)
        self.assertRaises(exception, self.computer.process)

    def _run_to_result(self, memory=None, result_memory=None, exception=exceptions.Finished):
        self._run_to_exception(memory, exception)
        self.computer.memory.memory.values()
        m = list(self.computer.memory.memory.values())[:len(result_memory)]
        self.assertListEqual(m, result_memory)

    def _run_to_input(self, memory=None, input=None):
        self._run_to_exception(memory, exceptions.WaitingForInput)
        if input is not None:
            self.computer.input(input)

    def _run_to_output(self, memory=None, expected_output=None):
        self._run_to_exception(memory, exceptions.WaitingForOutput)
        output = self.computer.output()
        if expected_output is not None:
            self.assertEqual(expected_output, output)
        return output

    def _run_input_output(self, memory=None, input=None, expected_output=None):
        self._run_to_input(memory, input)
        self._run_to_output(None, expected_output)

    def test_runout(self):
        self._run_to_exception(exception=exceptions.RanOut)

    def test_finish(self):
        self._run_to_exception([99])

    def test_day2_example1_addition(self):
        memory = [1, 0, 0, 0, 99]
        result_memory = [2, 0, 0, 0, 99]
        self._run_to_result(memory, result_memory)

    def test_day2_example2_multiplication(self):
        memory = [2, 3, 0, 3, 99]
        result_memory = [2, 3, 0, 6, 99]
        self._run_to_result(memory, result_memory)

    def test_day2_example3_multiplication2(self):
        memory = [2, 4, 4, 5, 99, 0]
        result_memory = [2, 4, 4, 5, 99, 9801]
        self._run_to_result(memory, result_memory)

    def test_day2_example4(self):
        memory = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        result_memory = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        self._run_to_result(memory, result_memory)

    def test_day5_part1_example1(self):
        memory = [1002, 4, 3, 4, 33]
        self._run_to_exception(memory)

    def test_day5_part1_example2(self):
        memory = [1101, 100, -1, 4, 0]
        self._run_to_exception(memory)

    def test_day5_part2_example1_equal_to(self):
        memory = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        self._run_input_output(memory, 8, 1)
        self._run_input_output(memory, 1, 0)

    def test_day5_part2_example2_less_than(self):
        memory = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        self._run_input_output(memory, 1, 1)
        self._run_input_output(memory, 8, 0)

    def test_day5_part2_example3_equal_to(self):
        memory = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        self._run_input_output(memory, 8, 1)
        self._run_input_output(memory, 1, 0)

    def test_day5_part2_example4_less_than(self):
        memory = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        self._run_input_output(memory, 1, 1)
        self._run_input_output(memory, 8, 0)

    def test_day5_part2_example5_jump_test(self):
        memory = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        self._run_input_output(memory, 0, 0)
        self._run_input_output(memory, 1, 1)

    def test_day5_part2_example6_jump_test(self):
        memory = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        self._run_input_output(memory, 0, 0)
        self._run_input_output(memory, 1, 1)

    def test_day9_part1_example1_copy_of_input(self):
        memory = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        self.computer = IntcodeComputer(memory)
        for m in memory:
            self._run_to_output(expected_output=m)
        self._run_to_exception()

    def test_day9_part1_example2_output_16digit_number(self):
        memory = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
        output = self._run_to_output(memory)
        self.assertEqual(len(str(output)), 16)
        self._run_to_exception()

    def test_day9_part1_example3_output_middle_number(self):
        memory = [104, 1125899906842624, 99]
        self._run_to_output(memory, expected_output=1125899906842624)
