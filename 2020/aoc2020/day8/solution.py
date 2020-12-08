

def parse_instructions(instructions):
    accumulator = 0
    offset = 0
    while offset < len(instructions):
        line = instructions[offset]
        operation = line[:3]
        argument = int(line[4:])
        increment = 1
        if "acc" in operation:
            accumulator += argument
        elif "jmp" in operation:
            increment = argument
        elif "nop" in operation:
            pass
        yield offset, accumulator
        offset += increment


def run_instructions_until_repeat(instructions):
    visited = {}
    for offset, accumulator in parse_instructions(instructions):
        if offset in visited:
            raise IndexError
        else:
            visited[offset] = True
            yield offset, accumulator


# unused
def get_furthest(instructions):
    furthest = 0
    for offset, _ in run_instructions_until_repeat(instructions):
        if offset > furthest:
            furthest = offset


def track(input):
    past = []
    try:
        for offset, _ in run_instructions_until_repeat(input):
            past.append(offset)
    except IndexError:
        return past


def part1(input):
    for _, accumulator in run_instructions_until_repeat(input):
        pass
    return accumulator


def part2(input):
    for changed_offset in reversed(track(input)):
        input_copy = input[:]
        if "jmp" in input_copy[changed_offset]:
            print("flipping jmp to nop at", changed_offset)
            input_copy[changed_offset] = input_copy[changed_offset].replace("jmp", "nop")
        elif "nop" in input_copy[changed_offset]:
            print("flipping nop to jmp at", changed_offset)
            input_copy[changed_offset] = input_copy[changed_offset].replace("nop", "jmp")
        else:
            continue

        try:
            for offset, accumulator in run_instructions_until_repeat(input_copy):
                pass
            print(accumulator)
        except IndexError:
            pass


if __name__ == "__main__":
    from aoc2020.common import puzzle_input
    input = puzzle_input.from_arg_file().splitlines()

    # print("Part 1:", part1(input))
    print("Part 2:", part2(input))
