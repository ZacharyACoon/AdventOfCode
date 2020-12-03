from aoc2020.common import testing
from aoc2020.common import puzzle_input
from . import solution
import math


example_input1 = puzzle_input.from_example(__file__, 1).splitlines()


class Test(testing.TimedTestCase):
    def test1_test_slope_example1(self):
        self.assertEqual(7, solution.measure_slope(example_input1, 3, 1))

    def test2_test_multiple_slopes(self):
        a = solution.measure_slopes(example_input1, solution.given_slopes)
        self.assertEqual(336, math.prod(a))
