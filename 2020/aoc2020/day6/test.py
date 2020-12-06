from aoc2020.common import testing
from aoc2020.common import puzzle_input
from . import solution


example_input1 = puzzle_input.from_example(__file__, 1)
example_input2 = puzzle_input.from_example(__file__, 2)


class Test(testing.TimedTestCase):
    def test_part1_example1(self):
        self.assertEqual(6, solution.part1(example_input1))

    def test_part1_example2(self):
        self.assertEqual(11, solution.part1(example_input2))

    def test_part2_example1(self):
        self.assertEqual(6, solution.part2(example_input2))
