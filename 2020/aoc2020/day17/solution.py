import unittest
from aoc2020.common import puzzle_input


"""
# active
. inactive
"""


def parse_active_coordinates(data):
    data = data.splitlines()
    coordinates = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                coordinates.append((x, y, 0))
    x1 = 0
    x2 = len(data[0])
    y1 = 0
    y2 = len(data)
    z1 = 0
    z2 = 1
    return coordinates, x1, x2, y1, y2, z1, z2


def get_neighbor_coordinates(coordinates, things=None):
    if len(coordinates) == 1:
        for thing in range(coordinates[0]-1, coordinates[0]+2):
            yield *things, thing
    else:
        for thing in range(coordinates[0]-1, coordinates[0]+2):
            yield from get_neighbor_coordinates(coordinates[1:], things=(thing,))


def count_neighbors(tesseract, x, y, z):
    neighbors = 0
    for coordinate in get_neighbor_coordinates(x, y, z):
        if coordinate in tesseract:
            neighbors += 1
    return neighbors


def flip_tesseract(tesseract, x1, x2, y1, y2, z1, z2):
    nx1, nx2, ny1, ny2, nz1, nz2 = x1, x2, y1, y2, z1, z2
    new_tesseract = tesseract.copy()
    for z in range(z1-1, z2+1):
        for y in range(y1-1, y2+1):
            for x in range(x1-1, x2+1):
                coordinate = (x, y, z)
                if (x, y, z) in tesseract:
                    # active
                    neighbors = count_neighbors(tesseract, *coordinate)
                    if not (2 <= neighbors <= 3):
                        del new_tesseract[coordinate]
                else:
                    # inactive
                    neighbors = count_neighbors(tesseract, *coordinate)
                    if neighbors == 3:
                        # update bounds
                        if x == x1: nx1 = x1 - 1
                        if x == x2: nx2 = x2 + 1
                        if y == y1: ny1 = y1 - 1
                        if y == y2: ny2 = y2 + 1
                        if z == z1: nz1 = z1 - 1
                        if z == z2: nz2 = z2 + 1
                        new_tesseract[coordinate] = True
    return new_tesseract, nx1, nx2, ny1, ny2, nz1, nz2


def print_tesseract(tesseract, x1, x2, y1, y2, z1, z2):
    for z in range(z1, z2):
        # print(f"z={z}")
        lines = []
        for y in range(y1, y2):
            row = ""
            for x in range(x1, x2):
                row += "#" if (x, y, z) in tesseract else "."
            lines.append(row)
        # print("\n".join(lines) + "\n")
    # print()


def cycle_tesseract(tesseract, bounds, count):
    for c, _ in enumerate(range(count)):
        tesseract, *bounds = flip_tesseract(tesseract, *bounds)
        # print(f"After {c+1} cycle:")
        # print(f"Active: ", len(tesseract))
        print_tesseract(tesseract, *bounds)
    return tesseract, bounds


def part1(data, cycles=6):
    coordinates, *bounds = parse_active_coordinates(data)
    tesseract = dict((coordinate, True) for coordinate in coordinates)
    print_tesseract(tesseract, *bounds)
    tesseract, bounds = cycle_tesseract(tesseract, bounds, cycles)
    return len(tesseract)


def part2(data):
    for thing in get_neighbor_coordinates((3, 3, 3)):
        print(thing)


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    # def test1_part1_example1(self):
    #     self.assertEqual(112, part1(self.examples[0]), 6)

    def test2_part2_example(self):
        part2(self.examples[0])


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    # print("Part 1:", part1(data))
    # print("Part 2:", part2(data))
