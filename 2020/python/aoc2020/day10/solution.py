"""
output joltage
# 1,2,3
required-3 <= jolts <= maximum

device_can_handle = max(adapter) + 3

charging outlet = 0

every adapter at once
"""
import math


def get_distribution(adapters):
    built_in = max(adapters) + 3
    adapters = [0] + list(sorted(adapters)) + [built_in]
    differences = {}
    for i in range(0, len(adapters)-1):
        difference = adapters[i+1] - adapters[i]
        if not difference in differences:
            differences[difference] = 1
        else:
            differences[difference] += 1
    return differences


def validate_configuration(adapters):
    last = None
    for adapter in adapters:
        if last is None:
            last = adapter
        else:
            if not last < adapter <= last + 3:
                return False
            else:
                last = adapter
    return True


def count_full_paths(adapters, m, cache=None, offset=0):
    if cache is None:
        cache = {}

    if offset < len(adapters) - 1:
        count = 0
        for candidate in m[offset]:
            if candidate not in cache:
                cache[candidate] = count_full_paths(adapters, m, cache, candidate)
            count += cache[candidate]
        return count
    else:
        return 1


def find_next_step_candidates(last, adapters, offset=0):
    maximum = last + 3
    if offset >= len(adapters):
        yield True

    while offset < len(adapters):
        adapter = adapters[offset]
        offset += 1
        if adapter <= maximum:
            yield from find_next_step_candidates(adapter, adapters, offset)
        else:
            break


def recurse_possible_paths(path, adapters, offset=0):
    last = path[-1]
    if offset < len(adapters):
        while offset < len(adapters):
            adapter = adapters[offset]
            if last < adapter <= last + 3:
                yield from recurse_possible_paths(path.copy() + [adapter], adapters, offset + 1)
            else:
                break
            offset += 1
        else:
            yield path


def map_next_offsets(adapters):
    a = 0
    next_offsets = {}
    while a < len(adapters) - 1:
        last = adapters[a]
        next_offsets[a] = []
        b = a + 1
        while b < len(adapters):
            candidate = adapters[b]
            if candidate <= last + 3:
                next_offsets[a].append(b)
            else:
                break
            b += 1
        a += 1
    return next_offsets


def multiply_options(m, last=0, count=0):
    if last in m:
        for option in m[last]:
            return multiply_options(m, last=option, count=count)
    return count


def part1(input):
    input = list(map(int, input.splitlines()))
    distribution = get_distribution(input)
    return distribution[1] * distribution[3]


def part2(input):
    input = list(map(int, input.splitlines()))
    adapters = [0] + list(sorted(input)) + [max(input) + 3]
    offset_map = map_next_offsets(adapters)
    return count_full_paths(adapters, offset_map)


if __name__ == "__main__":
    from aoc2020.common import puzzle_input
    input = puzzle_input.from_arg_file()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
