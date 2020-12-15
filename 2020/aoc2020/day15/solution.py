import unittest
from aoc2020.common import puzzle_input
from aoc2020.common.testing import TimedTestCase
from aoc2020.common.solution import Solution


def parse_input(input):
    return [int(i) for i in input.split(",")]


class Solution(Solution):
    def part1(self, input):
        input = parse_input(input)
        spoken = {}
        turn = 0
        last = 0
        while turn < 2020:
            if turn < len(input):
                number = input[turn]
            else:
                number = last

            if number in spoken:
                if len(spoken[number]) == 1:
                    number = 0
                else:
                    turns = spoken[number]
                    number = turns[-1] - turns[-2]

            if number not in spoken:
                spoken[number] = [turn]
            else:
                spoken[number].append(turn)

            last = number
            turn += 1
        return last

    def part2(self, input, turns=30000000):
        input = parse_input(input)
        spoken = {}
        number = 0
        spoken.update((value, [i]) for i, value in enumerate(input))
        for turn in range(len(input), turns):
            if number in spoken:
                when = spoken[number]
                if len(when) == 1:
                    number = 0
                else:
                    number = when[-1] - when[-2]

            if number not in spoken:
                spoken[number] = [turn]
            else:
                spoken[number].append(turn)

        return number


class Test(TimedTestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    # def test1_part1_example1(self):
    #     self.assertEqual(436, Solution().part1("0,3,6"))

    def test2_part2_example1(self):
        self.assertEqual(436, Solution().part2("0,3,6", 2020))

    def test3_part2_example2(self):
        self.assertEqual(175594, Solution().part2("0,3,6", 30000000))


if __name__ == "__main__":
    # unittest.main()
    input = puzzle_input.from_arg_file()
    print(input)
    solution = Solution()
    print("Part 1:", solution.part1(input))
    print("Part 2:", solution.part2(input))
