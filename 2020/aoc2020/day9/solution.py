from itertools import combinations


def verify_preambles(size, data):
    preamble = []
    for i, number in enumerate(data):
        if i < size:
            preamble.append(number)
        else:
            numbers_sum_2_of_preamble = []
            for combination in combinations(preamble, 2):
                numbers_sum_2_of_preamble.append(sum(combination) == number)
            if not any(numbers_sum_2_of_preamble):
                return number
            preamble.pop(0)
            preamble.append(number)


def part1(size, input):
    input = list(map(int, input.splitlines()))
    result = verify_preambles(size, input)
    return result


def part2(size, input):
    invalid = part1(size, input)
    input = list(map(int, input.splitlines()))
    invalid_index = input.index(invalid)

    for offset in range(0, invalid_index):
        for size in range(2, invalid_index-offset):
            r = input[offset:offset+size]
            if sum(r) == invalid:
                return min(r) + max(r)


if __name__ == "__main__":
    from aoc2020.common import puzzle_input
    input = puzzle_input.from_arg_file()

    print("Part 1:", part1(25, input))
    print("Part 2:", part2(25, input))
