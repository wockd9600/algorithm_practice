import heapq
import sys
input = sys.stdin.readline
INF = int(10e9)

def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    dp[1][0] = 0

    while q:
        dist, now = heapq.heappop(q)

        for next_node, l in graph[now]:
            cost = dist + l

            if cost < dp[next_node][k-1]:
                dp[next_node][k-1] = cost
                dp[next_node].sort()
                heapq.heappush(q, (cost, next_node))

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dp = [[INF] * (k) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


dijkstra()

for i in range(1, n + 1):
    print(dp[i][k-1] if dp[i][k-1] != INF else -1)
