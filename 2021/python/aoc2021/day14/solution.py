import unittest
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

    return template, rules, pair_counts


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
    template, rules, pair_counts = parse(data)
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


def step2(pair_counts, rules):
    old_pair_counts = pair_counts
    pair_counts = dict()

    changes = {}
    for (ab), count in old_pair_counts.items():
        a, b = ab
        c = rules[ab]
        ac = a, c
        cb = c, b
        if ab not in changes:
            changes[ab] = 0
        changes[(a, b)] -= count

        if ac not in changes:
            changes[ac] = 0
        changes[(a, c)] += count

        if cb not in changes:
            changes[cb] = 0
        changes[(c, b)] += count

    # print("old_pair_counts")
    # print(old_pair_counts)
    # print("changes")
    # print(changes)

    for pair, change in changes.items():
        if pair not in old_pair_counts:
            count = 0
        else:
            count = old_pair_counts[pair]
        count += change
        if count != 0:
            pair_counts[pair] = count

    # print("pair_counts")
    # print(pair_counts)

    return pair_counts


def count_elements2(pairs_count):
    elements = {}
    for ab, count in pairs_count.items():
        a, b = ab
        if a not in elements:
            elements[a] = 0
        elements[a] += count

        if b not in elements:
            elements[b] = 0
        elements[b] += count
    return elements

import math

def part2(data, steps=40):
    template, rules, pair_counts = parse(data)
    start_time = time.time()
    for s in range(steps):
        pair_counts = step2(pair_counts, rules)
        step_time = time.time()
        print(f"step {s+1} took {step_time - start_time} seconds.")

    element_counts = count_elements2(pair_counts)
    # print(element_counts)

    least_common = None
    least_common_count = math.inf
    most_common_count = -math.inf

    for c, count in element_counts.items():
        count = math.ceil(count / 2)
        if count < least_common_count:
            least_common = c
            least_common_count = count
        if count > most_common_count:
            most_common = c
            most_common_count = count

    # print(most_common)
    # print(most_common_count)
    # print(least_common)
    # print(least_common_count)

    return most_common_count - least_common_count


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        example = puzzle_input.from_example(__file__, 1)
        self.assertEqual(1588, part2(example, steps=10))

    def test2_part2_example1(self):
        example = self.examples[0]
        self.assertEqual(2188189693529, part2(example, steps=40))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
