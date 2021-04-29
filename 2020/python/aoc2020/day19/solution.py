import unittest
from aoc2020.common import puzzle_input
import re

def parse_rule(rule):
    if len(rule) > 1:
        ors = rule.split(" | ")
        rs = [map(int, r.split(" "))]
        ors = [r.split()]
        ors = []
        parts = rule.split(" ")

        try:
            parts.index("|")

        if "|" in parts:


def parse_rules(data):
    rules = {}
    regex = r'(\d+): (?:")?([\w \|]+)(?:")?'
    for key, value in re.findall(regex, data):
        rules[int(key)] = value
    return rules


def parse_data(data):
    rules_str, messages = data.split("\n\n")
    raw_rules = parse_rules(rules_str)
    return raw_rules, messages


def part1(data):
    raw_rules, messages = parse_data(data)
    print(raw_rules)
    print(messages)


def part2(data):
    pass


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        part1(self.examples[0])
        # self.assertEqual(0, solution.part1(self.examples[0]))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
