def bfs():
    # 편의점 수
    n = int(sys.stdin.readline())
    # 큐 생성
    queue = deque([])
    # 상근이네 집
    queue.append((map(int, sys.stdin.readline().split())))
    # 편의점 위치
    con = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        con.append((a, b))
    # 페스티벌 좌표
    rx, ry = map(int, sys.stdin.readline().split())
    # 편의점 방문 좌표
    check = [1] * n
    # 방문한 편의점이 있으면 계속 반복한다.
    while queue:
        # 현재 위치
        x1, y1 = queue.popleft()
        # 현재 위치에서 페스티벌까지 맥주를 마시면서 갈 수 있다면
        r = abs(x1 - rx) + abs(y1 - ry)
        if r <= 1000:
            # happy 출력
            return "happy"
        # 모든 편의점을 방문한다.
        for i in range(n):
            # 임의의 i번째 편의점에 방문한 적 없다면
            if check[i]:
                # 현재 위치부터 i번째 편의점까지 거리를 계산한다.
                s = abs(x1 - con[i][0]) + abs(y1 - con[i][1])
                # 맥주를 마시면서 갈 수 있는 거리라면
                if s <= 1000:
                    # 다음 편의점 방문
                    check[i] = False
                    queue.append((con[i][0], con[i][1]))
    # 방문할 수 있는 편의점을 모두 방문했는데 페스티벌에 도착하지 못했다면 sad 출력
    return "sad"

import sys
from collections import deque
# test case
t = int(sys.stdin.readline())
for _ in range(t):
    # bfs
    print(bfs())