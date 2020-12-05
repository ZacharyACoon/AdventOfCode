import math


given_slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


def measure_slope(slope_map, xi, yi):
    x = 0
    y = 0
    yl = len(slope_map) - 1
    trees = 0
    while y < yl:
        x += xi
        y += yi
        if slope_map[y][x % len(slope_map[y])] == "#":
            trees += 1
    return trees


def measure_slopes(slope_map, slopes):
    for slope in slopes:
        a = measure_slope(slope_map, *slope)
        yield a


def part1(input):
    input = input.splitlines()
    return measure_slope(input, 3, 1)


def part2(input):
    input = input.splitlines()
    return math.prod(measure_slopes(input, given_slopes))


if __name__ == "__main__":
    from aoc2020.common import puzzle_input
    input = puzzle_input.from_arg_file()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
