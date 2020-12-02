from aoc2020.common import puzzle_input
from aoc2020.common import testing
from aoc2020.common.utils import type_per_line


if __name__ == "__main__":
    input = type_per_line(puzzle_input.from_file_arg(), str)

    valid = 0
    for line in input:
        rule, password = line.split(":")

        amount = rule[:-2]
        requirement = rule[-1]
        minimum, maximum = amount.split("-")
        pos1 = int(minimum)
        pos2 = int(maximum)

        p1 = password[pos1] == requirement
        p2 = password[pos2] == requirement

        print(requirement, pos1, pos2, password)
        print(pos1, password[pos1], pos2, password[pos2])
        if (p1 and not p2) or (p2 and not p1):
            print("added")
            valid += 1

    print(valid)
