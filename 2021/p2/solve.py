def part1():
    horizontal_position = 0
    depth = 0
    with open("input.txt", "r") as f:
        for line in f:
            instruction, value = line.split(" ")
            if instruction == "forward":
                horizontal_position += int(value)
            elif instruction == "down":
                depth += int(value)
            elif instruction == "up":
                depth -= int(value)

    print(depth * horizontal_position)


def part2():
    horizontal_position = 0
    depth = 0
    aim = 0
    with open("input.txt", "r") as f:
        for line in f:
            instruction, value = line.split(" ")
            if instruction == "forward":
                horizontal_position += int(value)
                depth += aim * int(value)
            elif instruction == "down":
                aim += int(value)
            elif instruction == "up":
                aim -= int(value)

    print(depth * horizontal_position)


if __name__ == "__main__":
    part1()
    part2()
