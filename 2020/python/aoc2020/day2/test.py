from aoc2020.common import testing
from aoc2020.common import puzzle_input
from . import solution


example_input1 = puzzle_input.from_example(__file__, 1)


class Test(testing.TimedTestCase):
    def test1_find_product_with_2(self):
        self.assertEqual(solution.part1(example_input1), 2)

    def test2_find_product_with_3(self):
        self.assertEqual(solution.part2(example_input1), 1)
