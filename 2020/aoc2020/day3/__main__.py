from aoc2020.common import puzzle_input


a = puzzle_input.from_arg_file().splitlines()

print(len(a))

y = 0
x = 0
trees = 0
width = len(a[0])
while y < len(a) - 1:
    x += 1
    y += 2
    print(y, x, x % width)
    if a[y][x % width] == "#":
        trees += 1
    print(trees)


print(trees)

if __name__ == "__main__":
    pass
