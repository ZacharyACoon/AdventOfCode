import unittest
from pathlib import Path
import solution

parent = Path(__file__).parent


class Test(unittest.TestCase):
    with open("example_input1.txt") as f:
        example_input1 = f.read()

    def test1_part1(self):
        output = solution.part1(self.example_input1)
        assert output == 24000

    def test2_part2(self):
        output = solution.part2(self.example_input1)
        assert output == 45000


if __name__ == "__main__":
    unittest.main()
