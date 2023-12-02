configuration = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_game_possible(game_str):
    """Return a tuple of (True/False, game_id); True if the game is possible, False otherwise."""

    game_info, rounds_str = game_str.split(":")
    game_id = game_info.split("Game ")[1]
    game_id = game_id.strip()
    game_id = int(game_id)
    for round_str in rounds_str.split(";"):
        color_number_strs = round_str.split(",")
        for color_number_str in color_number_strs:
            number, color = color_number_str.strip().split(" ")
            if configuration[color] < int(number):
                return (False, game_id)

    return (True, game_id)


if __name__ == "__main__":
    with open("test.txt", "r") as f:
        total = 0
        for game_str in f:
            possible, game_id = is_game_possible(game_str)
            if possible:
                total += game_id
        print(total)
