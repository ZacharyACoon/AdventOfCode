from common.logging import log
from aoc_common import puzzle_input
import unittest


def parse_orbits(s):
    for line in s.split('\n'):
        yield line


def parse_orbit(orbit_s):
    parent, child = orbit_s.split(")")
    return parent, child


def orbit_tree_by_child(orbits):
    parents_by_child = dict()
    for orbit in orbits:
        parent, child = parse_orbit(orbit)
        parents_by_child[child] = parent
    return parents_by_child


def recurse_parents(parents_by_child: dict, child: str):
    if child in parents_by_child:
        parent = parents_by_child[child]
        return [child] + recurse_parents(parents_by_child, parent)
    else:
        return [child]


if __name__ == "__main__":

    orbits = parse_orbits(puzzle_input)
    parents_by_child = orbit_tree_by_child(orbits)

    YOU_path = set(recurse_parents(parents_by_child, "YOU"))
    SAN_path = set(recurse_parents(parents_by_child, "SAN"))

    symmetric_difference_path = YOU_path.symmetric_difference(SAN_path)
    print(len(symmetric_difference_path) - 2)
