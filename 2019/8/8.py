import unittest
from aoc_common import puzzle_input
from common.logging import root_logger
import numpy


def parse_input(input_string):
    return [int(s) for s in input_string]


# get a layers object
def parse_layers(data, size_x, size_y):
    layer_size = size_x * size_y
    layers = []
    for layer_start in range(0, len(data), layer_size):
        layer = []
        layer_end = layer_start + layer_size
        for row_start in range(layer_start, layer_end, size_x):
            row_end = row_start + size_x
            row = data[row_start:row_end]
            layer.append(row)
        layers.append(layer)
    return layers


def checksum_layers(layers):
    smallest_layer = None
    smaller_layer_zero_count = float("inf")
    for i in range(len(layers)):
        np_layer = numpy.asarray(layers[i], dtype=numpy.uint8)
        zero_count = numpy.sum(np_layer == 0)
        if zero_count < smaller_layer_zero_count:
            smaller_layer_zero_count = zero_count
            smallest_layer = np_layer

    one_count = numpy.sum(smallest_layer == 1)
    two_count = numpy.sum(smallest_layer == 2)
    checksum = one_count * two_count
    return checksum


def max_blended_layer(layers):
    layers = numpy.asarray(layers, dtype=numpy.uint8)
    a = layers[layers != 2]
    numpy.ufunc.reduce(a, axis=0, )
    print(a)


class ImageDecodeTest(unittest.TestCase):
    def test_day8_part1_example1(self):
        data = parse_input("123456789012")
        layers = parse_layers(data, 3, 2)
        expected_result = [
            [[1,2,3], [4,5,6]],
            [[7,8,9], [0,1,2]]
        ]
        self.assertListEqual(layers, expected_result)

    def test_day8_part2_example1(self):
        data = parse_input("0222112222120000")
        layers = parse_layers(data, 2, 2)
        expected_result = [
            [[0, 2],
            [2, 2]],
            [[1, 1],
             [2, 2]],
            [[2, 2],
            [1, 2]],
            [[0, 0],
            [0, 0]]
        ]
        self.assertListEqual(layers, expected_result)

        expected_result = [
            [0, 1],
            [1, 0]
        ]
        max_blended_layer(layers)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=0)
    answer = checksum_layers(parse_layers(parse_input(puzzle_input), 25, 6))
    root_logger.info(f"Part One = {answer}")
