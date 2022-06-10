import heapq
import sys
input = sys.stdin.readline
INF = int(10e9)

def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    
    dp = [INF] * (n + 1)
    dp[1] = 0

    visited = [0] * (n + 1)
    pre = [0] * (n + 1)

    while q:
        dist, now = heapq.heappop(q)
        visited[now] = 1

        if dist > dp[now]: continue

        for next_node, l in graph[now]:
            cost = dist + l

            if cost < dp[next_node]:
                dp[next_node] = cost
                heapq.heappush(q, (cost, next_node))
                pre[next_node] = now
    return pre
    
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

path = dijkstra()

print(n - 1)
for i in range(2, n + 1):
    print(i, path[i])