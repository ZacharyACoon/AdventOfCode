

def determine_priority(s: str):
    if s.islower():
        priority = ord(s) - 96
    else:
        priority = ord(s) - 38
    return priority


def part1(example_input):
    priority_total = 0
    for sack in example_input.strip().split("\n"):
        l = len(sack)
        sack = sack[:l // 2], sack[l // 2:]
        a, b = map(set, sack)

        intersection = a.intersection(b)
        intersection = ''.join(intersection)
        priority = determine_priority(intersection)
        # print(intersection, priority)
        priority_total += priority

    return priority_total


def part2(example_input):
    sacks = example_input.strip().split("\n")
    priority_total = 0
    for s in range(0, len(sacks), 3):
        ss = sacks[s: s+3]
        ss = map(set, ss)
        intersection = set.intersection(*ss)
        intersection = ''.join(intersection)
        priority_total += determine_priority(intersection)

    return priority_total
