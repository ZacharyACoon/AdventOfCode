import string


def parse_groups(input):
    for group in input.split("\n\n"):
        yield group


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
    yeses = 0
    for group in parse_groups(input):
        letters = group.replace(" ", "").replace("\n", "")
        yeses += len(set(letters))

    return yeses


def part2(input):
    groups = parse_groups(input)

    everyone = 0
    for group in groups:
        count = group.count("\n") + 1
        print(group, count)
        distribution = get_distribution(group)
        print(distribution)
        for answer in distribution:
            if distribution[answer] == count:
                everyone += 1
                print("everyone!")
    return everyone


if __name__ == "__main__":
    from aoc2020.common import puzzle_input
    input = puzzle_input.from_arg_file()
#     input = """\
# abc
#
# a
# b
# c
#
# ab
# ac
#
# a
# a
# a
# a
#
# b"""

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
