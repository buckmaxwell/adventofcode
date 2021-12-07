def has_bingo(board):
    success = ["x", "x", "x", "x", "x"]

    # horizontal
    start, end = 0, 5
    for _ in range(0, 5):
        if board[start:end] == success:
            return True
        start += 5
        end += 5

    # veritical
    i = 0
    for i in range(0, 5):
        vertical_row = [
            board[i],
            board[i + 5],
            board[i + 10],
            board[i + 15],
            board[i + 20],
        ]
        if vertical_row == success:
            return True


def p1():
    with open("input.txt", "r") as f:
        numbers = f.readline().strip().split(",")
        boards = []
        for line in f:
            if not line.strip():
                boards.append([])
                continue
            boards[-1] += [number for number in line.strip().split(" ") if number]

        for number in numbers:
            bingo = None
            for board in boards:
                try:
                    idx = board.index(number)
                    board[idx] = "x"
                except ValueError:
                    pass
                if has_bingo(board):
                    bingo = sum([int(num) for num in board if num != "x"]) * int(number)
            if bingo:
                print(bingo)
                break


def p2():
    with open("input.txt", "r") as f:
        numbers = f.readline().strip().split(",")
        boards = []
        for line in f:
            if not line.strip():
                boards.append([])
                continue
            boards[-1] += [number for number in line.strip().split(" ") if number]

        bingo = None
        for number in numbers:
            new_boards = []
            for board in boards:
                try:
                    idx = board.index(number)
                    board[idx] = "x"
                except ValueError:
                    pass
                if has_bingo(board):
                    bingo = sum([int(num) for num in board if num != "x"]) * int(number)
                else:
                    new_boards.append(board)
            boards = new_boards

        if bingo:
            print(bingo)


if __name__ == "__main__":
    p2()
