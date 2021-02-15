"""
주어진 도시 x에서 가까운 도시부터 방문해서 최단 거리를 저장한다.
구한 최단 거리가 k인 것만 출력한다.
"""
from collections import deque
import sys

# 도시, 도로, 원하는 거리, 출발 도시
n, m, k, x = map(int, sys.stdin.readline().split())
# 도로 입력 (Adjacency List)
road = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    road[a].append(b)

# 모든 도로의 거리를 저장할 리스트 초기화
distance = [-1] * (n + 1)

queue = deque([x])

# 출발 도시 도착
distance[x] = 0
while queue:
    city = queue.popleft()
    # 해당 도시와 연결된 도시 중 방문된 적 없으면 큐에 넣는다.
    for i in road[city]:
        if distance[i] == -1:
            queue.append(i)
            distance[i] = distance[city] + 1


ck = True
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        ck = False

if ck:
    print(-1)
