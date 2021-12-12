import unittest
from aoc2021.common import puzzle_input
import math
from os import system, name


def parse(data):
    heights = dict()
    lines = data.strip().splitlines()
    grid_height = len(lines)
    for y, line in enumerate(lines):
        width = len(line)
        for x, c in enumerate(line):
            height = int(c)
            heights[(x, y)] = height
    return heights, width, grid_height


def is_low_point(heights, p):
    x, y = p
    center_height = heights[p]
    adjacent_points = (x, y-1), (x+1, y), (x, y+1), (x-1, y)
    for adjacent_point in adjacent_points:
        height = heights.get(adjacent_point)
        if height is not None and height <= center_height:
            return False
    return True


def display(heights, basin, width, height, p=None):
    for y in range(height):
        line = ""
        for x in range(width):
            if p == (x, y):
                line += ">"
            elif (x, y) in basin:
                line += "("
            else:
                line += " "

            line += f"{heights[(x, y)]}"

            if p == (x,y):
                line += "<"
            elif (x, y) in basin:
                line += ")"
            else:
                line += " "
        print(line)

    # windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    print()


def identify_low_points(heights):
    low_points = set()
    for p in heights:
        if is_low_point(heights, p):
            low_points.add(p)
    return low_points


def part1(data):
    heights, width, height = parse(data)
    low_points = identify_low_points(heights)
    risk_levels = [heights[low_point]+1 for low_point in low_points]
    return sum(risk_levels)


def identify_basin(heights, width, height, p, basin=None, depth=0):
    if basin is None:
        basin = set()

    display(heights, basin, width, height, p)
    basin.add(p)

    # print(f"{depth*'  '}path={basin}, {p}, {heights.get(p)}")

    x, y = p
    adjacent_points = (x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)
    for adjacent_point in adjacent_points:
        # print(f"{depth*'  '}{adjacent_point}")
        adjacent_point_height = heights.get(adjacent_point, 9)
        if adjacent_point not in basin and adjacent_point_height != 9:
            identify_basin(heights, width, height, adjacent_point, basin, depth+1)

    return basin


def identify_basins(heights, width, height, low_points):
    basin_points = set()
    basins = set()
    for p in low_points:
        if p not in basin_points:
            # print(f"low point {p}, {heights[p]}")
            basin = identify_basin(heights, width, height, p)
            basins.add(frozenset(basin))
            basin_points.update(basin)
    return basins


def part2(data):
    heights, width, height = parse(data)
    low_points = identify_low_points(heights)
    basins = identify_basins(heights, width, height, low_points)
    largest_three = sorted(list(map(len, basins)))[-3:]
    return math.prod(largest_three)


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        example = self.examples[0]
        self.assertEqual(15, part1(example))

    def test2_part2_example1(self):
        example = self.examples[0]
        self.assertEqual(1134, part2(example))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
