numbers = []
with open("input.txt", "r") as f:
    for line in f:
        numbers.append(int(line.strip()))


def part1():
    result = 0
    previous_number = None
    for number in numbers:
        if previous_number is not None and previous_number < number:
            result += 1
        previous_number = number

    print(result)


def part2():
    result = 0
    previous_window_sum = None
    window = []
    for number in numbers:
        window.append(number)
        if len(window) == 3:
            if previous_window_sum is not None and previous_window_sum < sum(window):
                result += 1
            previous_window_sum = sum(window)
            window.pop(0)

    print(result)


if __name__ == "__main__":
    part1()
    part2()
    # Solved!
