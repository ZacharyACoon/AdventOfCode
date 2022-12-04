import unittest
from pathlib import Path
import solution

parent = Path(__file__).parent


class Test(unittest.TestCase):
    with open("example_input1.txt") as f:
        example_input1 = f.read()

    def test1_part1(self):
        output = solution.part1(self.example_input1)
        # assert output ==

    def test2_part2(self):
        output = solution.part2(self.example_input1)
        # assert output ==


if __name__ == "__main__":
    unittest.main()
