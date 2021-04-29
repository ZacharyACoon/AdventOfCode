import unittest
from aoc2020.common import puzzle_input
from aoc2020.common.testing import TimedTestCase
from aoc2020.common.solution import Solution
# from aoc2020.common.cli import args
import re
import math
from functools import reduce

"""
timestamp, minutes since reference point
bus id == bus loop time
bus loops
"""


def parse_lines(input):
    timestamp, busses = input.split("\n")
    timestamp = int(timestamp)
    busses = busses.split(",")
    return timestamp, busses


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def chinese_remainder(n, a):
    s = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        s += a_i * mul_inv(p, n_i) * p
    return s % prod


class Solution(Solution):
    def part1(self, input):
        timestamp, busses = parse_lines(input)
        next_bus = math.inf
        next_bus_time = math.inf
        for bus in busses:
            if bus == "x":
                continue
            bus = int(bus)
            bus_next = (timestamp // bus + 1) * bus
            if bus_next < next_bus_time:
                next_bus = bus
                next_bus_time = bus_next
        return next_bus * (next_bus_time - timestamp)

    def part2(self, input):
        timestamp, busses = parse_lines(input)
        bus_increments = {}
        i = 0
        for bus in busses:
            if bus != "x":
                bus_increments[int(bus)] = i
            i += 1
        print(bus_increments)

        busses = list(bus_increments.keys())
        timestamp = 0
        increment = busses[0]
        for i, (bus, offset) in enumerate(bus_increments.items()):
            increment = math.prod(busses[:i])
            while True:
                timestamp += increment
                if (timestamp + offset) % bus == 0:
                    print(timestamp, offset)
                    increment = timestamp
                    break
        return timestamp


class Test(TimedTestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        self.assertEqual(295, Solution().part1(self.examples[0]))

    def test2_part2_example1(self):
        self.assertEqual(3417, Solution().part2(self.examples[1]))


if __name__ == "__main__":
    # unittest.main()
    input = puzzle_input.from_arg_file()

    solution = Solution()
    print("Part 1:", solution.part1(input))
    print("Part 2:", solution.part2(input))
    # print(args)
