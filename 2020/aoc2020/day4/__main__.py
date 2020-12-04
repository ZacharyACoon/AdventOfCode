from aoc2020.common import puzzle_input
from . import solution
from itertools import tee


if __name__ == "__main__":
    input = puzzle_input.from_arg_file()
    entries1, entries2 = tee(solution.partition_entries(input))

    print("Part 1:", sum(map(solution.validate_entry1, entries1)))
    print("Part 2:", sum(map(solution.validate_entry2, entries2)))
