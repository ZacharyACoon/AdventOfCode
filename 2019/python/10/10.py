import unittest
from aoc_common import puzzle_input
from common.logging import root_logger
from unittest import TestCase


def parse_input_asteroids_by_position(s):
    # asteroids by position
    asteroids = set()
    for y, row in enumerate(s.split('\n')):
        for x, position in enumerate(row):
            asteroid = x, y
            asteroids.add(asteroid)
    return asteroids


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=0)
    root_logger.info(f"Part One = {answer}")
