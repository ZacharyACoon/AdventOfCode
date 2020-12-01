from common.logging import log
from aoc_common import puzzle_input
import unittest


def trace_vectors(vectors):
    directions = {
        "U": lambda x, y: (x, y + 1),
        "D": lambda x, y: (x, y - 1),
        "L": lambda x, y: (x - 1, y),
        "R": lambda x, y: (x + 1, y),
    }
    path = {}
    x, y, d = 0, 0, 0
    for vector in vectors:
        distance = int(vector[1:])
        for step in range(distance):
            d += 1
            x, y = directions[vector[0]](x, y)
            if (x, y) in path:
                path[x, y].append(d)
            else:
                path[x, y] = [d]
    return path


def distance_from_origin(xy):
    return sum(map(abs, xy))


def determine_intersections(paths):
    intersections = set(paths[0])
    for path in paths[1:]:
        intersections.intersection_update(set(path))
    return intersections


def determine_closest_intersection(intersections):
    intersection_distances = map(distance_from_origin, intersections)
    intersections_by_distance = thing_by_thing(intersection_distances, intersections)
    closest_intersection_distance = min(intersections_by_distance)
    return intersections_by_distance[closest_intersection_distance]


def determine_distance_to_closest_intersection(paths):
    intersections = determine_intersections(paths)
    closest_intersection = determine_closest_intersection(intersections)
    distance = distance_from_origin(closest_intersection)
    return distance


def determine_shortest_length_to_intersection(paths):
    intersections = determine_intersections(paths)
    intersection_wire_lengths = [paths[0][intersection][0] + paths[1][intersection][0] for intersection in intersections]
    intersections_by_wire_length = thing_by_thing(intersection_wire_lengths, intersections)
    shortest_length_to_intersection = min(intersections_by_wire_length)
    return shortest_length_to_intersection


def thing_by_thing(a, b):
    return dict(zip(a, b))


def derive_paths_from_vectors(vectors):
    return list(map(trace_vectors, vectors))


def parse_vectors(s):
    return [line.split(',') for line in s.split('\n')]


class WireTracingTests(unittest.TestCase):
    def _test_closest_intersection_distance(self, a, b):
        vectors = parse_vectors(a)
        paths = derive_paths_from_vectors(vectors)
        distance = determine_distance_to_closest_intersection(paths)
        self.assertEqual(distance, b)

    def test_closest_intersection1(self):
        self._test_closest_intersection_distance(
            "U1,R1\n"
            "R1,U1",
            2
        )

    def test_closest_intersection2(self):
        self._test_closest_intersection_distance(
            "R75,D30,R83,U83,L12,D49,R71,U7,L72\n"
             "U62,R66,U55,R34,D71,R55,D58,R83",
             159
        )

    def test_closest_intersection3(self):
        self._test_closest_intersection_distance(
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n"
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            135
        )

    def _test_shortest_length_to_intersection(self, a, b):
        vectors = parse_vectors(a)
        paths = derive_paths_from_vectors(vectors)
        length = determine_shortest_length_to_intersection(paths)
        self.assertEqual(length, b)

    def test_shortest_length_to_intersection1(self):
        self._test_shortest_length_to_intersection(
            "R75,D30,R83,U83,L12,D49,R71,U7,L72\n"
            "U62,R66,U55,R34,D71,R55,D58,R83",
            610
        )

    def test_shortest_length_to_intersection2(self):
        self._test_shortest_length_to_intersection(
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n"
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            410
        )


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=0)

    vectors = parse_vectors(puzzle_input)
    paths = list(map(trace_vectors, vectors))
    intersections = determine_intersections(paths)

    # part 1
    answer = determine_distance_to_closest_intersection(paths)
    log.info(f"Part One, Distance to Closest Intersection to Origin = {answer}")

    # part 2
    answer = determine_shortest_length_to_intersection(paths)
    log.info(f"Part Two, Shortest Wire Length to Intersection = {answer}")gps