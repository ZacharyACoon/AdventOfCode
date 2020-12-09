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


def part1(input, size=25):
    input = list(map(int, input.splitlines()))
    result = verify_preambles(size, input)
    return result


def part2(input, size=25):
    invalid = part1(input, size)
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

    print("Part 1:", part1(input, 25))
    print("Part 2:", part2(input, 25))
