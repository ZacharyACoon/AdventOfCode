import re

# bags color coded
# contain counts of other colored bags


def parse_rules(input):
    inner_rules = {}
    outer_rules = {}

    for line in input.splitlines():
        outer, inner = line.split(" bags contain ")
        contents = re.sub(r"(?: bags?)|\.|\n", "", inner)
        inner = contents.split(", ")
        inner_count = {}
        for bag in inner:
            count = bag[0]
            if count != "n":
                bag = bag[2:]
                inner_count[bag] = count
                if bag not in outer_rules:
                    outer_rules[bag] = [outer]
                else:
                    outer_rules[bag].append(outer)
        inner_rules[outer] = inner_count
    return inner_rules, outer_rules


def determine_outer(outer_rules, bag):
    if bag in outer_rules:
        for shell in outer_rules[bag]:
            print(shell)


def determine_layer_recursive(layer_rules, bag):
    if bag in layer_rules:
        for layer in layer_rules[bag]:
            yield layer
            yield from determine_layer_recursive(layer_rules, layer)


def determine_inner_recursive(inner_rules, bag):
    if bag in inner_rules:
        for layer in inner_rules[bag]:
            count = int(inner_rules[bag][layer])
            for _ in range(count):
                yield layer
                yield from determine_inner_recursive(inner_rules, layer)


def part1(input):
    inner_rules, outer_rules = parse_rules(input)
    return len(set(determine_layer_recursive(outer_rules, "shiny gold")))


def part2(input):
    inner_rules, outer_rules = parse_rules(input)
    print(inner_rules)
    print(len(list(determine_inner_recursive(inner_rules, "shiny gold"))))


if __name__ == "__main__":
    from aoc2020.common import puzzle_input
    input = puzzle_input.from_arg_file()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
