from aoc.common.testcase import TestCase
from . import solution


class Test(TestCase):
    def test1_part1(self):
        output = solution.part1(self.example_input1)
        print(output)
        assert output == "CMZ"

    def test2_part2(self):
        output = solution.part2(self.example_input1)
        assert output == "MCD"
