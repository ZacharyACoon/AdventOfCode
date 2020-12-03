from aoc2020.common import puzzle_input
from aoc2020.common.utils import type_per_line
from . import solution


if __name__ == "__main__":
    input = type_per_line(puzzle_input.from_arg_file(), int)

    print("Part day1:", solution.find_product_of_sum_components(input, 2, 2020))
    print("Part day2:", solution.find_product_of_sum_components(input, 3, 2020))
