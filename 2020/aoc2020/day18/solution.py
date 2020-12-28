import unittest
from aoc2020.common import puzzle_input
import re
import math


def parse(data):
    regex = r"(\d+|\+|\-|\*|\(|\))"
    components = re.findall(regex, data)
    components = [int(value) if value.isnumeric() else value for value in components ]
    return components


operators = {
    "+": sum,
    "-": lambda vs: -sum(vs),
    "*": math.prod,
}


def solve(components):




def part1(data):
    data = parse(data)
    print(data)
    recursively_solve(data)
    print(data)


def part2(data):
    pass


class Test(unittest.TestCase):
    examples = [
        "1 + 1",
        "1 * 2",
        "2 * 3 + (4 * 5)",
        "5 + (8 * 3 + 9 + 3 * 4 * 3)",
        "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
        "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
    ]

    def test1_part1_example1(self):
        self.assertEqual(2, part1(self.examples[0]))
        # self.assertEqual(26, part1(self.examples[2]))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    # print("Part 1:", part1(data))
    # print("Part 2:", part2(data))
