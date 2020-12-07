

def calculate_fuel_for_mass(mass):
    return mass // 3 - 2


def calculate_fuel_for_mass_recursively(mass):
    fuel = calculate_fuel_for_mass(mass)
    if fuel > 0:
        return fuel + calculate_fuel_for_mass_recursively(fuel)
    else:
        return 0


def part1(input):
    return sum(calculate_fuel_for_mass(int(module)) for module in input)


def part2(input):
    return sum(calculate_fuel_for_mass_recursively(int(module)) for module in input)


if __name__ == "__main__":
    from aoc2019.common import puzzle_input
    input = puzzle_input.from_arg_file().splitlines()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
