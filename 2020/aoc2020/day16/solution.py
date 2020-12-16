import unittest
from aoc2020.common import puzzle_input
import re
import math


def parse_rules(data):
    rules = {}
    regex = r"([\w ]+)\: (\d+)-(\d+) or (\d+)-(\d+)"
    for key, *values in re.findall(regex, data):
        r = tuple(int(v) for v in values)
        rules[key] = lambda v, r=r: (r[0] <= v <= r[1] or r[2] <= v <= r[3])
    return rules


def parse_nearby_tickets(data):
    nearby_str = data.split("nearby tickets:")[1].strip()
    nearby_tickets = nearby_str.splitlines()
    tickets = []
    for ticket in nearby_tickets:
        values = [int(v) for v in re.findall(r"(\d+)", ticket)]
        tickets.append(values)
    return tickets


def parse_your_ticket(data):
    your_str = data.split("your ticket:")[1].strip().splitlines()[0]
    return tuple(int(v) for v in re.findall(r"(\d+)", your_str))


def get_invalid_values(rules, ticket):
    invalid_values = []
    for value in ticket:
        if not any(rule(value) for rule in rules.values()):
            invalid_values.append(value)
    return invalid_values


def validate_ticket(rules, ticket):
    return not get_invalid_values(rules, ticket)


def derive_offset_rule_map(rules, tickets, offset_rule_candidates=None):
    if offset_rule_candidates is None:
        offset_rule_candidates = {}
        num_offsets = len(tickets[1])
        for o in range(num_offsets):
            offset_rule_candidates[o] = list(rules.keys())

    for ticket in tickets:
        queued_changes = {}
        corrupted_ticket = False
        for o, v in enumerate(ticket):
            queued_changes[o] = offset_rule_candidates[o].copy()
            for rule in offset_rule_candidates[o]:
                print(o, v, rule, end="")
                validator = rules[rule]
                if validator(v):
                    print(" valid")
                else:
                    if not any(r(v) for r in rules.values()):
                        print(" corrupted ticket!")
                        corrupted_ticket = True
                        break
                    else:
                        print(" invalid")
                        queued_changes[o].remove(rule)
        if not corrupted_ticket:
            offset_rule_candidates.update(queued_changes)

    return offset_rule_candidates


def reduce_offset_candidates(offset_rule_candidates):
    changing = True
    while changing:
        changing = False
        for offset in offset_rule_candidates:
            rules = offset_rule_candidates[offset]
            if len(rules) == 1:
                rule = rules[0]
                for o, r in offset_rule_candidates.items():
                    if rule in r and len(r) > 1:
                        changing = True
                        r.remove(rule)
    return offset_rule_candidates


def translate_candidates_to_offsets(offset_rule_candidates):
    return dict((rules[0], offset) for offset, rules in offset_rule_candidates.items())


def part1(data):
    rules = parse_rules(data)
    return sum(sum(get_invalid_values(rules, ticket)) for ticket in parse_nearby_tickets(data))


def part2(data):
    rules = parse_rules(data)
    your_ticket = parse_your_ticket(data)
    nearby_tickets = parse_nearby_tickets(data)
    print(f"Rules: {len(rules)}, Nearby Tickets: {len(nearby_tickets)}")
    from functools import partial
    valid_tickets = list(filter(partial(validate_ticket, rules), nearby_tickets))
    result = derive_offset_rule_map(rules, nearby_tickets)
    [print(thing) for thing in result.items()]
    result = reduce_offset_candidates(result)
    [print(thing) for thing in result.items()]
    rule_offsets = translate_candidates_to_offsets(result)
    print(rule_offsets)
    departure_str_offsets = [offset for rule, offset in rule_offsets.items() if rule.startswith("departure")]
    departure_values = [your_ticket[offset] for offset in departure_str_offsets]
    return math.prod(departure_values)


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        self.assertEqual(71, part1(self.examples[0]))

    def test2_part2_example1(self):
        part2(self.examples[1])


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
