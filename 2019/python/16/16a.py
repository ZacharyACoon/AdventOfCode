from common.logging import log
from aoc_common import puzzle_input, TimedTestCase, Timer, human_time_interval
import unittest

base_pattern = [0, 1, 0, -1]


def pattern(scale, i):
    index = i // scale % 4
    return base_pattern[index]


def phase(input_data):
    output_length = len(input_data)
    output_data = [0 for _ in range(output_length)]

    with Timer() as at:
        for a in range(output_length):
            build = [0 for _ in range(output_length)]
            for b in range(output_length):
                v = input_data[b]
                p = pattern(b+1, a+1)
                build[b] = v * p
                b += 1
            output_data[a] = abs(sum(build)) % 10
            a += 1
            at.click()
            if at.time_for_report():
                log.debug(f"{a+1}/{output_length}, "
                          f"Average: {at.average_per_lap():.2f} seconds, "
                          f"ETA: {at.human_eta(output_length - a)}, "
                          f"Average {at.average_per_second():.2f} per second.")

    return output_data


def phase_count(data, n=1):
    with Timer() as t:
        for i in range(n):
            data = phase(data)
            t.click()
            if t.time_for_report():
                log.debug(f"{i+1}/{n}, Average: {t.average_per_lap():.2f} seconds, ETA: {t.eta(n - i):.2f} seconds, Average {t.average_per_second():.2f} per second.")
    return data


def parse_input(data: str):
    return list(map(int, list(data)))


def parse_output(data):
    return ''.join(map(str, data[:8]))


class TestPhasing(TimedTestCase):
    def _test_phase_rounds_output(self, data, n, expected):
        data = parse_input(data)
        data = phase_count(data, n)
        data = parse_output(data)
        self.assertEqual(data, expected)

    def test_part1_example1_phase1(self):
        self._test_phase_rounds_output(
            "12345678",
            1,
            "48226158"
        )

    def test_part1_example1_phase2(self):
        self._test_phase_rounds_output(
            "12345678",
            2,
            "34040438"
        )

    def test_part1_example1_phase3(self):
        self._test_phase_rounds_output(
            "12345678",
            3,
            "03415518"
        )

    def test_part1_example1_phase4(self):
        self._test_phase_rounds_output(
            "12345678",
            4,
            "01029498"
        )

    def test_part1_example_2(self):
        self._test_phase_rounds_output(
            "80871224585914546619083218645595",
            100,
            "24176176"
        )

    def test_part1_example_3(self):
        self._test_phase_rounds_output(
            "19617804207202209144916044189917",
            100,
            "73745418"
        )

    def test_part1_example_4(self):
        self._test_phase_rounds_output(
            "69317163492948606335995924319873",
            100,
            "52432133"
        )

    def test_part2_example1(self):
        self._test_phase_rounds_output(
            "03036732577212944063491565474664" * 10000,
            100,
            "84462026"
        )

    def test_part2_example2(self):
        self._test_phase_rounds_output(
            "02935109699940807407585447034323" * 10000,
            100,
            "78725270"
        )

    def test_part2_example3(self):
        self._test_phase_rounds_output(
            "03081770884921959731165446850517" * 10000,
            100,
            "53553731"
        )


if __name__ == "__main__":
    unittest.main(defaultTest="TestPhasing", exit=False, verbosity=0)

    # part 1
    try:
        with Timer() as t:
            answer = parse_output(phase_count(parse_input(puzzle_input), 100))
            log.info(f"Part One, 100 Phases = {answer}")
    finally:
        log.info(f"It took {t} seconds.")

    # part 2
    # real_signal = parse_input(puzzle_input) * 10000

    #
    # part 2
    # answer = determine_shortest_length_to_intersection(paths)
    # log.info(f"Part Two, Shortest Wire Length to Intersection = {answer}")
