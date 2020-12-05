from aoc2020.common import testing
from . import solution


class Test(testing.TimedTestCase):
    def test_part1_paths(self):
        def values(input):
            row, column = solution.path_to_cartesian(input)
            seat_id = solution.calculate_seat_id(row, column)
            return row, column, seat_id

        self.assertEqual(values("BFFFBBFRRR"), (70, 7, 567))
        self.assertEqual(values("FFFBBBFRRR"), (14, 7, 119))
        self.assertEqual(values("BBFFBBFRLL"), (102, 4, 820))
