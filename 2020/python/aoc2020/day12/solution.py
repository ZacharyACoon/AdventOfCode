import unittest
from aoc2020.common import puzzle_input
from aoc2020.common.testing import TimedTestCase
from aoc2020.common.solution import Solution
import re
import math
from aoc2020.common.cli import args


def parse_instructions(input):
    for match in re.finditer(r"([A-zA-Z]+)(\d+)", input):
        instruction, distance = match.groups()
        yield instruction, int(distance)


compass = {
    "N": 0,
    "E": 90,
    "S": 180,
    "W": 270,
    360: "N",
}
compass.update({v: k for k, v, in compass.items()})


rotation = {
    0: lambda wx, wy: (wx, wy),
    90: lambda wx, wy: (wy, -wx),
    180: lambda wx, wy: (-wx, -wy),
    270: lambda wx, wy: (-wy, wx),
}


def rpo(wx, wy, deg):
    r = math.radians(deg)
    nwx = math.cos(r) * wx - math.sin(r) * wy
    nwy = math.sin(r) * wx + math.cos(r) * wy
    return int(nwx), int(nwy)


class Solution(Solution):
    def part1(self, input):
        f = compass["E"]
        sx = x = 0
        sy = y = 0
        move = {
            "N": lambda v: (x, y+v, f),
            "S": lambda v: (x, y-v, f),
            "E": lambda v: (x-v, y, f),
            "W": lambda v: (x+v, y, f),
            "L": lambda v: (x, y, (f-v) % 360),
            "R": lambda v: (x, y, (f+v) % 360),
        }
        for direction, v in parse_instructions(input):
            self.log.debug(direction, v)
            if direction == "F":
                x, y, f = move[compass[f]](v)
            else:
                x, y, f = move[direction](v)
            self.log.debug(x, y, f)
        return abs(sx - x) + abs(sy - y)

    def part2(self, input):
        # ship, starts, coordinates, facing
        sx = x = 0
        sy = y = 0
        f = compass["E"]
        # waypoint, relative to ship
        wx = 10
        wy = 1

        move = {
            "N": lambda v: (x, y, f, wx, wy+v),
            "S": lambda v: (x, y, f, wx, wy-v),
            "E": lambda v: (x, y, f, wx+v, wy),
            "W": lambda v: (x, y, f, wx-v, wy),
            "L": lambda v: (x, y, f, *rotation[360-v%360](wx, wy)),
            "R": lambda v: (x, y, f, *rotation[v%360](wx, wy)),
            # "L": lambda v: (x, y, f, *rpo(wx, wy, v)),
            # "R": lambda v: (x, y, f, *rpo(wx, wy, -v)),
            "F": lambda v: (x+(wx*v), y+(wy*v), f, wx, wy),
        }

        for direction, v in parse_instructions(input):
            self.log.debug(direction, v)
            x, y, f, wx, wy = move[direction](v)
            self.log.debug(x, y, f, wx, wy)
        return abs(sx - x) + abs(sy - y)


class Test1(TimedTestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        self.assertEqual(25, Solution().part1(self.examples[0]))

    def test2_part2_example1(self):
        self.assertEqual(286, Solution().part2(self.examples[0]))


if __name__ == "__main__":
    unittest.main(argv=[__file__], verbosity=0, exit=False)
    print(args)
    input = puzzle_input.from_arg_file()

    solution = Solution()
    print("Part 1:", solution.part1(input))
    print("Part 2:", solution.part2(input))
