def part1():
    with open("input.txt", "r") as f:
        new_bin_list = None
        no_lines = 0
        for line in f:
            line = line.strip()
            no_lines += 1
            if new_bin_list is None:
                new_bin_list = list(line)
                continue

            for pos, digit in enumerate(line):
                new_bin_list[pos] = int(new_bin_list[pos]) + int(digit)

        gamma_bin = "".join([f"{round(b / no_lines)}" for b in new_bin_list])
        epsilon_bin = "".join([f"{abs(round(b / no_lines) - 1)}" for b in new_bin_list])

        print(int(gamma_bin, 2) * int(epsilon_bin, 2))


def get_oxygen_generator_rating(oxygen_generator_ratings):
    for pos, _val in enumerate(oxygen_generator_ratings[0]):
        if len(oxygen_generator_ratings) == 1:
            return oxygen_generator_ratings[0]

        sum_of_pos = sum([int(o[pos]) for o in oxygen_generator_ratings])
        one_is_more_common = sum_of_pos >= len(oxygen_generator_ratings) / 2
        value_to_keep = "1" if one_is_more_common else "0"

        new_oxygen_generator_ratings = []
        for oxygen_generator_rating in oxygen_generator_ratings:
            if oxygen_generator_rating[pos] == value_to_keep:
                new_oxygen_generator_ratings.append(oxygen_generator_rating)
        oxygen_generator_ratings = new_oxygen_generator_ratings
    if len(oxygen_generator_ratings) == 1:
        return oxygen_generator_ratings[0]


def get_c02_scrubber_rating(c02_scrubber_ratings):
    for pos, _val in enumerate(c02_scrubber_ratings[0]):
        if len(c02_scrubber_ratings) == 1:
            return c02_scrubber_ratings[0]

        sum_of_pos = sum([int(o[pos]) for o in c02_scrubber_ratings])
        one_is_more_common = sum_of_pos >= len(c02_scrubber_ratings) / 2
        value_to_keep = "0" if one_is_more_common else "1"

        new_c02_scrubber_ratings = []
        for c02_scrubber_rating in c02_scrubber_ratings:
            if c02_scrubber_rating[pos] == value_to_keep:
                new_c02_scrubber_ratings.append(c02_scrubber_rating)
        c02_scrubber_ratings = new_c02_scrubber_ratings
    if len(c02_scrubber_ratings) == 1:
        return c02_scrubber_ratings[0]


def part2():
    oxygen_generator_ratings = []
    with open("input.txt", "r") as f:
        new_bin_list = None
        no_lines = 0
        for line in f:
            line = line.strip()
            oxygen_generator_ratings.append(line)

    c02_scrubber_ratings = oxygen_generator_ratings.copy()

    oxygen_generator_rating = get_oxygen_generator_rating(oxygen_generator_ratings)
    c02_scrubber_rating = get_c02_scrubber_rating(c02_scrubber_ratings)

    print(int(oxygen_generator_rating, 2) * int(c02_scrubber_rating, 2))


if __name__ == "__main__":
    part2()
