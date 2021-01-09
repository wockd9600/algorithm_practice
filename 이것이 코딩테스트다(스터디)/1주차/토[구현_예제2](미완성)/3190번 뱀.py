from collections import deque

n = int(input())
board = [[0]*n for _ in range(n)]

snake = deque([(0, 0)])
x, y = 0, 0
d = 0
#     R, D, L, U
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def changeDirection(c):
    dirc = 1 if c == 'D' else -1
    dirc += d
    if dirc < 0:
        dirc = 3
    elif dirc > 3:
        dirc = 0
    return dirc

def checkSnake(x, y):
    for i in snake:
        if x == i[0] and y == i[1]:
            return True
    return False

appleCnt = int(input())
for _ in range(appleCnt):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

l = int(input())
rotate = []
for _ in range(l):
    X, c = input().split()
    rotate.append([int(X), c])

t = 0
i = 0
while True:    
    x += dx[d]
    y += dy[d]
    t += 1
    if checkSnake(x, y) or x < 0 or x >= n or y < 0 or y >= n:
        break

    snake.append(tuple([x, y]))
    if board[x][y] == 1:
        board[x][y] = 0
    else:
        snake.popleft()
    
    
    if t == rotate[i][0]:
        d = changeDirection(rotate[i][1])
        i += 1
        i = 0 if i >= l else i
    
print(t)
