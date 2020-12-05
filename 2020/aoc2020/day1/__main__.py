from aoc2020.common import puzzle_input
from . import solution


if __name__ == "__main__":
    input = puzzle_input.from_arg_file()

    print("Part 1:", solution.solve1(input))
    print("Part 2:", solution.solve2(input))
