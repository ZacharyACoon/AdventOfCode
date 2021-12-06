import unittest
from aoc2021.common import puzzle_input


def part1(data, days=80):
    frame = list(map(int, data.split(",")))
    for day in range(days):
        new_frame = []
        for fish in frame:
            fish -= 1
            if fish < 0:
                fish = 6
                new_frame.append(fish)
                new_frame.append(8)
            else:
                new_frame.append(fish)
        frame = new_frame
    return len(frame)


def part2(data, days=256):
    fish = list(map(int, data.split(",")))
    fish_counts = dict(zip(range(9), [0]*9))
    for f in fish:
        fish_counts[f] += 1
    print(fish_counts)

    for day in range(days):
        new_fish_counts = dict(zip(range(9), [0]*9))
        for k, v in fish_counts.items():
            if k == 0:
                new_fish_counts[6] += v
                new_fish_counts[8] += v
            else:
                new_fish_counts[k-1] += v
        fish_counts = new_fish_counts
    return sum(fish_counts.values())


class Test(unittest.TestCase):
    def test1_part1_example1(self):
        example = "3,4,3,1,2"
        self.assertEqual(26, part1(example, 18))
        self.assertEqual(5934, part1(example, 80))

    def test2_part2_example1(self):
        example = "3,4,3,1,2"
        self.assertEqual(26984457539, part2(example))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
