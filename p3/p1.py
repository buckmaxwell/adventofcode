import numpy as np
from uuid import uuid4


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
            elif element == ".":
                new_matrix[i][j] = -1
            else:
                new_matrix[i][j] = -2
    return new_matrix


def number_has_adjacent_symbol(matrix, x, y):
    if matrix[x][y] == -2:
        raise ValueError("This is a symbol, not a number")

    try:
        # check above
        if matrix[x - 1][y] == -2:
            return True
    except IndexError:
        pass

    try:
        # check below
        if matrix[x + 1][y] == -2:
            return True
    except IndexError:
        pass

    try:
        # check left
        if matrix[x][y - 1] == -2:
            return True
    except IndexError:
        pass

    try:
        # check right
        if matrix[x][y + 1] == -2:
            return True
    except IndexError:
        pass

    try:
        # check top left
        if matrix[x - 1][y - 1] == -2:
            return True
    except IndexError:
        pass

    try:
        # check top right
        if matrix[x - 1][y + 1] == -2:
            return True
    except IndexError:
        pass

    try:
        # check bottom left
        if matrix[x + 1][y - 1] == -2:
            return True
    except IndexError:
        pass

    try:
        # check bottom right
        if matrix[x + 1][y + 1] == -2:
            return True
    except IndexError:
        pass

    return False


def return_numbers_adjacent_to_symbol(matrix):
    """
    numbers are consecutive groups of non-zero numbers. Symbols are -2.
    Adjacent means directly next to each other, or diagonally next to each other.
    """

    number_group_has_neighbour = False
    current_number_group = []
    number_groups = []
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element >= 0:
                current_number_group.append(element)
                if number_has_adjacent_symbol(matrix, i, j):
                    number_group_has_neighbour = True
            else:
                if number_group_has_neighbour and current_number_group:
                    number_groups.append(current_number_group)

                # reset
                current_number_group = []
                number_group_has_neighbour = False

    if current_number_group and number_group_has_neighbour:
        number_groups.append(current_number_group)

    #  turn number groups into strings
    result = []
    for number_group in number_groups:
        result.append("".join([str(x) for x in number_group]))

    # turn the strings into integers
    result = [int(x) for x in result]

    return result


def get_numbers_next_to_symbols(string_matrix):
    matrix = create_matrix(string_matrix)
    return return_numbers_adjacent_to_symbol(matrix)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        string_matrix = f.read()
        string_matrix = string_matrix.strip()
    numbers = get_numbers_next_to_symbols(string_matrix)
    print(sum(numbers))
