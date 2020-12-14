from unittest import TestCase
import time


class TimedTestCase(TestCase):

    def setUp(self) -> None:
        self._start = time.time()

    def tearDown(self) -> None:
        self._finish = time.time()
        self._elapsed = self._finish - self._start
        print(self.id(), f"{self._elapsed:.8f}")
