 """
집의 개수는 고정이다.
치킨 집과 집의 치킨 거리를 계산해서 치킨 거리가 가장 적은 값만 저장한다.

집의 위치, 치킨 집의 위치, 치킨 거리를 저장할 메모리가 필요하다.
"""
from itertools import combinations

# 도시의 크기와 유지할 치킨집 개수를 입력 받는다.
n, m = map(int, input().split())

# 도시의 모양을 입력 받는다.
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 집의 위치, 치킨집의 위치
h = []
ch = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            continue
        elif board[i][j] == 1:
            h.append((i, j))
        elif board[i][j] == 2:
            ch.append((i, j))

# 집의 개수, 각 집마다 최소 치킨 거리 저장리스트, 도시의 치킨 거리 리스트
lh = len(h)
cd = [0] * lh
cdList = []

# 유지할 치킨집을 구한다.            
for combi in combinations(ch, m):
    for i in range(lh):
        cd[i] = 0

    # 치킨집의 위치를 가져온다.
    for c in combi:
        # 해당 치킨집과 모든 집의 치킨 거리를 계산한다.
        for i in range(lh):
            t = abs(c[0] - h[i][0]) + abs(c[1] - h[i][1])
            # 가장 작은 값을 저장한다.
            if cd[i] > t or cd[i] == 0:
                cd[i] = t

    # 모든 집에 가장 작은 치킨 거리가 저장되었으면 다 더해서 도시의 치킨 리스트에 저장
    cdList.append(sum(cd))

# 가장 작은 도시의 치킨 리스트를 출력한다.    
print(min(cdList))