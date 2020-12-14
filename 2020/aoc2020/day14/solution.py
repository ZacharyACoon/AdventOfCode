import unittest
from aoc2020.common import puzzle_input
from aoc2020.common.testing import TimedTestCase
from aoc2020.common.solution import Solution
import re
from itertools import combinations_with_replacement


def parse_instructions(input):
    regex = r"mask = ([X01]+)|mem\[(\d+)\] = (\d+)"
    for mask, address, value in re.findall(regex, input):
        if address:
            address = int(address)
            value = int(value)
        yield mask, address, value


def mask_to_map(mask):
    mask_map = {}
    for i, bit in enumerate(mask):
        if bit not in mask_map:
            mask_map[bit] = [i]
        else:
            mask_map[bit].append(i)
    return mask_map


def value_to_bitsring(value):
    return "{0:b}".format(value).zfill(36)


class Solution(Solution):
    def part1(self, input):
        memory = {}
        # mask_map = mask_to_map(mask)
        for mask, address, value in parse_instructions(input):
            if mask:
                mask_map = mask_to_map(mask)
            else:
                bitstring = list(value_to_bitsring(value))
                for bit, positions in mask_map.items():
                    if bit == "X":
                        continue
                    for position in positions:
                        bitstring[position] = bit
                value = int("".join(bitstring), 2)
                memory[address] = value
        return sum(memory.values())

    def part2(self, input):
        memory = {}
        mask_map = {}
        for mask, address, value in parse_instructions(input):
            if mask:
                mask_map = mask_to_map(mask)
            else:
                address_bits = list(value_to_bitsring(address))
                if "1" in mask_map:
                    for position in mask_map["1"]:
                        address_bits[position] = "1"
                if "X" in mask_map:
                    positions = mask_map["X"]
                    addresses = []
                    for combination in range(2**len(positions)):
                        floating_mask = list("{0:b}".format(combination).zfill(len(positions)))
                        address_bits_copy = address_bits.copy()
                        for i, bit in enumerate(floating_mask):
                            address_bits_copy[positions[i]] = bit
                        addresses.append(int("".join(address_bits_copy), 2))
                    for address in addresses:
                        memory[address] = value
        return sum(memory.values())


class Test(TimedTestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        self.assertEqual(165, Solution().part1(self.examples[0]))

    def test2_part2_example2(self):
        self.assertEqual(208, Solution().part2(self.examples[1]))


if __name__ == "__main__":
    # unittest.main()
    input = puzzle_input.from_arg_file()

    solution = Solution()
    print("Part 1:", solution.part1(input))
    print("Part 2:", solution.part2(input))
