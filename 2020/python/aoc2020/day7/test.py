from aoc2020.common import testing
from aoc2020.common import puzzle_input
from . import solution


examples = puzzle_input.from_examples(__file__)  # list of stripped str


class Test(testing.TimedTestCase):
    def test1_template(self):
        self.assertEqual(4, solution.part1(examples[0]))

    def test2_template(self):
        self.assertEqual(126, solution.part2(examples[1]))
