import re


def parse(line):
    return re.split(r"-|: | ", line)


def validate_password1(a, b, char, password):
    return int(a) <= password.count(char) <= int(b)


def validate_password2(a, b, char, password):
    pos1 = password[int(a) - 1] == char
    pos2 = password[int(b) - 1] == char
    return pos1 ^ pos2


def count_valid(validator, lines):
    return sum(validator(*x) for x in lines)
