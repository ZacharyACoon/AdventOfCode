from aoc2020.common import testing
from aoc2020.common import puzzle_input
from . import solution


examples = puzzle_input.from_examples(__file__)


class Test(testing.TimedTestCase):
    def test_part1_example1(self):
        self.assertEqual(6, solution.part1(examples[0]))

    def test_part1_example2(self):
        self.assertEqual(11, solution.part1(examples[1]))

    def test_part2_example1(self):
        self.assertEqual(6, solution.part2(examples[1]))
