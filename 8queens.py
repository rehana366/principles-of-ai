N = 8
count = 0

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()


def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve(board, col):
    global count

    if col == N:
        count += 1
        print(f"Solution {count}:")
        print_board(board)
        
        if count == 7:
            return True
        return False

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve(board, col + 1):
                return True 

            board[row][col] = 0
    return False

board = [[0] * N for _ in range(N)]
solve(board, 0)

print("Finished")