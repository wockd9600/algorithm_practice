"""
dfs
벽으로 막을 수 있는 모든 경우의 수를 구한다.
각 케이스 마다 바이러스를 퍼뜨려 생존 가능한 방의 개수를 구한다.

복기
이 문제에서 bfs는 바이러스가 퍼지는 것에 적용하는 것이 아니라
벽을 세우는 거에 적용하는 문제였음.. 물론 두 개 다 bfs로 적용할 수 있지만
바이러스가 퍼지는 건 dfs가 더 낫지 않나 생각했는데
벽 세울 때 bfs를 적용하는 것까지는 뇌가 열려있지 않았던 것 같다.
"""

# 2차원 배열을 1차원화한 배열을 다시 2차원화 ㅋㅋㅋㅋ
def rc(num):
    return num//m, num%m

# 임의의 바이러스가 활동한다.
def infecting(x, y):
    # 연구소의 크기를 벗어나면 x
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    # 빈 방이 아니라면 감염 불가능
    elif temp[x][y] != 0:
        return

    # 감염된 방은 -1로 표시한다.
    temp[x][y] = -1

    # 해당 칸의 상하좌우와 다시 상하좌우의 칸의 상하좌우도 감염시킨다.
    for _ in range(4):
        infecting(x+1, y)
        infecting(x-1, y)
        infecting(x, y+1)
        infecting(x, y-1)

# 벽을 모두(3개) 세웠을 때 바이러스 감염 시작
def infection(arr):
    # 모든 방을 확인한다.
    for i in range(n*m):
        x, y = rc(i)
        # 만약 해당 칸에 바이러스가 있다면 감염을 시작한다
        if arr[x][y] == 2:
                arr[x][y] = 0
                infecting(x, y)

# 바이러스 감염이 끝났을 때 안전한 칸을 카운트한다.
def count(arr):
    global maxids
    c = 0
    for i in range(n*m):
        x, y = rc(i)
        if arr[x][y] == 0:
                c += 1
    # 이번 케이스의 생존 칸이 저번 케이스 보다 적다면
    # 최대 생존 칸의 수를 바꾸지 않는다.
    if maxids > c: c = maxids
        
    return c
                

# 행렬의 크기(NxM)를 입력
n, m = map(int, input().split())

# 연구소 기본 구조
ids = []
for _ in range(n):
    ids.append(list(map(int, input().split())))

# 가장 많은 생존 칸의 수
maxids = 0
# 테스트할 임시 연구소
temp = [[0] * m for _ in range(n)]

# 벽 세우기(3개) 모든 경우의 수
# 각 for문이 벽을 세울 위치고, x, y 로 6중 for문 돌리기 싫어서 편법을 사용했다.
# 연구소의 크기(배열의 총 크기)를 1차원화 해서 n*m으로 표현했다.
for one in range(n*m):
    # custom function 'rc'를 통해 1차원화한 크기를 다시 2차원으로 돌려 받는다.
    a, b = rc(one)

    # 만약 연구소가 비어있으면 벽을 세우고
    if ids[a][b] == 0:
        ids[a][b] = 1

    # 바이러스 또는 벽이 이미 있다면 빈 곳을 찾는다.
    else:
        continue
    
    for two in range(one, m*n):
        c, d = rc(two)

        if ids[c][d] == 0:
            ids[c][d] = 1
        else:
            continue
        
        for three in range(two, m*n):
            e, f = rc(three)
            
            if ids[e][f] == 0:
                # 만약 세 번째 벽을 세웠다면 바이러스 감염을 시작한다.
                ids[e][f] = 1
                # 바이러스 감염은 임시 연구소에서 진행한다.
                for x in range(n):
                    for y in range(m):
                        temp[x][y] = ids[x][y]
                infection(temp)
                # 생존 가능한 벽을 카운트
                maxids = count(temp)
                ids[e][f] = 0
            else:
                continue
        ids[c][d] = 0
    ids[a][b] = 0

print(maxids)
