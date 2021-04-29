from common.logging import log
from aoc_common import puzzle_input, TimedTestCase, Timer
import unittest
from itertools import zip_longest


base_pattern = [0, 1, 0, -1]


def pattern(scale, i):
    index = (i+1) // scale % 4
    return base_pattern[index]


def generate_sum_array(input_data):
    sum_array = []
    s = 0
    for v in input_data:
        s += v
        sum_array.append(s)
    return sum_array


def phase(input_data):
    output_data = input_data.copy()
    sum_array = generate_sum_array(input_data)
    l = len(input_data)
    for offset in range(l):
        scale = offset + 1
        s = 0

        for span_start in range(offset, l, scale):
            span_end = min(l-1, span_start + offset)
            if scale == 1:
                span_sum = input_data[span_start]
            else:
                span_sum = sum_array[span_end] - sum_array[span_start - 1]
            p = base_pattern[(span_start + 1) // scale % 4]
            n = span_sum * p
            s += n
            # print(f"start={span_start}, stop={span_end}, span_sum={span_sum}, p={p}, n={n}, sum={s}")
        v = abs(s) % 10
        output_data[offset] = v
    return output_data


def phase_count(data, n=1):
    with Timer() as t:
        for i in range(n):
            data = phase(data)
            t.click()
            if t.time_for_report():
                log.debug(f"{i+1}/{n}, "
                          f"ETA: {t.eta(n)}")
    return data


def parse_input(data: str):
    return list(map(int, list(data)))


def parse_output(data):
    return ''.join(map(str, data))


class TestPhasing(TimedTestCase):
    def _test_part1_phase_rounds_output(self, data, n, expected):
        data = parse_input(data)
        data = phase_count(data, n)
        data = parse_output(data)[:8]
        self.assertEqual(data, expected)

    def test_part1_example1_phase1(self):
        self._test_part1_phase_rounds_output(
            "12345678",
            1,
            "48226158"
        )

    def test_part1_example1_phase2(self):
        self._test_part1_phase_rounds_output(
            "12345678",
            2,
            "34040438"
        )

    def test_part1_example1_phase3(self):
        self._test_part1_phase_rounds_output(
            "12345678",
            3,
            "03415518"
        )

    def test_part1_example1_phase4(self):
        self._test_part1_phase_rounds_output(
            "12345678",
            4,
            "01029498"
        )

    def test_part1_example_2(self):
        self._test_part1_phase_rounds_output(
            "80871224585914546619083218645595",
            100,
            "24176176"
        )

    def test_part1_example_3(self):
        self._test_part1_phase_rounds_output(
            "19617804207202209144916044189917",
            100,
            "73745418"
        )

    def test_part1_example_4(self):
        self._test_part1_phase_rounds_output(
            "69317163492948606335995924319873",
            100,
            "52432133"
        )

    def _test_part2_phase_rounds_output(self, data, n, expected):
        message_offset = int(data[:7])
        data = parse_input(data)
        data = phase_count(data, n)
        data = parse_output(data)
        message = data[message_offset:message_offset+8]
        self.assertEqual(message, expected)

    def test_part2_example1(self):
        self._test_part2_phase_rounds_output(
            "03036732577212944063491565474664" * 10000,
            100,
            "84462026"
        )


if __name__ == "__main__":
    # unittest.main(defaultTest="TestPhasing", exit=False, verbosity=0)

    # part 1
    try:
        with Timer() as t:
            answer = parse_output(phase_count(parse_input(puzzle_input), 100))
            log.info(f"Part One = {answer}")
    finally:
        log.info(f"It took {t.interval} seconds.")

    # part 1
    try:
        with Timer() as t:
            data = puzzle_input * 10000
            message_offset = int(data[:7])
            data = parse_input(data)
            data = phase_count(data, 100)
            data = parse_output(data)
            message = data[message_offset:message_offset+8]
            log.info(f"Part Two = {message}")
    finally:
        log.info(f"It took {t.interval} seconds.")

# 18:28:43
# 18:30:00