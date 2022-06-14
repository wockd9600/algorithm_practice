import heapq
from collections import deque
import sys
input = sys.stdin.readline
INF = int(10e9)

def bfs(last_node, dp):
    q = deque([last_node])
    
    while q:
        now = q.popleft()

        for pre_node, l in graph_r[now]:
            if not visit[pre_node][now] and dp[pre_node] + l == dp[now]:
                    visit[pre_node][now] = 1
                    q.append(pre_node)

def dijkstra(s, e):
    q = []
    heapq.heappush(q, (0, s))
    dp = [INF] * n
    dp[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > dp[now]: continue

        for next_node, l in graph[now]:
            if visit[now][next_node]: continue
            cost = dist + l

            if cost < dp[next_node]:
                dp[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return dp

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    s, d = map(int, input().split())

    graph = [[] for _ in range(n)]
    graph_r = [[] for _ in range(n)]
    visit = [[0] * n for _ in range(n)]

    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))
        graph_r[v].append((u, p))
                                    
    dp = dijkstra(s, d)
    bfs(d, dp)

    answer = dijkstra(s, d)
    print(answer[d] if answer[d] != INF else -1)
