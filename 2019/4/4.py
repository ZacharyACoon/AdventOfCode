
# puzzle_input: 367479-893698
# Six digit number
# within the range of the puzzle input
# doesn't decrease

input_min = 367479
input_max = 893698


class Lowers(ValueError):pass
class NotGroupOfTwo(ValueError):pass
class NoDouble(ValueError):pass
class ShouldHaveErrored(ValueError):pass


def check_rules(n):
    digits = str(n)
    double = False

    last = int(digits[0])
    repeats = 0
    for digit in map(int, digits[1:]):
        if digit < last:
            raise Lowers
        elif digit == last:
            repeats += 1
        elif repeats and digit != last:
            if repeats == 1:
                double = True
            repeats = 0
        last = digit
    if repeats == 1:
        double = True

    if not double:
        raise NoDouble

    return True


try:
    print(check_rules(111111))
    raise ShouldHaveErrored
except NoDouble:pass
try:
    print(check_rules(223450)) # decreasing
    raise ShouldHaveErrored
except Lowers:pass
try:
    print(check_rules(123789)) # No double
    raise ShouldHaveErrored
except NoDouble:pass


valid = []
for i in range(input_min, input_max):
    try:
        check_rules(i)
        valid.append(i)
    except ValueError:
        pass
print("Possible:", len(valid))
