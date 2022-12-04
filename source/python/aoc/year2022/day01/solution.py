

def parse_input(puzzle_input):
    elves = puzzle_input.strip().split("\n\n")
    elves = [map(int, elf.split("\n")) for elf in elves]
    return elves


def part1(puzzle_input):
    elves = parse_input(puzzle_input)
    elf_totals = map(sum, elves)
    return max(elf_totals)


def part2(puzzle_input):
    elves = parse_input(puzzle_input)
    elf_totals = map(sum, elves)
    top_3_sum = sum(sorted(elf_totals)[-3:])
    return top_3_sum
