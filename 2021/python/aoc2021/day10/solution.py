import unittest
from aoc2021.common import puzzle_input


def part1(data):
    pass


def part2(data):
    pass


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        example = self.examples[0]
        self.assertEqual(0, part1(example))

    def test2_part2_example1(self):
        example = self.examples[0]
        self.assertEqual(0, part2(example))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
