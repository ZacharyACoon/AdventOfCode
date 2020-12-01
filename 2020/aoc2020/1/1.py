from aoc2020.common import puzzle_input, testing
from itertools import permutations
import math
import unittest


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
    for permutation in permutations(values, components):
        if sum(permutation) == summation:
            return permutation, math.prod(permutation)


class Test(testing.TimedTestCase):
    example_input1 = puzzle_input.type_per_line(puzzle_input.from_example(__file__, 1))

    def test1_find_product_with_2(self):
        a = find_product_of_sum_components(self.example_input1, 2, 2020)
        self.assertEqual(a, ((1721, 299), 514579))

    def test2_find_product_with_3(self):
        a = find_product_of_sum_components(self.example_input1, 3, 2020)
        self.assertEqual(a, ((979, 366, 675), 241861950))


if __name__ == "__main__":
    unittest.main(exit=False)

    puzzle_input = [int(value) for value in puzzle_input.from_file_arg().splitlines()]

    print("Part 1:", find_product_of_sum_components(puzzle_input, 2, 2020))
    print("Part 2:", find_product_of_sum_components(puzzle_input, 3, 2020))
