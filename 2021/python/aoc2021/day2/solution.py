import unittest
from aoc2021.common import puzzle_input


def part1(instructions):
    x = 0
    y = 0
    for instruction in instructions:
        direction, value = instruction.split(" ")
        value = int(value)
        if direction == "up":
            x -= value
        elif direction == "down":
            x += value
        elif direction == "forward":
            y += value
        elif direction == "backward":
            y -= value

    return x * y


def part2(instructions):
    x = 0
    y = 0
    aim = 0
    for instruction in instructions:
        direction, value = instruction.split(" ")
        value = int(value)
        if direction == "up":
            aim -= value
        elif direction == "down":
            aim += value
        elif direction == "forward":
            x += value
            y += aim * value
        elif direction == "backward":
            x -= value
            y -= aim * value

    return x * y


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        example = self.examples[0].strip().split("\n")
        self.assertEqual(150, part1(example))

    def test2_part2_example1(self):
        example = self.examples[0].strip().split("\n")
        self.assertEqual(900, part2(example))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file().strip().split("\n")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
