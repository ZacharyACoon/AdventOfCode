from aoc2020.common import puzzle_input


def part1(input):
    for letters in input:
        row = letters[:7]

        min_row = 0
        max_row = 127
        for letter in row:
            half = (max_row - min_row + 1) // 2
            if letter == "F":
                max_row -= half
            else:
                min_row += half

        seat = letters[-3:]
        min_seat = 0
        max_seat = 7
        for letter in seat:
            half = (max_seat - min_seat + 1) // 2
            if letter == "R":
                min_seat += half
            else:
                max_seat -= half
        seatid = min_row*8+min_seat
        yield seatid


def part2(input):
    l = sorted(part1(input))
    i = 0
    v = 21
    while True:
        if l[i] != v:
            print(v)
            break




if __name__ == "__main__":
    input = puzzle_input.from_arg_file().splitlines()
    # input = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


    # print("Part 1:", max(part1(input)))
    print("Part 2:", part2(input))
