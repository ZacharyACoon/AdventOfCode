import unittest
from aoc2021.common import puzzle_input
import numpy as np
import numpy

# 00000000
#        1
#       2
#      4
#     8
#   16
#  32
# 64
#128


def sum_col(arr, col):
    v = 0
    for a in arr:
        v += int(a[col])
    return v


def determine_commons(bins, lean=False):
    bin_count = len(bins)
    bin_length = len(bins[0])
    place_counts = [0] * bin_length
    for p in range(bin_length):
        place_counts[p] = sum_col(bins, p)

    most_commons = 0
    least_commons = 0
    for p in place_counts:
        if p == bin_count // 2:
            if lean:
                most_commons << 1 | 1
                least_commons << 1 | 0
            else:
                most_commons << 1 | 0
                least_commons << 1 | 1
        elif p > bin_count // 2:
            most_commons = most_commons << 1 | 1
            least_commons = least_commons << 1 | 0
        else:
            most_commons = most_commons << 1 | 0
            least_commons = least_commons << 1 | 1
    return most_commons, least_commons


def part1(bins):
    most_commons, least_commons = determine_commons(bins)
    gamma_rate = most_commons
    epsilon_rate = least_commons
    return gamma_rate * epsilon_rate


def part2(bins):
    # truncate bins down using bit criteria to filter bits
    # bit criteria
    #    oxygen_generator_rating: most_common
    #    co2_scrubber_rating:     least_common

    l = len(bins[0])

    orb = bins.copy()
    position = 0
    while len(orb) > 1 and position < l:
        position_sum = sum_col(orb, position)
        most_common = int(position_sum >= len(orb) / 2)
        # print(orb)
        # print(f"col={position}, sum={position_sum}, most_common={most_common}")
        orb = list(filter(lambda b: int(b[position]) == most_common, orb))
        # print(orb)
        # print()
        position += 1
    oxygen_rating = int(orb[0], base=2)
    # print(oxygen_rating)

    crb = bins.copy()
    position = 0
    while len(crb) > 1 and position < l:
        position_sum = sum_col(crb, position)
        least_common = 1 - int(position_sum >= len(crb) / 2)
        # print(crb)
        # print(f"col={position}, sum={position_sum}, least_common={least_common}")
        crb = list(filter(lambda b: int(b[position]) == least_common, crb))
        # print(crb)
        # print()
        position += 1
    co2_rating = int(crb[0], base=2)
    # print(co2_rating)

    return oxygen_rating * co2_rating


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        example = self.examples[0].strip().split("\n")
        self.assertEqual(198, part1(example))

    def test2_part2_example1(self):
        example = self.examples[0].strip().split("\n")
        self.assertEqual(230, part2(example))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file().strip().split("\n")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
