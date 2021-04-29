import unittest
from aoc2020.common import puzzle_input
from aoc2020.common.testing import TimedTestCase
from aoc2020.common.solution import Solution


def parse_input(input):
    return [int(i) for i in input.split(",")]


def van_eck_sequence(start_numbers=None, turns=2020):
    spoken = {}
    if start_numbers:
        spoken.update((number, [offset]) for offset, number in enumerate(start_numbers))

    number = list(spoken.keys())[-1]
    for turn in range(len(spoken), turns):
        if number in spoken:
            previous_utterance_turn = spoken[number]
            if len(previous_utterance_turn) == 1:
                number = 0
            else:
                number = previous_utterance_turn[-1] - previous_utterance_turn[-2]

        if number not in spoken:
            spoken[number] = [turn]
        else:
            spoken[number].append(turn)

    return number


class Solution(Solution):
    def part1(self, input):
        input = parse_input(input)
        return van_eck_sequence(input, 2020)

    def part2(self, input):
        input = parse_input(input)
        return van_eck_sequence(input, 30000000)


class Test(TimedTestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        self.assertEqual(436, Solution().part1("0,3,6"))

    def test2_part2_example1(self):
        self.assertEqual(175594, Solution().part2("0,3,6"))


if __name__ == "__main__":
    # unittest.main()
    input = puzzle_input.from_arg_file()
    print("Part 1:", Solution().part1(input))
    print("Part 2:", Solution().part2(input))
