from aoc2020.common import puzzle_input
# from . import solution
import re


def byr(value):
    return 1920 <= int(value) <= 2002


def iyr(value):
    return 2010 <= int(value) <= 2020


def eyr(value):
    return 2020 <= int(value) <= 2030


def hgt(value):
    if len(value) > 2:
        if "cm" in value and value[-2:] == "cm":
            height = int(value[:-2])
            return 150 <= height <= 193
        elif "in" in value and value[-2:] == "in":
            height = int(value[:-2])
            return 59 <= int(value[:-2]) <= 76
    return False


def hcl(value):
    if len(value) == 7 and value[0] == "#":
        color = value[1:]
        try:
            int(color, 16)
            return True
        except ValueError:
            return False


def ecl(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def pid(value):
    return len(value) == 9 and value.isnumeric()


expected_fields = {
    "byr": byr,
    "iyr": iyr,
    "eyr": eyr,
    "hgt": hgt,
    "hcl": hcl,
    "ecl": ecl,
    "pid": pid,
    # "cid",
}

data = {}

if __name__ == "__main__":
    input = puzzle_input.from_arg_file()
    # input = puzzle_input.from_example(__file__, 3)
    passports = input.split("\n\n")

    valid = 0
    for passport in passports:
        pairs = re.split(r"\s", passport)

        entry = {}
        for pair in pairs:
            key, value = pair.split(":")
            entry[key] = value

        valid_entry = True
        for expected_field in expected_fields:
            validator = expected_fields[expected_field]
            print(expected_field, validator)
            if expected_field not in entry:
                print(expected_field, "fail")
                valid_entry = False
                break
            else:
                if not validator(entry[expected_field]):
                    print(expected_field, "fail")
                    valid_entry = False

        if valid_entry:
            valid += 1

    print(valid)

    # re.findall(r"")
    print("Part 1:", )
    print("Part 2:", )
