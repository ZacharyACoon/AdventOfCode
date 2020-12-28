import unittest
from aoc2020.common import puzzle_input
import re
import numpy
from collections import Counter
import math


# def orientations_and_rotations(arr):
#     """
#     orientations: 0, 1 - 90d, 2 - 180d, 3 - 270d
#     flips: 0 - none, 1 - horizontal, 2 - vertical
#     :return:
#     """
#     for rotation in range(3):
#         for flip in range(3):
#             new = numpy.copy(arr)
#             new = numpy.rot90(new, rotation)
#             if flip == 1:
#                 new = numpy.fliplr(arr)
#             elif flip == 2:
#                 new = numpy.flipud(arr)
#             yield rotation, flip
#             yield new


def parse_plates(data):
    regex = r"Tile (\d+):\n((?:[\.\#]+\n{0,1})+)"
    for id, plate in re.findall(regex, data):
        id = int(id)
        height = len(plate.splitlines())
        width = len(plate.splitlines()[0])
        plate = plate.replace("\n", "").replace(".", "0").replace("#", "1")
        plate = numpy.array([bool(int(v)) for v in plate], dtype=bool)
        plate = plate.reshape([height, width])
        yield id, plate


def get_edge_hashes(arr):
    h = lambda v: hash(tuple(v))
    n = h(arr[0])
    nf = h(arr[0][::-1])
    e = h(arr[0:, -1])
    ef = h(arr[0:, -1][::-1])
    s = h(arr[-1])
    sf = h(arr[-1][::-1])
    w = h(arr[0:, 0])
    wf = h(arr[0:, 0][::-1])
    return n, e, s, w, nf, ef, sf, wf


def get_maps(id_plates):
    edge_to_plates = {}
    plate_to_edges = {}
    for id, plate in id_plates:
        for edge in get_edge_hashes(plate):
            edge_to_plates.setdefault(edge, []).append(id)
            plate_to_edges.setdefault(id, []).append(edge)
    return edge_to_plates, plate_to_edges


def get_plates_to_plates_map(edges_to_plates, plate_to_edges):
    plates_to_plates = {}
    for plate, edges in plate_to_edges.items():
        for edge in edges:
            for neighbor_plate in edges_to_plates[edge]:
                if neighbor_plate != plate:
                    plates_to_plates.setdefault(plate, []).append(neighbor_plate)
                    plates_to_plates.setdefault(neighbor_plate, []).append(plate)
    return plates_to_plates


def part1(data):
    id_plates = parse_plates(data)
    edge_to_plates, plate_to_edges = get_maps(id_plates)
    plates_to_plates = get_plates_to_plates_map(edge_to_plates, plate_to_edges)
    corners = [plate for plate in plates_to_plates if len(plates_to_plates[plate]) == 8]
    return math.prod(corners)


def part2(data):
    id_plates = parse_plates(data)
    edges_to_plates, plates_to_edges = get_maps(id_plates)
    plates_to_plates = get_plates_to_plates_map(edges_to_plates, plates_to_edges)


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        self.assertEqual(20899048083289, part1(self.examples[0]))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
