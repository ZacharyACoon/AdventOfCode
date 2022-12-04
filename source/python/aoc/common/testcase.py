import unittest
from inspect import stack
from pathlib import Path


class TestCase(unittest.TestCase):
    def __getattr__(self, item):
        if item.startswith("example_input"):
            last_context_filename = stack()[1].filename
            last_context_filepath = Path(last_context_filename)
            last_context_directory = last_context_filepath.parent
            return (last_context_directory / f"{item}.txt").read_text()
