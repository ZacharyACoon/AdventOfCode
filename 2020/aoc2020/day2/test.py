from aoc2020.common import testing
from aoc2020.common.utils import type_per_line
from aoc2020.common import puzzle_input
from . import solution


input = type_per_line(puzzle_input.from_example(__file__, 1), solution.parse)


class Test(testing.TimedTestCase):
    def test1_find_product_with_2(self):
        a = solution.count_valid(solution.validate_password1, input)
        self.assertEqual(a, 2)

    def test2_find_product_with_3(self):
        a = solution.count_valid(solution.validate_password2, input)
        self.assertEqual(a, 1)
