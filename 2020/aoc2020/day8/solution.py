

def parse_instruction(instruction):
    operation = instruction[:3]
    argument = int(instruction[4:])
    return operation, argument


# 0 - no error
# 1 - repeating
# 2 - operation not implemented

def run_instructions(instructions):
    accumulator = 0
    offset = 0

    trail = {}
    while offset < len(instructions):
        error = 0
        increment = 1

        operation, argument = parse_instruction(instructions[offset])

        if "acc" in operation:
            accumulator += argument
        elif "jmp" in operation:
            increment = argument
        elif "nop" in operation:
            pass
        else:
            error = 2

        offset += increment

        if not offset in trail:
            trail[offset] = True
        else:
            error = 1

        yield offset, accumulator, error


def part1(input):
    for _, accumulator, error in run_instructions(input):
        if error == 1:
            return accumulator


def part2(input):
    for change_offset in range(len(input)):
        input_copy = input[:]
        if "jmp" in input_copy[change_offset]:
            input_copy[change_offset] = input_copy[change_offset].replace("jmp", "nop")
        elif "nop" in input_copy[change_offset]:
            input_copy[change_offset] = input_copy[change_offset].replace("nop", "jmp")
        else:
            continue  # next loop

        for _, accumulator, error in run_instructions(input_copy):
            if error == 1:
                break
        else:
            return accumulator


if __name__ == "__main__":
    from aoc2020.common import puzzle_input
    input = puzzle_input.from_arg_file().splitlines()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
