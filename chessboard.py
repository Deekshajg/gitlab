def print_chessboard(board):
    for row in board:
        print(" ".join(row))

def create_chessboard():
    board = [['_' for _ in range(8)] for _ in range(8)]

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                board[i][j] = 'X'

    return board

chessboard = create_chessboard()
print_chessboard(chessboard)
