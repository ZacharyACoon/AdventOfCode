from aoc2020.common import testing
from aoc2020.common import puzzle_input
from . import solution


example_input1 = puzzle_input.from_example(__file__, 1).splitlines()


class Test(testing.TimedTestCase):
    def template(self):
        self.assertEqual(0, )
