import unittest
from aoc2021.common import puzzle_input


def parse(data):
    nodes = dict()

    lines = data.strip().splitlines()
    for line in lines:
        a, b = line.split("-")
        nodes.setdefault(a, set()).add(b)
        nodes.setdefault(b, set()).add(a)
    return nodes


def find_paths1(nodes, position="start", visited=None, path=None, paths=None):
    # can visit a small cave (lowercase) ONCE
    # can visit a large cave (uppercase) INFINITE
    if visited is None:
        visited = set()
    if path is None:
        path = list()
    if paths is None:
        paths = list()

    path.append(position)

    if position == "end":
        # print("end", path)
        paths.append(tuple(path))
        return paths

    visited.add(position)

    for next_node in nodes[position]:
        if next_node.isupper() or (next_node.islower() and next_node not in visited):
            find_paths1(nodes, next_node, visited.copy(), path.copy(), paths)

    return paths


def part1(data):
    nodes = parse(data)
    paths = find_paths1(nodes)
    return len(paths)


def find_paths2(nodes, position="start", visited=None, path=None, paths=None, visited_twice_used=False):
    # can visit a SINGLE small cave TWICE
    # can visit other small caves ONCE
    if visited is None:
        visited = set()
    if path is None:
        path = list()
    if paths is None:
        paths = list()

    path.append(position)

    if position == "end":
        # print("end", path)
        paths.append(tuple(path))
        return paths

    visited.add(position)

    for next_node in nodes[position]:
        if next_node == "start":
            continue

        if next_node.isupper():
            find_paths2(nodes, next_node, visited.copy(), path.copy(), paths, visited_twice_used)

        if next_node.islower() and next_node not in visited:
            find_paths2(nodes, next_node, visited.copy(), path.copy(), paths, visited_twice_used)

        if next_node.islower() and next_node in visited and not visited_twice_used:
            find_paths2(nodes, next_node, visited.copy(), path.copy(), paths, visited_twice_used=True)

    return paths


def part2(data):
    nodes = parse(data)
    paths = find_paths2(nodes)
    return len(paths)


class Test(unittest.TestCase):
    def test1_part1_example1(self):
        example = puzzle_input.from_example(__file__, 1)
        self.assertEqual(10, part1(example))

    def test2_part1_example2(self):
        example = puzzle_input.from_example(__file__, 2)
        self.assertEqual(19, part1(example))

    def test3_part1_example3(self):
        example = puzzle_input.from_example(__file__, 3)
        self.assertEqual(226, part1(example))

    def test4_part2_example1(self):
        example = puzzle_input.from_example(__file__, 1)
        self.assertEqual(36, part2(example))

    def test5_part2_example2(self):
        example = puzzle_input.from_example(__file__, 2)
        self.assertEqual(103, part2(example))

    def test6_part2_example3(self):
        example = puzzle_input.from_example(__file__, 3)
        self.assertEqual(3509, part2(example))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
