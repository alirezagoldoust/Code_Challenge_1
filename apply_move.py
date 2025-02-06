def apply_move(player, column, board):
    for i in range(len(board) - 1, -1, -1):
        if board[i][column] == 0:
            board[i][column] = -1 if player == "p1" else 1
            return board
    return board
