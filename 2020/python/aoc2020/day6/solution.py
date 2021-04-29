

def parse_groups(input):
    for group in input.split("\n\n"):
        yield group


def count_unique_yeses(group):
    letters = group.replace(" ", "").replace("\n", "")
    return len(set(letters))


# also import collections.Counter .keys() .values()
def get_distribution(letters):
    answers = letters.replace(" ", "").replace("\n", "")
    distribution = {}
    for answer in answers:
        if not answer in distribution:
            distribution[answer] = 1
        else:
            distribution[answer] += 1
    return distribution


def part1(input):
    return sum(count_unique_yeses(group) for group in parse_groups(input))


def part2(input):
    everyone = 0
    for group in parse_groups(input):
        members = group.count("\n") + 1
        distribution = get_distribution(group)
        for count in distribution.values():
            if count == members:
                everyone += 1
    return everyone


if __name__ == "__main__":
    from aoc2020.common import puzzle_input
    input = puzzle_input.from_arg_file()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
