import re
from aoc2020.common.utils import type_per_line


def parse(line):
    return re.split(r"-|: | ", line)


def validate_password1(a, b, char, password):
    return int(a) <= password.count(char) <= int(b)


def validate_password2(a, b, char, password):
    pos1 = password[int(a) - 1] == char
    pos2 = password[int(b) - 1] == char
    return pos1 ^ pos2


def count_valid(validator, lines):
    return sum(validator(*x) for x in lines)


def solve1(input):
    input = type_per_line(input, parse)
    return count_valid(validate_password1, input)


def solve2(input):
    input = type_per_line(input, parse)
    return count_valid(validate_password2, input)


if __name__ == "__main__":
    from aoc2020.common import puzzle_input
    input = puzzle_input.from_arg_file()

    print("Part 1:", solve1(input))
    print("Part 2:", solve2(input))
