"""
dfs
3중 for문으로 1이 될 수 있는 모든 경우의 수를 구한다.
임의의 케이스에 0을 2로 바꾼다. (최솟값을 저장해서 반복 횟수를 줄임)
일단 단순하게 만들어보자.
"""
n, m = map(int, input().split())

ids = []
for _ in range(n):
    ids.append(list(map(int, input().split())))

inf = []
virus = []

def rc(num):
    return num//m, num%m

def infecting(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    elif ids[x][y] != 0:
        return
    
    ids[x][y] = -1

    for _ in range(4):
        infecting(x+1, y)
        infecting(x-1, y)
        infecting(x, y+1)
        infecting(x, y-1)

def dinfection(ids):
    for x in range(n):
        for y in range(m):
            if ids[x][y] == -1:
                ids[x][y] = 0
    for i in range(0, len(virus), 2):
        ids[virus[i]][virus[i+1]] = 2

check = True
def infection(ids):
    for x in range(n):
        for y in range(m):
            if ids[x][y] == 2:
                global check
                ids[x][y] = 0
                if check:
                    virus.append(x)
                    virus.append(y)
                infecting(x, y)
    check = False

def count(arr):
    c = 0
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 0:
                c += 1
    return c
                

# 벽세우기 모든 경우의 수
for one in range(n*m):
    a, b = rc(one)
    if ids[a][b] == 0:
        ids[a][b] = 1
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
                ids[e][f] = 1
                infection(ids)
                inf.append(count(ids))
                dinfection(ids)
                ids[e][f] = 0
            else:
                continue
        ids[c][d] = 0
    ids[a][b] = 0

print(max(inf))
