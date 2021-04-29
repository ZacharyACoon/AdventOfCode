import unittest
import time
import logging


class TimedTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = self.__class__.__name__
        self.log = logging.getLogger(self.name)

    def setUp(self) -> None:
        self.log = logging.getLogger(self.name).getChild(self._testMethodName)
        self.start_time = time.time()

    def tearDown(self) -> None:
        self.log.debug(f"{time.time() - self.start_time:.8f} seconds.")