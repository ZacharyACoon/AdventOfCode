from aoc2020.common import testing
from aoc2020.common import puzzle_input
from . import solution


class Test(testing.TimedTestCase):
    def test_part1_example1(self):
        example_input1 = puzzle_input.from_example(__file__, 1)  # 2/4 fail
        entries = solution.partition_entries(example_input1)
        self.assertEqual(2, sum(map(solution.validate_entry1, entries)))

    def test_part2_example2(self):
        example_input2 = puzzle_input.from_example(__file__, 2)  # all fail
        entries = solution.partition_entries(example_input2)
        self.assertFalse(all(map(solution.validate_entry2, entries)))

    def test_part2_example3(self):
        example_input2 = puzzle_input.from_example(__file__, 3)  # all pass
        entries = solution.partition_entries(example_input2)
        self.assertTrue(all(map(solution.validate_entry2, entries)))
