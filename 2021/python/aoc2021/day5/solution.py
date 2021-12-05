import unittest
from aoc2021.common import puzzle_input
from pprint import pprint


def parse_points(s):
    coords = []
    num = ""
    for c in s:
        if c.isdigit():
            num += c
        else:
            if num:
                coords.append(int(num))
                num = ""
    if num:
        coords.append(int(num))

    xy_pairs = [(coords[i: i+2]) for i in range(0, len(coords), 2)]
    coord_pairs = [xy_pairs[i: i+2] for i in range(0, len(xy_pairs), 2)]
    return coord_pairs


def print_wires(wires):
    for y in range(0, 10):
        for x in range(0, 10):
            if not (x, y) in wires:
                print(".", end="")
            else:
                print(wires[(x,y)], end="")
        print()
    print()

def part1(data):
    coord_pairs = parse_points(data)
    # print(len(coord_pairs))
    wires = {}
    for pair in coord_pairs:
        # print(pair)
        p1, p2 = pair
        x1, y1 = p1
        x2, y2 = p2
        # horizontal or vertical
        if y1 == y2:
            # print("horizontal")
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            for x in range(min_x, max_x+1):
                point = x, y1
                # print(point)
                if point not in wires:
                    wires[point] = 1
                else:
                    wires[point] += 1

        if x1 == x2:
            # print("vertical")
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            for y in range(min_y, max_y+1):
                point = x1, y
                # print(point)
                if point not in wires:
                    wires[point] = 1
                else:
                    wires[point] += 1

    # pprint(wires.values())
    print_wires(wires)
    return len(list(filter(lambda a: a > 1, wires.values())))


def part2(data):
    coord_pairs = parse_points(data)
    wires = {}

    for pair in coord_pairs:
        p1, p2 = pair
        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2:
            xi = 0
        elif x1 < x2:
            xi = 1
        else:
            xi = -1

        if y1 == y2:
            yi = 0
        elif y1 < y2:
            yi = 1
        else:
            yi = -1

        x = x1
        y = y1
        # print(2)
        # print(pair)
        while x != x2 + xi or y != y2 + yi:
            point = x, y
            # print(point, xi, yi)
            if point not in wires:
                wires[point] = 1
            else:
                wires[point] += 1

            x += xi
            y += yi

    print_wires(wires)

    return len(list(filter(lambda a: a > 1, wires.values())))


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        example = self.examples[0]
        self.assertEqual(5, part1(example))

    def test2_part2_example1(self):
        example = self.examples[0]
        self.assertEqual(12, part2(example))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
