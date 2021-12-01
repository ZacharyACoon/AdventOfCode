import math
import unittest
from aoc2021.common import puzzle_input


def part1(depths):
    depth_increased_count = -1
    last_depth = 0
    for depth in depths:
        if depth > last_depth:
            depth_increased_count += 1
        last_depth = depth
    return depth_increased_count


def part2(depths):
    count = 0
    s = 0
    sliding_sums = []
    for i, v in enumerate(depths):
        s += v
        count += 1
        # print(i, v, s, count)
        if count == 3:
            sliding_sums.append(s)
            count -= 1
            s -= depths[i-2]
            # print(f"Removing {depths[i-3]}")

    return part1(sliding_sums)


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        example = list(map(int, self.examples[0].strip().split("\n")))
        self.assertEqual(7, part1(example))

    def test2_part2_example1(self):
        example = list(map(int, self.examples[0].strip().split("\n")))
        self.assertEqual(5, part2(example))


if __name__ == "__main__":
    # unittest.main()
    data = list(map(int, puzzle_input.from_arg_file().strip().split("\n")))
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
