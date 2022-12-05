
def parse_input(input: str):
    pairs = []
    for raw_pair in input.strip().split("\n"):
        pair = []
        for raw_section_range in raw_pair.split(","):
            section_range = raw_section_range.split("-")
            section_range = list(map(int, section_range))
            pair.append(section_range)
        pairs.append(pair)
    # print(pairs)
    return pairs


def bidirectional_total_overlap(pair):
    a, b = pair
    a1, a2 = a
    b1, b2 = b

    if a1 <= b1 and a2 >= b2:
        return True
    elif b1 <= a1 and b2 >= a2:
        return True

    return False


def bidirectional_overlap(pair):
    a, b = pair
    a1, a2 = a
    b1, b2 = b
    if a1 <= b1 <= a2:
        return True
    elif b1 <= a1 <= b2:
        return True
    return False


def part1(example_input):
    pairs = parse_input(example_input)
    return sum(map(bidirectional_total_overlap, pairs))


def part2(example_input):
    pairs = parse_input(example_input)
    return sum(map(bidirectional_overlap, pairs))
