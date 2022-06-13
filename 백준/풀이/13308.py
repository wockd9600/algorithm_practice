import heapq
import sys
import math
input = sys.stdin.readline
INF = int(2e14)

def dijkstra():
    q = []
    heapq.heappush(q, (0, gas[1],  1))

    dp = [[INF] * 2501 for _ in range(n + 1)]
    dp [1][gas[1]] = 0

    while q:
        dist, curgas, now = heapq.heappop(q)

        if now == n: return dist
        if dist > dp[now][curgas]: continue
        
        curgas = min(curgas, gas[now])

        for next_node, l in graph[now]:
            cost = dist + l * curgas

            if cost < dp[next_node][curgas]:
                dp[next_node][curgas] = cost
                heapq.heappush(q, (cost, curgas, next_node))

n, m = map(int, input().rstrip().split())
gas = [INF] + list(map(int, input().rstrip().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(dijkstra())