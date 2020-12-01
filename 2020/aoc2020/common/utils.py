

def type_per_line(string, t=int):
    return [t(line) for line in string.splitlines() if line]
