import unittest
from aoc2021.common import puzzle_input


def parse(data):
    lines = data.strip().splitlines()
    width = len(lines[0])
    height = len(lines)
    os = dict()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            xy = x, y
            os[xy] = int(c)
    return os, width, height


def display(os, width, height):
    lines = ""
    for y in range(height):
        line = ""
        for x in range(width):
            xy = x, y
            line += str(os[xy])
        lines += line + "\n"
        line = ""
    print(lines.strip())


def cascade_flash(os, width, height, flash, flashed=None):
    if flashed is None:
        flashed = set()

    next_flash = set()
    for xy in flash:
        flashed.add(xy)
        x, y = xy
        neighboring_xys = (
            (x, y - 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
            (x, y + 1),
            (x - 1, y + 1),
            (x - 1, y),
            (x - 1, y - 1)
        )
        for nxy in neighboring_xys:
            if e := os.get(nxy):
                e += 1
                os[nxy] = e
                if e > 9 and nxy not in flashed:
                    next_flash.add(nxy)

    next_flash.difference_update(flashed)

    if next_flash:
        cascade_flash(os, width, height, next_flash, flashed)

    return flashed


def step(os, width, height):
    old_os = os
    os = os.copy()

    to_flash = set()
    for xy, e in os.items():
        e += 1
        if e > 9:
            to_flash.add(xy)
        os[xy] = e

    flashed = cascade_flash(os, width, height, to_flash)
    for xy in flashed:
        os[xy] = 0

    return os, len(flashed)


def part1(data, steps=100):
    os, width, height = parse(data)
    total_flashes = 0
    for s in range(steps):
        os, step_flashes = step(os, width, height)
        total_flashes += step_flashes

    return total_flashes


def part2(data):
    os, width, height = parse(data)
    o_count = len(os)
    s = 0
    while True:
        os, step_flashes = step(os, width, height)
        s += 1
        if step_flashes == o_count:
            return s


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example2_part1(self):
        example = self.examples[0]
        self.assertEqual(1656, part1(example))

    def test2_part2_example1(self):
        example = self.examples[0]
        self.assertEqual(195, part2(example))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
