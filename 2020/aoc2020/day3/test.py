from aoc2020.common import testing
from aoc2020.common import puzzle_input
from . import solution


example_input1 = puzzle_input.from_example(__file__, 1).splitlines()


class Test(testing.TimedTestCase):
    def test1_test_slope_example1(self):
        self.assertEqual(7, solution.part1(example_input1))

    def test2_test_multiple_slopes(self):
        self.assertEqual(336, solution.part2(example_input1))
