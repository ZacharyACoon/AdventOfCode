from string import ascii_letters


def parse_stack_map(stack_map):
    stacks = {}
    for line in reversed(stack_map.splitlines()[:-1]):
        nothing = 0
        stack = 1
        for c in line:
            if c in ascii_letters:
                stacks.setdefault(stack, []).append(c)
                stack += 1
                nothing = 0
            elif c == " ":
                nothing += 1

            if nothing == 4:
                stack += 1
                nothing = 0
    for stack in stacks.values():
        print(stack)
    return stacks


def render_stack_map(stacks):
    max_height = max(map(len, stacks.values()))
    output = ""
    for height in range(max_height, -1, -1):
        row = ""
        for column in stacks.values():
            if height < len(column):
                row += "[" + column[height] + "] "
            else:
                row += "    "
        output += row + "\n"

    for i, _ in enumerate(stacks):
        output += f" {i+1}  "

    return output


def parse_raw_instructions(raw_instructions):
    raw_instructions = raw_instructions\
        .replace("move ", "")\
        .replace(" from ", ",")\
        .replace(" to ", ",")

    instructions = []
    for line in raw_instructions.splitlines():
        line = list(map(int, line.split(",")))
        instructions.append(line)
    return instructions


def parse_input(input):
    stack_map, raw_instructions = input.split("\n\n")
    stacks = parse_stack_map(stack_map)
    instructions = parse_raw_instructions(raw_instructions)
    return stacks, instructions


def process_instruction_single(instruction, stacks):
    count, a, b = instruction
    for _ in range(count):
        # if len(stacks[a]):
        moving = stacks[a].pop(-1)
        stacks[b].extend(moving)


def process_instruction_stack(instruction, stacks):
    count, a, b = instruction
    moving = stacks[a][-count:]
    stacks[a] = stacks[a][:-count]
    stacks[b].extend(moving)


def process_instructions(instructions, stacks, fn):
    for instruction in instructions:
        print(render_stack_map(stacks))
        fn(instruction, stacks)


def get_tops(stacks):
    tops = []
    for stack in stacks.values():
        if stack:
            tops.append(stack[-1])
    return tops


def part1(input):
    stacks, instructions = parse_input(input)
    process_instructions(instructions, stacks, process_instruction_single)
    return "".join(get_tops(stacks))


def part2(input):
    stacks, instructions = parse_input(input)
    process_instructions(instructions, stacks, process_instruction_stack)
    return "".join(get_tops(stacks))
