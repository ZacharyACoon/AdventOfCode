import unittest
from aoc2021.common import puzzle_input
import math


def parse(data):
    l = len(data)
    width = 0
    heights = []
    for i, c in enumerate(data):
        if c != "\n":
            width += 1
            heights.append(int(c))
        else:
            width = 0

    return heights, width


def is_low_point(heights, width, p):
    w = width
    l = len(heights)
    adjacent_points = p-w, p-1, p+1, p+w
    adjacent_points = filter(lambda v: 0 <= v < l, adjacent_points)
    center_height = heights[p]
    for adjacent_point in adjacent_points:
        adjacent_point_height = heights[adjacent_point]
        if adjacent_point_height <= center_height:
            return False
    else:
        return True


def part1(data):
    heights, width = parse(data)
    risk_level = 0
    for point in range(len(heights)):
        if is_low_point(heights, width, point):
            risk_level += heights[point] + 1
    return risk_level


def part2(data):
    pass


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        example = self.examples[0]
        print(example)
        self.assertEqual(15, part1(example))

    # def test2_part2_example1(self):
    #     example = self.examples[0]
    #     self.assertEqual(0, part2(example))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
