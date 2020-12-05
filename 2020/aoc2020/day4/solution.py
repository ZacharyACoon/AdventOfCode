from aoc2020.common import puzzle_input
import re


def partition_entries(lines):
    for entry in re.finditer(r"(\S+(?:\s\S+)*)", lines):
        yield entry.group(0)


def parse_entry(entry):
    for pair in re.finditer(r"(\w+):(\S+)", entry):
        yield pair.groups()


def validate_hgt(value):
    if "cm" in value and value[-2:] == "cm":
        return 150 <= int(value[:-2]) <= 193
    elif "in" in value and value[-2:] == "in":
        return 59 <= int(value[:-2]) <= 76


def validate_hcl(value):
    if len(value) == 7 and value[0] == "#":
        try:
            int(value[1:], 16)
            return True
        except ValueError:
            return False


validators = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9 and x.isnumeric()
}


def validate_entry1(entry):
    required_validations = validators.copy()
    for key, value in parse_entry(entry):
        if key in required_validations:
            del required_validations[key]
    return not bool(required_validations)


def validate_entry2(entry):
    required_validations = validators.copy()
    for key, value in parse_entry(entry):
        if key in required_validations:
            result = required_validations[key](value)
            if result:
                del required_validations[key]
            else:
                return False
    return not bool(required_validations)


def solve1(input):
    entries = partition_entries(input)
    return sum(map(validate_entry1, entries))


def solve2(input):
    entries = partition_entries(input)
    return sum(map(validate_entry2, entries))


if __name__ == "__main__":
    input = puzzle_input.from_arg_file()

    print("Part 1:", solve1(input))
    print("Part 2:", solve2(input))
