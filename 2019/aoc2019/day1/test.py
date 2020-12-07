from aoc2019.common import testing
from . import solution


class Test(testing.TimedTestCase):
    def test_part1_example1(self):
        self.assertEqual(2, solution.calculate_fuel_for_mass(12))
        self.assertEqual(2, solution.calculate_fuel_for_mass(14))
        self.assertEqual(654, solution.calculate_fuel_for_mass(1969))
        self.assertEqual(33583, solution.calculate_fuel_for_mass(100756))

    def test_part2_example1(self):
        self.assertEqual(2, solution.calculate_fuel_for_mass_recursively(14))
        self.assertEqual(966, solution.calculate_fuel_for_mass_recursively(1969))
        self.assertEqual(50346, solution.calculate_fuel_for_mass_recursively(100756))
