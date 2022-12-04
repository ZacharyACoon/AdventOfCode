

# A, X, rock, 1,
# B, Y, paper, 2
# C, Z, scissors, 3

# get points for your selection
# +
# 0, lost
# 3, draw
# 6, won


enumerate_rps = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2
}


def parse(example_input: str):
    for play in example_input.strip().splitlines():
        a, b = play.split(" ")
        a = enumerate_rps[a]
        b = enumerate_rps[b]
        yield a, b


def hand_to_result_points(hand: tuple[int, int]):
    a, b = hand
    # win
    if b == (a + 1) % 3:
        r = 6
    # draw
    elif a == b:
        r = 3
    # loss
    else:
        r = 0
    return r + b + 1


def part1(example_input):
    hands = parse(example_input)
    return sum(map(hand_to_result_points, hands))


# X, lose
# Y, draw
# Z, win


def result_to_hand_points(play: tuple[int, int]):
    their_hand, goal_result = play
    # lose
    if goal_result == 0:
        your_hand = (their_hand - 1) % 3
    # draw
    elif goal_result == 1:
        your_hand = their_hand
    # win
    else:
        your_hand = (their_hand + 1) % 3

    points = 3 * goal_result + your_hand + 1
    return points


def part2(example_input):
    plays = parse(example_input)
    return sum(map(result_to_hand_points, plays))
