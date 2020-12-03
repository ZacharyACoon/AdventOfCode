from itertools import permutations
import math


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
