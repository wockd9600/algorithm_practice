"""
노드 수와 간선수, 시작 노드, 그래프를 입력 받는다.
시작 노드를 방문해서 연결된 모든 노드에 값을 입력해준다.
연결 되었던 노드에 방문해서 연결된 노드까지 최소값인지 확인 후 최소값이면 입력
"""

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
dp = [INF] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    
    visited[start] = True
    dp[start] = 0
    
    while q:
        dist, index = heapq.heappop(q)

        if visited[index]:
            continue

        for i in graph[index]:
            tdist = dp[graph[index]] + dp[index]

            if tidst < dp[i[0]]:
                dp[i[0]] = tdist
                heapq.heappush(q, (tdist, i[0]))


dijkstra(start)

print(dp)
