import unittest
from aoc2020.common import puzzle_input
from scipy.spatial.kdtree import KDTree
import numpy as np

"""
# active
. inactive
"""


def parse_active_coordinates(data, dimensions=2):
    data = data.splitlines()
    coordinates = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                coordinates.append((*(x, y), *[0 for _ in range(dimensions-2)]))
    boundaries = [
        0, len(data[0]),
        0, len(data),
    ]
    for _ in range(dimensions - 2):
        boundaries.append(0)
        boundaries.append(1)
    return coordinates, boundaries


def generate_tesseract(coordinates, boundaries):
    pts = np.array(coordinates)
    tree = KDTree(pts, leafsize=1000)
    active_list = coordinates
    active_dict = dict((coordinate, True) for coordinate in coordinates)
    return tree, active_dict, active_list, boundaries


def recursively_iterate_boundaries(boundaries, layer=None):
    if layer is None:
        layer = []
    minimum = boundaries[0]
    maximum = boundaries[1]
    if len(boundaries) > 2:
        for thing in range(minimum-1, maximum+1):
            yield from recursively_iterate_boundaries(boundaries[2:], layer=(*layer, thing))
    else:
        for thing in range(minimum-1, maximum+1):
            yield *layer, thing


def count_neighbors(tesseract, coordinate):
    tree, active_dict, active_list, boundaries = tesseract
    # don't count given coordinate itself as a neighbor
    neighbor_offsets = tree.query_ball_point(coordinate, 1.999)
    neighbors = len([o for o in neighbor_offsets if active_list[o] != coordinate])
    print(neighbors)
    # for debugging neighbors found at each point
    # neighbors = 0
    # for o in neighbor_offsets:
    #     print("active list", active_list)
    #     if active_list[o] != coordinate:
    #         print("ignore self")
    #         continue
    #     neighbors += 1
    return neighbors


def flip_tesseract(tesseract: (KDTree, list)):
    tree, active_dict, active_list, boundaries = tesseract
    new_active_dict = active_dict.copy()
    new_boundaries = boundaries.copy()
    for coordinate in recursively_iterate_boundaries(boundaries):
        neighbors = count_neighbors(tesseract, coordinate)
        # print(coordinate, neighbors)
        if coordinate in active_dict:
            if not 2 <= neighbors <= 3:
                del new_active_dict[coordinate]
        else:
            if neighbors == 3:
                new_active_dict[coordinate] = True
                # expand boundaries of tesseract if needed
                for c, o in enumerate(range(0, len(boundaries), 2)):
                    if coordinate[c] <= boundaries[o]:
                        new_boundaries[o] = boundaries[o] - 1
                    elif coordinate[c] >= boundaries[o+1]:
                        new_boundaries[o+1] = boundaries[o+1] + 1
    new_active_list = list(new_active_dict.keys())
    pts = np.array(new_active_list)
    new_tree = KDTree(pts, leafsize=1000)
    return new_tree, new_active_dict, new_active_list, new_boundaries


def count_active(tesseract):
    tree, active_dict, active_list, boundaries = tesseract
    return len(active_list)


def print_tesseract(tesseract, layer=None):
    tree, active_dict, active_list, boundaries = tesseract
    if layer is None:
        layer = []
    if len(boundaries) // 2 - len(layer) > 2:
        o = len(boundaries)-len(layer)*2-2
        minimum = boundaries[o]
        maximum = boundaries[o+1]
        for thing in range(minimum, maximum):
            print_tesseract(tesseract, layer=(*layer, thing))
    else:
        plate = ""
        for y in range(boundaries[2], boundaries[3]):
            row = ""
            for x in range(boundaries[0], boundaries[1]):
                if (x, y, *reversed(layer)) in active_dict:
                    row += "#"
                else:
                    row += "."
            plate += row + "\n"
        print(*layer)
        print(plate)


def part1(data):
    active_coordinates, boundaries = parse_active_coordinates(data, 3)
    tesseract = generate_tesseract(active_coordinates, boundaries)
    for _ in range(6):
        tesseract = flip_tesseract(tesseract)
        print_tesseract(tesseract)
        quit()
    return count_active(tesseract)


def part2(data):
    active_coordinates, boundaries = parse_active_coordinates(data, 4)
    tesseract = generate_tesseract(active_coordinates, boundaries)
    print_tesseract(tesseract)
    print("cycle")
    tesseract = flip_tesseract(tesseract)
    print_tesseract(tesseract)


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        self.assertEqual(112, part1(self.examples[0]))
    #
    # def test2_part2_example(self):
    #     part2(self.examples[0])


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    # print("Part 2:", part2(data))
