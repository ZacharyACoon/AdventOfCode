import unittest
from aoc2020.common import puzzle_input


"""
# active
. inactive
"""


def parse_active_coordinates(data, dimensions=2):
    data = data.splitlines()
    coordinates = set()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                coordinates.add((*(x, y), *[0 for _ in range(dimensions-2)]))
    bounds = [
        0, len(data[0]),
        0, len(data),
    ]
    for _ in range(dimensions - 2):
        bounds.append(0)
        bounds.append(1)
    return coordinates, bounds


def recursively_iterate_boundaries(bounds, layer=None):
    if layer is None:
        layer = []
    if len(bounds) > 2:
        for thing in range(bounds[0]-1, bounds[1]+1):
            yield from recursively_iterate_boundaries(bounds[2:], layer=(*layer, thing))
    else:
        for thing in range(bounds[0]-1, bounds[1]+1):
            yield *layer, thing


def get_neighbor_coordinates(coordinates):
    bounds = []
    for coordinate in coordinates:
        bounds.append(coordinate)
        bounds.append(coordinate + 1)
    for coordinate in recursively_iterate_boundaries(bounds):
        if coordinate != coordinates:
            yield coordinate


def count_neighbors(active, coordinates):
    neighbors = 0
    for coordinate in get_neighbor_coordinates(coordinates):
        if coordinate in active:
            neighbors += 1
    return neighbors


def flip_tesseract(active, bounds):
    new_active = active.copy()
    new_bounds = bounds.copy()
    for coordinate in recursively_iterate_boundaries(bounds):
        neighbors = count_neighbors(active, coordinate)
        if coordinate in active:
            if not 2 <= neighbors <= 3:
                # active
                new_active.remove(coordinate)
        else:
            # inactive
            if neighbors == 3:
                # activate
                new_active.add(coordinate)
                # update bounds
                for c, o in enumerate(range(0, len(bounds), 2)):
                    if coordinate[c] <= new_bounds[o]:
                        new_bounds[o] -= 1
                    elif coordinate[c] >= new_bounds[o+1]:
                        new_bounds[o+1] += 1
    return new_active, new_bounds


def print_tesseract(active, bounds, layer=None):
    if layer is None:
        layer = []
    if len(bounds) // 2 - len(layer) > 2:
        o = len(bounds) - len(layer) * 2 - 2
        for thing in range(bounds[o], bounds[o + 1]):
            print_tesseract(active, bounds, layer=(*layer, thing))
    else:
        plate = ""
        for y in range(bounds[2], bounds[3]):
            row = ""
            for x in range(bounds[0], bounds[1]):
                if (x, y, *reversed(layer)) in active:
                    row += "#"
                else:
                    row += "."
            plate += row + "\n"
        print(*layer)
        print(plate)


def cycle_tesseract(active, bounds, count):
    # print_tesseract(active, bounds)
    for c, _ in enumerate(range(count)):
        active, bounds = flip_tesseract(active, bounds)
        # print(f"After {c+1} cycle:")
        # print(f"Active: ", len(active))
        # print_tesseract(active, bounds)
    return active, bounds


def part1(data):
    active, bounds = parse_active_coordinates(data, 3)
    active, bounds = cycle_tesseract(active, bounds, 6)
    return len(active)


def part2(data):
    active, bounds = parse_active_coordinates(data, 4)
    active, bounds = cycle_tesseract(active, bounds, 6)
    return len(active)


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        self.assertEqual(112, part1(self.examples[0]))

    def test2_part2_example(self):
        self.assertEqual(848, part2(self.examples[0]))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
