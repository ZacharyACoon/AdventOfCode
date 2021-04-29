from aoc2020.common import testing
from aoc2020.common import puzzle_input
from . import solution


examples = puzzle_input.from_examples(__file__)  # list of stripped str


class Test(testing.TimedTestCase):
    def test_part1_example1(self):
        self.assertEqual(37, solution.part1(examples[0]))

    def test_part2_example1(self):
        self.assertEqual(26, solution.part2(examples[0])[1])

    def test_part2_example1_result(self):
        self.assertEqual(
            examples[1],
            "".join(solution.part2(examples[0])[0])
        )
