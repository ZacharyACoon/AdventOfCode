import unittest
from aoc2020.common import puzzle_input


def part1(data):
    pass


def part2(data):
    pass


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        # self.assertEqual(0, solution.part1(self.examples[0]))
        pass


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
