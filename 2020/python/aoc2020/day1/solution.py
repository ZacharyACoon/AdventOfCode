from itertools import combinations
import math
from aoc2020.common.utils import type_per_line


# works, but not used
def find_sum_pair(values, summation=2020):
    values_by_need = dict()
    for value in values:
        need = summation - value
        if need in values_by_need:
            values_by_need[need].append(value)
        else:
            values_by_need[need] = [value]
    for value in values:
        if value in values_by_need:
            return value, values_by_need[value][0]


def find_product_of_sum_components(values, components=2, summation=2020):
    for combination in combinations(values, components):
        if sum(combination) == summation:
            return math.prod(combination)


def part1(input):
    input = type_per_line(input, int)
    return find_product_of_sum_components(input, 2, 2020)


def part2(input):
    input = type_per_line(input, int)
    return find_product_of_sum_components(input, 3, 2020)


if __name__ == "__main__":
    from aoc2020.common import puzzle_input
    input = puzzle_input.from_arg_file()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
