import unittest
from aoc2021.common import puzzle_input

# example 7 segment display default wires
#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg


digits_to_segments = {
    0: {0, 1, 2, 4, 5, 6},
    1: {2, 5},
    2: {0, 2, 3, 4, 6},
    3: {0, 2, 3, 5, 6},
    4: {1, 2, 3, 5},
    5: {0, 1, 3, 5, 6},
    6: {0, 1, 3, 4, 5, 6},
    7: {0, 2, 5},
    8: {0, 1, 2, 3, 4, 5, 6},
    9: {0, 1, 2, 3, 5, 6}
}

segments_to_digits = {}
for digit, segments in digits_to_segments.items():
    for segment in segments:
        segments_to_digits.setdefault(segment, set()).add(digit)

digits_to_len = {}
for digit, segments in digits_to_segments.items():
    digits_to_len[digit] = len(segments)

len_to_digits = {}
for digit, segment_count in digits_to_len.items():
    len_to_digits.setdefault(segment_count, set()).add(digit)

def parse_entries(data):
    data = data.replace(" |\n", " ")
    entries = []
    for line in data.splitlines():
        words = line.split(" ")
        combos = [set(combo) for combo in words[:10]]
        decode_combos = [set(combo) for combo in words[-4:]]
        entry = combos, decode_combos
        entries.append(entry)
    return entries


def part1(data):
    entries = parse_entries(data)
    count = 0
    for entry in entries:
        combos, decode_combos = entry
        for combo in decode_combos:
            l = len(combo)
            digits = len_to_digits[l]
            if len(digits) == 1:
                count += 1
    return count


def part2(data):
    entries = parse_entries(data)
    count = 0
    for entry in entries:
        combos, decode_combos = entry
        combos_to_suspected_digits = {}

        digit_to_combo = {}
        len_to_combo = {}

        for combo in combos:
            len_to_combo.setdefault(len(combo), []).append(combo)

        # known lens, giving us: 1, 4, 7, 8
        for l, combos in len_to_combo.items():
            if len(combos) == 1:
                combo ,= combos
                digit ,= len_to_digits[len(combo)]
                digit_to_combo[digit] = combo

        # 1, 4, 7, 8

        d = digit_to_combo
        # segments
        s = dict()
        s[0] = d[7].difference(d[1])

        # 6
        for c in len_to_combo[6]:
            if d[8].difference(d[1]).issubset(c):
                d[6] = c
        s[2] = d[8].difference(d[6])

        # 5
        for c in len_to_combo[5]:
            if c.isdisjoint(s[2]):
                d[5] = c

        # 9
        d[9] = d[5].union(s[2])

        # 3
        for c in len_to_combo[5]:
            if d[7].issubset(c):
                d[3] = c

        # 2
        for c in len_to_combo[5]:
            if c not in (d[3], d[5]):
                d[2] = c

        # 0
        s[1] = d[4].difference(d[3])
        s[3] = d[4].difference(d[1]).difference(s[1])
        d[0] = d[8].difference(s[3])

        combo_to_digit = dict()
        for digit, combo in digit_to_combo.items():
            combo_to_digit["".join(sorted(combo))] = digit

        # 1, 3, 4, 5, 6, 7, 8, 9, 0 and 0, 1, 2, 3
        # print(sorted(d), sorted(s))

        readout = ""
        for combo in decode_combos:
            readout += str(combo_to_digit["".join(sorted(combo))])
        # print(readout)
        count += int(readout)
    return count


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    # def test1_part1_example1(self):
    #     example = self.examples[1]
    #     self.assertEqual(0, part1(example))

    def test2_part2_example1(self):
        example = self.examples[1]
        self.assertEqual(61229, part2(example))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
