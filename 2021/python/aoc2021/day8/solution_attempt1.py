import unittest
from aoc2021.common import puzzle_input


def parse_input(s):
    s = s.replace("|\n", "| ")
    entries = []
    for line in s.split("\n"):
        # print(line)
        ten_combos_str, four_combo_str = line.split(" | ")
        ten_combo = list(map(lambda j: "".join(j), map(sorted, ten_combos_str.split(" "))))
        four_combo = list(map(lambda j: "".join(j), map(sorted, four_combo_str.split(" "))))
        entry = ten_combo, four_combo
        entries.append(entry)
    return entries


digit_to_segment_count = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}


segment_count_to_digits = {}
for k, v in digit_to_segment_count.items():
    if v not in segment_count_to_digits:
        segment_count_to_digits[v] = [k]
    else:
        segment_count_to_digits[v].append(k)


def map_segment_count_to_combo(combos):
    lens_to_combo = {}
    for combo in combos:
        l = len(combo)
        if l not in lens_to_combo:
            lens_to_combo[l] = [combo]
        else:
            lens_to_combo[l].append(combo)
    return lens_to_combo


def part1(data):
    entries = parse_input(data)
    count = 0
    for entry in entries:
        ten_combo, four_combo = entry
        # print(ten_combo, four_combo)
        lens_to_combo = map_segment_count_to_combo(ten_combo)
        # print(lens_to_combo)

        combo_to_digit = {}
        for segment_count, digits in segment_count_to_digits.items():
            if len(digits) == 1:
                digit = digits[0]
                if segment_count in lens_to_combo:
                    combo = lens_to_combo[segment_count][0]
                    # print(combo)
                    combo_to_digit[combo] = digit

        for combo in four_combo:
            if combo in combo_to_digit:
                count += 1

    return count


# segment default positions
#  000
# 1   2
# 1   2
# 1   2
#  333
# 4   5
# 4   5
# 4   5
#  666
segment_to_digits = {
    0: {0, 2, 3, 5, 6, 7, 8, 9},
    1: {0, 4, 5, 6, 8, 9},
    2: {0, 1, 2, 3, 4, 7, 8, 9},
    3: {2, 3, 4, 5, 6, 8, 9},
    4: {0, 2, 6, 8},
    5: {0, 1, 3, 4, 5, 6, 7, 8, 9},
    6: {0, 2, 3, 5, 6, 8, 9}
}

digit_to_segments = dict()
for k, v in segment_to_digits.items():
    for digit in v:
        if digit not in digit_to_segments:
            digit_to_segments[digit] = set([k])
        else:
            digit_to_segments[digit].add(k)


def map_combos_to_suspect_digits(combos):
    combos_to_suspects = dict()
    for combo in combos:
        combos_to_suspects[combo] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    return combos_to_suspects


start_with_counts = set()
for count, digits in segment_count_to_digits.items():
    if len(digits) == 1:
        start_with_counts.add(count)


def part2(data):
    entries = parse_input(data)
    print(1)
    for entry in entries:
        print(2)
        resolved_digits_to_segments = {}
        resolved_combos_to_digits = {}
        resolved_digits_to_combos = {}

        ten_combo, four_combo = entry
        combo_to_suspect_digits = map_combos_to_suspect_digits(ten_combo)
        lens_to_combo = map_segment_count_to_combo(ten_combo)
        # start with what we know,  1, 4, 7, 8
        for count in start_with_counts:
            combo = lens_to_combo[count][0]
            digit = segment_count_to_digits[count][0]
            resolved_combos_to_digits[combo] = digit
            resolved_digits_to_combos[digit] = combo
            print(combo, count, digit)

        print(resolved_digits_to_combos)

        resolved_wire_to_segment = {}

        # 1, 7 = identify 0
        print(3)
        print(digit_to_segments)
        combo1 = resolved_digits_to_combos[1]
        combo7 = resolved_digits_to_combos[7]
        diff = set(combo7).difference(set(combo1))
        resolved_wire_to_segment[diff] = 0



        print(combo7, combo1, diff)
        resol


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example2(self):
        example = self.examples[1]
        self.assertEqual(26, part1(example))

    def test2_part2_example1(self):
        example = self.examples[0]
        self.assertEqual(0, part2(example))


if __name__ == "__main__":
    unittest.main()
    data = puzzle_input.from_arg_file()
    # print("Part 1:", part1(data))
    # print("Part 2:", part2(data))
