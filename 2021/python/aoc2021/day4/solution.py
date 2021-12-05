import unittest
from aoc2021.common import puzzle_input
from pprint import pprint


def parse_sequence_and_boards(s):
    lines = s.split("\n")
    sequence = list(map(int, lines[0].split(",")))

    boards = []
    for b in range(2, len(lines), 6):
        board = []
        boards.append(board)
        for i in range(5):
            board_row = []
            board.append(board_row)
            line_no = b + i
            line = lines[line_no]
            number = ""
            for c in line:
                if c != " ":
                    number += c
                else:
                    if number:
                        board_row.append(int(number))
                        number = ""
            if number:
                board_row.append(int(number))

    return sequence, boards


def map_values_to_coordinates(boards):
    nums_to_coords = {}
    for b, board in enumerate(boards):
        for r, row in enumerate(board):
            for c, v in enumerate(row):
                nums_to_coords.setdefault(v, []).append((b, r, c))
    return nums_to_coords


def mark_board(boards, nums_to_coords, v):
    board, row, col = nums_to_coords[v]
    boards[board][row][col] = True


def count_connected_directional(boards, coords, marks, direction=None, length=0):
    board, row, col = coords
    if coords in marks:
        length += 1
        # print(f"            d={direction}, l={length}")
    else:
        # print("            end of line")
        return length

    if direction == 0: # up
        return count_connected_directional(boards, (board, row-1, col), marks, direction=0, length=length)
    elif direction == 1: # right
        return count_connected_directional(boards, (board, row, col+1), marks, direction=1, length=length)
    elif direction == 2: # down
        return count_connected_directional(boards, (board, row+1, col), marks, direction=2, length=length)
    elif direction == 3: # left
        return count_connected_directional(boards, (board, row, col-1), marks, direction=3, length=length)


def count_connected(boards, coords, marks):
    # print(f"        Count connected {coords}")
    board, row, col = coords
    vertical = 1
    horizontal = 1
    vertical += count_connected_directional(boards, (board, row-1, col), marks, direction=0)
    horizontal += count_connected_directional(boards, (board, row, col+1), marks, direction=1)
    vertical += count_connected_directional(boards, (board, row+1, col), marks, direction=2)
    horizontal += count_connected_directional(boards, (board, row, col-1), marks, direction=3)
    return vertical, horizontal


def run_sequence(sequence, nums_to_coords, boards):
    marks = set()
    for i, s in enumerate(sequence):
        # print(f"{i} new number! {s}")
        if s in nums_to_coords:
            for coords in nums_to_coords[s]:
                # print(f"    Found! {coords}")
                marks.add(coords)
                vertical, horizontal = count_connected(boards, coords, marks)
                # print(f"    {vertical}, {horizontal}")
                if vertical > 4 or horizontal > 4:
                    yield s, coords, marks


def part1(data):
    sequence, boards = parse_sequence_and_boards(data)
    nums_to_coords = map_values_to_coordinates(boards)

    for win in run_sequence(sequence, nums_to_coords, boards):
        last_sequence_n, last_coords, marks = win
        break

    sum_unmarked = 0
    board = last_coords[0]
    for r, row in enumerate(boards[board]):
        for c, col in enumerate(row):
            if (board, r, c) not in marks:
                sum_unmarked += col
    return sum_unmarked * last_sequence_n


def part2(data):
    sequence, boards = parse_sequence_and_boards(data)
    nums_to_coords = map_values_to_coordinates(boards)
    print(f"There are {len(boards)} boards")
    won = set()
    wins = {}
    for win in run_sequence(sequence, nums_to_coords, boards):
        last_sequence_n, last_coords, marks = win
        board = last_coords[0]
        if board not in wins:
            sum_unmarked = 0
            for r, row in enumerate(boards[board]):
                for c, col in enumerate(row):
                    if (board, r, c) not in marks:
                        sum_unmarked += col
            wins[board] = sum_unmarked * last_sequence_n
    print(wins)


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        example = self.examples[0]
        part1(example)
        # self.assertEqual(0, solution.part1(self.examples[0]))
        pass


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
