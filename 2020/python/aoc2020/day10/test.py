from aoc2020.common import testing
from aoc2020.common import puzzle_input
from . import solution


examples = puzzle_input.from_examples(__file__)  # list of stripped str


class Test(testing.TimedTestCase):
    # def test1_part1_example1_distribution(self):
    #     distribution = solution.get_distribution(list(map(int, examples[0].splitlines())))
    #     self.assertEqual(7, distribution[1])
    #     self.assertEqual(5, distribution[3])

    def test2_part2_example2_count(self):
        self.assertEqual(8, solution.part2(examples[0]))
        self.assertEqual(19208, solution.part2(examples[1]))
