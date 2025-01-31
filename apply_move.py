def apply(dictionary1, board):
    player = next(iter(dictionary1))
    played_space = next(iter(dictionary1.values()))

    for i in range(len(board - 1, -1, -1)):
        if board[i][played_space] == 0:
            if player == "p1":
                board[i][played_space] = -1
            elif player == "p2":
                board[i][played_space] = 1
            break
    return board
