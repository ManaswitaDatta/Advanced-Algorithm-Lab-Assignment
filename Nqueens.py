def isSafe(board, col, row, n):
    for i in range(n):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)) :
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveUtil(board, col, n):
    if col == n:
        print(board)
        return True
    res = False
    for i in range(n):
        if isSafe(board, col, i, n):
            board[i][col] = 1
            res = solveUtil(board, col + 1, n) or res
            board[i][col] = 0
    return res


n = int(input("Enter the number of queens: "))
board = [[0 for i in range(n)] for j in range(n)]
if not solveUtil(board, 0, n):
    print("Solution doesn't exist")

