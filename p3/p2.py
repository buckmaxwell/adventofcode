import numpy as np
from uuid import uuid4


# The gear relationship map maps the coordinates of a gear to any numbers adjacent to it.
gear_relationship_map = {}


def create_matrix(string_matrix):
    """
    String matrix looks like this:
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    """

    new_matrix_width = len(string_matrix.split("\n")[0])
    new_matrix_height = len(string_matrix.split("\n"))
    new_matrix = np.zeros((new_matrix_height, new_matrix_width), dtype=int)
    for i, row in enumerate(string_matrix.split("\n")):
        for j, element in enumerate(row):
            element = element.strip()
            if element.isdigit():
                new_matrix[i][j] = int(element)
            elif element == "*":
                new_matrix[i][j] = -2
            else:
                new_matrix[i][j] = -1
    return new_matrix


def number_has_adjacent_gear(matrix, x, y):
    if matrix[x][y] == -2:
        raise ValueError("This is a gear, not a number")

    try:
        # check above
        if matrix[x - 1][y] == -2:
            return (x - 1, y)
    except IndexError:
        pass

    try:
        # check below
        if matrix[x + 1][y] == -2:
            return (x + 1, y)

    except IndexError:
        pass

    try:
        # check left
        if matrix[x][y - 1] == -2:
            return (x, y - 1)
    except IndexError:
        pass

    try:
        # check right
        if matrix[x][y + 1] == -2:
            return (x, y + 1)
    except IndexError:
        pass

    try:
        # check top left
        if matrix[x - 1][y - 1] == -2:
            return (x - 1, y - 1)
    except IndexError:
        pass

    try:
        # check top right
        if matrix[x - 1][y + 1] == -2:
            return (x - 1, y + 1)
    except IndexError:
        pass

    try:
        # check bottom left
        if matrix[x + 1][y - 1] == -2:
            return (x + 1, y - 1)
    except IndexError:
        pass

    try:
        # check bottom right
        if matrix[x + 1][y + 1] == -2:
            return (x + 1, y + 1)
    except IndexError:
        pass

    return False


def return_numbers_adjacent_to_gear(matrix):
    """
    numbers are consecutive groups of non-zero numbers. Symbols are -2.
    Adjacent means directly next to each other, or diagonally next to each other.
    """

    number_group_has_neighbour = False
    current_number_group = []
    number_groups = []
    gear_coordinates = None
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element >= 0:
                current_number_group.append(element)
                if gc := number_has_adjacent_gear(matrix, i, j):
                    gear_coordinates = gc
                    number_group_has_neighbour = True
            else:
                if (
                    number_group_has_neighbour
                    and current_number_group
                    and gear_coordinates
                ):
                    number_groups.append(current_number_group)
                    if gear_coordinates not in gear_relationship_map:
                        gear_relationship_map[gear_coordinates] = [
                            int("".join([str(x) for x in current_number_group]))
                        ]
                    else:
                        gear_relationship_map[gear_coordinates].append(
                            int("".join([str(x) for x in current_number_group]))
                        )

                # reset
                current_number_group = []
                number_group_has_neighbour = False

    if current_number_group and number_group_has_neighbour and gear_coordinates:
        number_groups.append(current_number_group)
        if gear_coordinates not in gear_relationship_map:
            gear_relationship_map[gear_coordinates] = [
                int("".join([str(x) for x in current_number_group]))
            ]
        else:
            gear_relationship_map[gear_coordinates].append(
                int("".join([str(x) for x in current_number_group]))
            )

    # go through the gear coordinates map and find keys that are a list of length 2, calculate the gear ratio by multiplying the two numbers together
    result = [v[0] * v[1] for k, v in gear_relationship_map.items() if len(v) == 2]

    # get the sum of the gear ratios
    return sum(result)


def get_numbers_next_to_gears(string_matrix):
    matrix = create_matrix(string_matrix)
    return return_numbers_adjacent_to_gear(matrix)


if __name__ == "__main__":
    with open("test.txt", "r") as f:
        string_matrix = f.read()
        string_matrix = string_matrix.strip()
    print(get_numbers_next_to_gears(string_matrix))
