from common.logging import log
from aoc_common import puzzle_input
import unittest
import math


def determine_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    return fuel


def determine_fuel_recursive(mass):
    fuel = determine_fuel(mass)
    if fuel > 0:
        return fuel + determine_fuel_recursive(fuel)
    else:
        return 0


class TestFuelCalculations(unittest.TestCase):
    def test_determine_fuel(self):
        def test(a, b):
            self.assertEqual(determine_fuel(a), b)

        test(12, 2)
        test(14, 2)
        test(1969, 654)
        test(100756, 33583)

    def test_determine_fuel_recursive(self):
        def test(a, b):
            self.assertEqual(determine_fuel_recursive(a), b)

        test(14, 2)
        test(1969, 966)
        test(100756, 50346)


def parse_module_masses(s):
    return [int(line.strip()) for line in s.split('\n')]


if __name__ == '__main__':
    unittest.main(exit=False)

    for f in (determine_fuel, determine_fuel_recursive):
        module_masses = parse_module_masses(puzzle_input)
        fuel = sum(map(f, module_masses))
        log.info(f"{f.__name__} = {fuel}")
