from aoc2020.common import puzzle_input
from . import solution
import math


if __name__ == "__main__":
    input = puzzle_input.from_arg_file().splitlines()

    print("Part 1:", solution.measure_slope(input, 3, 1))
    print("Part 2:", math.prod(solution.measure_slopes(input, solution.given_slopes)))
