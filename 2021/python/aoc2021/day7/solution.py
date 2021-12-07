import unittest
from aoc2021.common.testing import TimedTestCase
from aoc2021.common import puzzle_input
import math
# 21 57


def parse_crabs(data):
    return list(map(int, data.split(",")))


def map_position_to_count_and_get_range(crabs):
    counts = {}
    l = math.inf
    u = -math.inf
    for position in crabs:
        if position < l:
            l = position
        if position > u:
            u = position

        if position not in counts:
            counts[position] = 1
        else:
            counts[position] += 1
    return counts, l, u


def part1(data):
    crabs = parse_crabs(data)
    position_to_count, l, u = map_position_to_count_and_get_range(crabs)

    least_fuel_alignment = 0
    least_fuel_alignment_cost = math.inf
    for position in range(l, u+1):
        fuel_required = 0
        for crab_position, crab_count in position_to_count.items():
            fuel_required += abs(position - crab_position) * crab_count
        if fuel_required < least_fuel_alignment_cost:
            least_fuel_alignment_cost = fuel_required
            least_fuel_alignment = position
    return least_fuel_alignment_cost


def part2(data):
    crabs = parse_crabs(data)
    position_to_count, l, u = map_position_to_count_and_get_range(crabs)
    least_fuel_alignment_cost = math.inf
    for position in range(l, u+1):
        fuel_required = 0
        for crab_position, crab_count in position_to_count.items():
            distance = abs(position - crab_position)
            distance_change_cost = distance * (distance + 1) // 2
            fuel_required += distance_change_cost * crab_count

        if fuel_required < least_fuel_alignment_cost:
            least_fuel_alignment_cost = fuel_required
    return least_fuel_alignment_cost


class Test(TimedTestCase):
    example = "16,1,2,0,4,2,7,1,2,14"

    def test1_part1_example1(self):
        self.assertEqual(37, part1(self.example))

    def test2_part2_example1(self):
        self.assertEqual(168, part2(self.example))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
