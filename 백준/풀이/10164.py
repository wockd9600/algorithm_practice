import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [[[0, 0] for _ in range(m + 1)] for _ in range(n + 1)]
board[1][1][0] = 1
arrive = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (i - 1) * m + j == k:
            board[i][j][1] = board[i-1][j][0] + board[i][j-1][0] + board[i][j][0]
            arrive = 1
            continue

        board[i][j][arrive] = board[i-1][j][arrive] + board[i][j-1][arrive] + board[i][j][arrive]

print(board[n][m][1] if board[n][m][1] != 0 else board[n][m][0])
