import unittest
from aoc2021.common.testing import TimedTestCase
from aoc2021.common import puzzle_input


def parse_fish(data):
    return list(map(int, data.split(",")))


def map_fish_age_to_count(fish):
    fish_counts = dict(zip(range(9), [0]*9))
    for f in fish:
        fish_counts[f] += 1
    return fish_counts


def age_fish(fish_counts, days):
    frame = fish_counts
    for day in range(days):
        new_frame = map_fish_age_to_count([])
        for k, v in frame.items():
            if k == 0:
                new_frame[6] += v
                new_frame[8] += v
            else:
                new_frame[k-1] += v
        frame = new_frame
    return frame


def part1(data, days=80):
    fish = parse_fish(data)
    fish_counts = map_fish_age_to_count(fish)
    fish_counts = age_fish(fish_counts, days)
    return sum(fish_counts.values())


def part2(data, days=256):
    fish = parse_fish(data)
    fish_counts = map_fish_age_to_count(fish)
    fish_counts = age_fish(fish_counts, days)
    return sum(fish_counts.values())


class Test(TimedTestCase):
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
