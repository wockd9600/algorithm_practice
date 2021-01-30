"""
노드 수와 간선수, 시작 노드, 그래프를 입력 받는다.
시작 노드를 방문해서 연결된 모든 노드에 값을 입력해준다.
연결 되었던 노드에 방문해서 연결된 노드까지 최소값인지 확인 후 최소값이면 입력
"""

import sys
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

def min_node():
    minIndex = 0
    for i in range(n + 1):
        if not visited[i] and dp[i] < dp[minIndex]:
            minIndex = i
    return minIndex

def dijkstra(start):
    visited[start] = True
    dp[start] = 0
    for i in graph[start]:
        dp[i[0]] = i[1]

    for i in range(n - 1):
        index = min_node()
        visited[index] = True
        for j in graph[index]:
            dist = dp[index] + j[1]
            if dp[j[0]] > dist:
                dp[j[0]] = dist


dijkstra(start)

print(dp)
