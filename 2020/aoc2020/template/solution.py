import unittest
from aoc2020.common import puzzle_input
from aoc2020.common.testing import TimedTestCase
from aoc2020.common.solution import Solution


class Solution(Solution):
    def part1(self, input):
        pass

    def part2(self, input):
        pass


class Test(TimedTestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        # self.assertEqual(0, solution.part1(self.examples[0]))
        pass


if __name__ == "__main__":
    unittest.main()
    input = puzzle_input.from_arg_file()

    solution = Solution()
    print("Part 1:", solution.part1(input))
    print("Part 2:", solution.part2(input))
