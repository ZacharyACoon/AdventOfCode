"""
rules
    seat empty L and no adjacent, becomes occupied
    seat occupied # and 4+ seats adjacent, becomes empty
    else: no change
    adjacent means 8 spaces around
"""
from pprint import pprint
raw_input = input


def detect_width(input):
    return len(input.splitlines()[0]) + 1


def determine_adjacency_offsets(width):
    return [
        -width-1,
        -width,
        -width+1,
        -1,
        1,
        width-1,
        width,
        width+1,
    ]


def count_adjacencies_filled(seats, adjacency_offsets, offset):
    filled = 0
    for adjacency_offset in adjacency_offsets:
        seat = offset + adjacency_offset
        if 0 <= seat < len(seats):
            if seats[seat] == "#":
                filled += 1
    return filled


def flip_seats(seats, adjacency_offsets):
    new_seats = seats.copy()
    changes = 0
    for offset, seat in enumerate(seats):
        # filled = count_adjacencies_filled(seats, adjacency_offsets, offset)
        # print(offset, seat.replace("\n", "n"), filled)
        if seat == "L" and count_adjacencies_filled(seats, adjacency_offsets, offset) == 0:
            new_seats[offset] = "#"
            changes += 1
        elif seat == "#" and count_adjacencies_filled(seats, adjacency_offsets, offset) > 3:
            new_seats[offset] = "L"
            changes += 1
    return new_seats, changes


def scan_direction(adjacency_offsets, offset, direction):
    distance = 1
    while True:
        yield offset + adjacency_offsets[direction] * distance
        distance += 1


def count_deep_adjacencies(seats, adjacency_offsets, offset, width):
    filled = 0
    for direction in range(8):
        for adjacency in scan_direction(adjacency_offsets, offset, direction):
            # print(adjacency)
            if adjacency > 0 and adjacency % width == width - 1:
                # print(adjacency, "direction edge", direction)
                break
            if 0 <= adjacency < len(seats):
                if seats[adjacency] == "#":
                    # print(f"direction {direction} filled")
                    filled += 1
                    break
                elif seats[adjacency] == "L":
                    # print(f"direction {direction} empty")
                    break
            else:
                break
    # print(f"{filled} filled")
    return filled


def flip_seats2(seats, adjacency_offsets, width):
    new_seats = seats.copy()
    changes = 0
    for offset, seat in enumerate(seats):
        # if offset % width == 0:
            # print(seats[offset:offset + width - 1])
        # print(offset, seat.replace("\n", "n"))
        if seat == "L" and count_deep_adjacencies(seats, adjacency_offsets, offset, width) == 0:
            new_seats[offset] = "#"
            changes += 1
        elif seat == "#" and count_deep_adjacencies(seats, adjacency_offsets, offset, width) > 4:
            new_seats[offset] = "L"
            changes += 1
    return new_seats, changes


def part1(input):
    width = detect_width(input)
    adjacency_offsets = determine_adjacency_offsets(width)
    seats = list(input)
    while True:
        seats, changes = flip_seats(seats, adjacency_offsets)
        # print()
        # print("".join(seats))
        if not changes:
            break
    # print("done")
    # print("".join(seats))
    return seats.count("#")


def part2(input):
    width = detect_width(input)
    # print(width)
    adjacency_offsets = determine_adjacency_offsets(width)
    seats = list(input)
    # print("".join(seats))
    flips = 0
    while True:
        seats, changes = flip_seats2(seats, adjacency_offsets, width)
        flips += 1
        # print(flips)
        # print()
        # print("".join(seats))
        # raw_input("...")
        if not changes:
            break
    return seats, seats.count("#")


if __name__ == "__main__":
    from aoc2020.common import puzzle_input
    input = puzzle_input.from_arg_file()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input)[1])
