from string import digits

strs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
reversed_strs = [s[::-1] for s in strs]


def get_first_digit(line, strs=strs):

    mem = ""
    for c in line:
        if c in digits:
            return c
        mem += c
        for s in strs:
            if s in mem:
                return str(strs.index(s) + 1)


def get_last_digit(line):
    return get_first_digit(reversed(line), reversed_strs)


with open("input.txt") as f:
    total = 0
    for line in f:
        if line.strip() != "":
            total += int(get_first_digit(line.strip()) + get_last_digit(line.strip()))

    print(total)
