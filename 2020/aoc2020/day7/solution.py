import re


def sanitize(input):
    return re.sub(r"(?: bags?)|(?:\.)", "", input)


def parse_rules(input):
    inner_rules = {}
    outer_rules = {}
    for line in sanitize(input).splitlines():
        key, values = line.split(" contain ")
        values = values.split(", ")
        for value in values:
            if not value == "no other":
                count = int(value[0])
                bag = value[2:]
                if key not in inner_rules:
                    inner_rules[key] = {}

                inner_rules[key][bag] = count

                if bag not in outer_rules:
                    outer_rules[bag] = [key]
                else:
                    outer_rules[bag].append(key)

    return inner_rules, outer_rules


def determine_outer_recursive(outer_rules, bag):
    if bag in outer_rules:
        for outer in outer_rules[bag]:
            yield outer
            yield from determine_outer_recursive(outer_rules, outer)


def determine_inner_recursive(inner_rules, bag):
    if bag in inner_rules:
        for layer in inner_rules[bag]:
            count = int(inner_rules[bag][layer])
            for _ in range(count):
                yield layer
                yield from determine_inner_recursive(inner_rules, layer)


def part1(input):
    _, outer_rules = parse_rules(input)
    possible_outer_layers = determine_outer_recursive(outer_rules, "shiny gold")
    unique_outer_layers = set(possible_outer_layers)
    count_unique_outer_layers = len(unique_outer_layers)
    return count_unique_outer_layers


def part2(input):
    inner_rules, _ = parse_rules(input)
    inner_items = list(determine_inner_recursive(inner_rules, "shiny gold"))
    return len(inner_items)


if __name__ == "__main__":
    from aoc2020.common import puzzle_input
    input = puzzle_input.from_arg_file()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
