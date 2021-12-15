import unittest
import math
import time
from aoc2021.common import puzzle_input


def count_pairs(template):
    pair_counts = {}
    for o in range(len(template)-1):
        a = template[o]
        b = template[o+1]
        ab = a, b
        if ab not in pair_counts:
            pair_counts[ab] = 1
        else:
            pair_counts[ab] += 1
    return pair_counts


def parse(data):
    lines = data.strip().splitlines()
    template = list(lines[0])
    pair_counts = count_pairs(template)

    rules = dict()
    for line in lines[2:]:
        ab, c = line.split(" -> ")
        ab = tuple(ab)
        rules[ab] = c
    return pair_counts, rules


def step(pair_counts, rules):
    old_pair_counts = pair_counts
    pair_counts = pair_counts.copy()
    for (ab), count in old_pair_counts.items():
        a, b = ab
        c = rules[ab]
        ac = a, c
        cb = c, b
        pair_counts[ab] -= count

        if ac not in pair_counts:
            pair_counts[ac] = 0
        pair_counts[ac] += count

        if cb not in pair_counts:
            pair_counts[cb] = 0
        pair_counts[cb] += count

    return pair_counts


def count_elements_in_pairs(pairs_count):
    elements = {}
    for (ab), count in pairs_count.items():
        a, b = ab
        if a not in elements:
            elements[a] = 0
        elements[a] += count

        if b not in elements:
            elements[b] = 0
        elements[b] += count

    for element, count in elements.items():
        elements[element] = math.ceil(count / 2)

    return elements


def determine_commons(counts):
    least_common_count = math.inf
    most_common_count = -math.inf
    for c, count in counts.items():
        least_common_count = min(least_common_count, count)
        most_common_count = max(most_common_count, count)
    return least_common_count, most_common_count


def part1(data, steps=10):
    pair_counts, rules = parse(data)
    # print(pair_counts)
    start_time = time.time()
    for s in range(steps):
        pair_counts = step(pair_counts, rules)
        step_time = time.time()
        # print(f"Step {s+1}, {step_time-start_time:{0:.8f}} seconds.")
        # print(pair_counts)
    element_counts = count_elements_in_pairs(pair_counts)
    least_common_count, most_common_count = determine_commons(element_counts)
    return most_common_count - least_common_count


def part2(data, steps=40):
    return part1(data, steps)


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        example = puzzle_input.from_example(__file__, 1)
        self.assertEqual(1588, part1(example, steps=10))

    def test2_part2_example1(self):
        example = puzzle_input.from_example(__file__, 1)
        self.assertEqual(2188189693529, part2(example, steps=40))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
