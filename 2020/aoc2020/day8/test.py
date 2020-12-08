from aoc2020.common import testing
from aoc2020.common import puzzle_input
from . import solution


examples = puzzle_input.from_examples(__file__)  # list of stripped str


class Test(testing.TimedTestCase):
    # def test1_part1_example1(self):
    #     self.assertEqual(5, solution.part1(examples[0].splitlines()))

    def test1_part2_example1(self):
        self.assertEqual(8, solution.part2(examples[0].splitlines()))
