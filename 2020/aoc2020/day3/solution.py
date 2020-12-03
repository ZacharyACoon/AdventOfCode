

given_slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


def measure_slope(slope_map, xi, yi):
    x = 0
    y = 0
    yl = len(slope_map) - 1
    trees = 0
    while y < yl:
        x += xi
        y += yi
        if slope_map[y][x % len(slope_map[y])] == "#":
            trees += 1
    return trees


def measure_slopes(slope_map, slopes):
    for slope in slopes:
        a = measure_slope(slope_map, *slope)
        yield a
