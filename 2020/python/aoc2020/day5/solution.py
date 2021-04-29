from aoc2020.common import puzzle_input


def vector_row(path):
    offset = 0
    span = 128
    for direction in path:
        if direction == "B":
            offset += span // 2

        span //= 2
    return offset


def vector_column(path):
    offset = 0
    span = 8
    for direction in path:
        if direction == "R":
            offset += span // 2

        span //= 2
    return offset


def calculate_seat_id(row, column):
    return row * 8 + column


def path_to_cartesian(path):
    row = vector_row(path[:7])
    column = vector_column(path[-3:])
    return row, column


def process_path(path):
    return calculate_seat_id(*path_to_cartesian(path))


def part1(input):
    input = input.splitlines()
    return max(map(process_path, input))


def part2(input):
    input = input.splitlines()
    l = sorted(map(process_path, input))  # ordered seat list

    i = 0
    v = l[i]
    while i < len(l):
        if v != l[i]:
            return v
        i += 1
        v += 1


if __name__ == "__main__":
    input = puzzle_input.from_arg_file()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
