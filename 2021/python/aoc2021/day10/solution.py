import unittest
from aoc2021.common import puzzle_input


class LinkedListItem:
    def __init__(self, v, n=None):
        self.value = v
        self.next = n


class LinkedList:
    def __init__(self):
        self.next = None

    def __repr__(self):
        s = ""
        current = self.next
        while current:
            s += str(current.value)
            current = current.next
        return s

    def add(self, v):
        self.next = LinkedListItem(v, self.next)

    def peek(self):
        if self.next:
            return self.next.value

    def get(self):
        node = self.next
        self.next = self.next.next
        return node.value


anti = {
    "[": "]",
    "(": ")",
    "{": "}",
    "<": ">"
}

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


def classify_line(line):
    # 0, valid
    # 1, corrupted
    # 2, incomplete
    stack = LinkedList()
    for c in line:
        if c in anti:
            stack.add(anti[c])
        elif c in anti.values():
            if c != stack.get():
                return 1, c, None

    if stack.peek():
        closing = ""
        while stack.peek():
            closing += stack.get()

        return 2, None, closing

    return 0, None, None


def part1(data):
    lines = data.strip().splitlines()
    classifications = map(classify_line, lines)
    score = 0
    for classification, character, closing in classifications:
        if classification == 1:
            score += scores[character]
    return score


closing_scores = dict([(c, i+1) for i, c in enumerate(")]}>")])


def part2(data):
    lines = data.strip().splitlines()
    scores = []
    for line in lines:
        t, c, closing = classify_line(line)
        # if incomplete
        if t == 2:
            scores.append(0)
            # print(line, closing)
            for c in closing:
                scores[-1] *= 5
                scores[-1] += closing_scores[c]
    sorted_scores = sorted(scores)
    # print(sorted_scores)
    middle = len(sorted_scores) // 2
    return sorted_scores[middle]


class Test(unittest.TestCase):
    examples = puzzle_input.from_examples(__file__)  # list of stripped str

    def test1_part1_example1(self):
        example = self.examples[0]
        self.assertEqual(26397, part1(example))

    def test2_part2_example1(self):
        example = self.examples[0]
        self.assertEqual(288957, part2(example))


if __name__ == "__main__":
    # unittest.main()
    data = puzzle_input.from_arg_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
