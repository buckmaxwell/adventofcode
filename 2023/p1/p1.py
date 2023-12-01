from string import digits


def get_first_and_last_digit(num):
    result = None
    for c in str(num):
        if c in digits:
            result = c
            break

    for c in reversed(str(num)):
        if c in digits:
            result += c
            break

    return int(result)


with open("input.txt") as f:
    total = 0
    for line in f:
        total += get_first_and_last_digit(line.strip())
    print(total)
