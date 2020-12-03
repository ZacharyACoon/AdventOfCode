from aoc2020.common import puzzle_input
from aoc2020.common.utils import type_per_line
from . import solution


if __name__ == "__main__":
    input = type_per_line(puzzle_input.from_arg_file(), solution.parse)

    print("Part 1:", solution.count_valid(solution.validate_password1, input))
    print("Part 2:", solution.count_valid(solution.validate_password2, input))

