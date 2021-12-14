import unittest
from aoc2021.common import puzzle_input


def parse(data):
    lines = data.strip().splitlines()
    template = list(lines[0])
    rules = dict()
    for line in lines[2:]:
        ab, c = line.split(" -> ")
        ab = tuple(ab)
        rules[ab] = c
    return template, rules


def step(template, rules):
    old_template = template
    template = []
    for o in range(len(old_template)-1):
        a = old_template[o]
        b = old_template[o+1]
        template.append(a)
        ab = tuple((a, b))
        template.append(rules[ab])
    template.append(b)
    return template


def count_elements(template):
    counts = dict()
    for c in template:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    return counts

import math
import time


def part1(data, steps=10):
    template, rules = parse(data)
    start_time = time.time()
    for s in range(steps):
        template = step(template, rules)
        step_time = time.time()
        print(f"Step {s} took {step_time-start_time} seconds.")

    counts = count_elements(template)
    least_common = None
    least_common_count = math.inf
    most_commont = None
    most_common_count = -math.inf
    for c, count in counts.items():
        if count < least_common_count:
            least_common = c
            least_common_count = count
        if count > most_common_count:
            most_commont = c
            most_common_count = count

    return most_common_count - least_common_count


def part2(data, steps=40):
    return part1(data, steps)


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        example = puzzle_input.from_example(__file__, 1)
        self.assertEqual(1588, part1(example, steps=10))

    def test2_part2_example1(self):
        example = self.examples[0]
        self.assertEqual(2188189693529, part2(example, steps=40))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
