import unittest
from aoc2021.common import puzzle_input


def parse(data):
    dots = set()
    max_x = 0
    max_y = 0
    lines = data.strip().splitlines()
    for i, line in enumerate(lines):
        if line == "":
            break
        x, y = tuple(map(int, line.split(",")))
        max_x = max(max_x, x+1)
        max_y = max(max_y, y+1)
        xy = x, y
        dots.add(xy)

    bounds = max_x, max_y

    folds = []
    for line in lines[i+1:]:
        line = line[11:]
        axis, position = line.split("=")
        position = int(position)
        folds.append((axis, position))

    return dots, bounds, folds


def display(dots, bounds):
    width, height = bounds
    lines = ""
    for y in range(height):
        for x in range(width):
            xy = x, y
            if xy in dots:
                lines += "#"
            else:
                lines += "."
        lines += "\n"
    print(lines)


def fold(dots, bounds, folds, max_folds):
    old_dots = dots

    previous_dots = old_dots.copy()
    for axis, position in folds[:max_folds]:
        dots = set()
        max_x = 0
        max_y = 0
        for x, y in previous_dots:
            if axis == "x":
                if x > position:
                    x = position - (x - position)
            elif axis == "y":
                if y > position:
                    y = position - (y - position)
            xy = x, y
            max_x = max(max_x, x+1)
            max_y = max(max_y, y+1)
            dots.add(xy)
        previous_dots = dots.copy()

    new_bounds = max_x, max_y
    return dots, new_bounds


def part1(data, max_folds=1):
    dots, bounds, folds = parse(data)
    # display(dots, bounds)
    dots, bounds = fold(dots, bounds, folds, max_folds)
    display(dots, bounds)

    return len(dots)


def part2(data):
    part1(data, max_folds=999)


class Test(unittest.TestCase):

    def test1_part1_example1_one_fold(self):
        example = puzzle_input.from_example(__file__, 1)
        self.assertEqual(17, part1(example, 1))

    def test2_part1_example1_two_folds(self):
        example = puzzle_input.from_example(__file__, 1)
        self.assertEqual(16, part1(example, 2))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    # print("Part 1:", part1(data))
    print("Part 2:", part2(data))

"""
###..####.####...##.#..#.###..####.####
#..#....#.#.......#.#..#.#..#.#.......#
#..#...#..###.....#.####.#..#.###....#.
###...#...#.......#.#..#.###..#.....#..
#....#....#....#..#.#..#.#.#..#....#...
#....####.#.....##..#..#.#..#.#....####
"""