def game_power(game_str):
    """Return a tuple of (power, game_id)"""

    game_info, rounds_str = game_str.split(":")
    game_id = game_info.split("Game ")[1]
    game_id = game_id.strip()
    game_id = int(game_id)

    min_possible = {"red": 0, "green": 0, "blue": 0}
    for round_str in rounds_str.split(";"):
        color_number_strs = round_str.split(",")
        for color_number_str in color_number_strs:
            number, color = color_number_str.strip().split(" ")
            if min_possible[color] < int(number):
                min_possible[color] = int(number)

    power = min_possible["red"] * min_possible["green"] * min_possible["blue"]
    return (power, game_id)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        total = 0
        for game_str in f:
            power, game_id = game_power(game_str)
            total += power
        print(total)
