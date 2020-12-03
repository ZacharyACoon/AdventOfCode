from aoc2020.common import testing
from aoc2020.common.utils import type_per_line
from aoc2020.common import puzzle_input
from . import solution


class Test(testing.TimedTestCase):
    example_input1 = type_per_line(puzzle_input.from_example(__file__, 1), int)

    def test1_find_product_with_2(self):
        a = solution.find_product_of_sum_components(self.example_input1, 2, 2020)
        self.assertEqual(a, ((1721, 299), 514579))

    def test2_find_product_with_3(self):
        a = solution.find_product_of_sum_components(self.example_input1, 3, 2020)
        self.assertEqual(a, ((979, 366, 675), 241861950))
