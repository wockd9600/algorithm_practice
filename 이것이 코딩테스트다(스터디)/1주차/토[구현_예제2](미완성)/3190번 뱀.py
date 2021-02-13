"""
어렸을 적 컴퓨터 시간에 했던 뱀 게임을 만들면 된다.
뱀은 머리를 기준으로 방향이 움직이고 나머지는 차례대로 머리를 뒤따른다. 과일을 먹으면 몸이 1씩 늘어난다.
뱀의 움직임은 맨 앞과 맨 뒤만 변화하므로 큐 자료구조 방식이 적절할 거라고 생각했다.
"""

from collections import deque

# 뱀이 지나다닐 보드 입력
n = int(input())
board = [[0]*n for _ in range(n)]

# 뱀의 위치를 나타낼 큐 자료구조, 뱀의 머리의 좌표, 방향
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

# 뱀의 머리가 뱀의 몸에 닿았는지 확인
def checkSnake(x, y):
    for i in snake:
        if x == i[0] and y == i[1]:
            return True
    return False

# 과일의 개수와 좌표를 받고 보드에 입력한다.
appleCnt = int(input())
for _ in range(appleCnt):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1


# 뱀의 방향 변환과 횟수
l = int(input())
rotate = []
for _ in range(l):
    X, c = input().split()
    rotate.append([int(X), c])

# 시간, 방향 변환 index
t = 0
i = 0
# 시작
while True:
    # 뱀의 머리가 향한 방향으로 움직이고 시간을 더 한다.
    x += dx[d]
    y += dy[d]
    t += 1
    # 움직인 방향이 문제가 없는지(몸에 접촉, 보드 경계) 확인한다.
    if checkSnake(x, y) or x < 0 or x >= n or y < 0 or y >= n:
        break

    # 뱀의 위치에 좌표 추가
    snake.append(tuple([x, y]))
    if board[x][y] == 1: #뱀이 방문한 좌표에 과일이 있으면 과일을 먹고(없애고)
        board[x][y] = 0
    else: #없으면 꼬리를 지운다.
        snake.popleft()
    
    # 방향을 바꿀 시간이 됐는지 확인한다.
    if t == rotate[i][0]:
        # 시간이 됐다면 방향을 바꿔준다.
        d = changeDirection(rotate[i][1])
        i += 1
        i = 0 if i >= l else i
    
print(t)

"""
뱀을 하나 만들었으니 게임 자체를 만들어보는 것도 좋을 거 같다.
"""
