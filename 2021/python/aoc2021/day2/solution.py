import unittest
from aoc2021.common import puzzle_input


# ∑
def sigma(values):
    v = 1
    for value in values:
        v *= value
    return v


def part1(instructions):
    # x, y
    coordinates = [0, 0]
    direction_map = {
        "forward": (0, 1),
        "backward": (0, -1),
        "up": (1, -1),
        "down": (1, 1),
    }
    for instruction in instructions:
        direction, value = instruction.split(" ")
        value = int(value)
        coordinate, multiplier = direction_map[direction]
        coordinates[coordinate] += multiplier * value
        # print(direction, value, coordinates)
    return sigma(coordinates)


class Sub:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0

    def __repr__(self):
        return f"Sub({self.x}, {self.y}, {self.aim})"

    def up(self, v):
        self.aim -= v

    def down(self, v):
        self.aim += v

    def forward(self, v):
        self.x += v
        self.y += self.aim * v

    def backward(self, v):
        self.x -= v
        self.y -= self.aim * v


def part2(instructions):
    s = Sub()
    for instruction in instructions:
        direction, value = instruction.split(" ")
        value = int(value)
        if hasattr(s, direction):
            getattr(s, direction)(value)
        print(direction, value, s)
    return s.x * s.y


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
