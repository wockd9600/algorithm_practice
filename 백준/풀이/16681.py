import heapq
import sys
input = sys.stdin.readline
INF = int(2e14)

def dijkstra(start, r):
    q = []
    heapq.heappush(q, (0, start))

    dp = [INF] * (n + 1)
    dp[start] = 0
    

    while q:
        dist, now = heapq.heappop(q)

        if dist > dp[now]: continue
        
        for next_node, l in graph[now]:
            cost = dist + l
            if heights[next_node-1] == heights[now-1]: continue

            if cost < dp[next_node] and heights[next_node-1] > heights[now-1]:
                dp[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return dp

n, m, d, e = map(int, input().rstrip().split())
heights = list(map(int, input().rstrip().split()))

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dp_h_m = dijkstra(1, 0)
dp_m_c = dijkstra(n, 1)

answer = -INF
check = False
for i in range(1, n + 1):
    if dp_h_m[i] == INF or dp_m_c[i] == INF: continue

    catharsis = heights[i-1] * e
    total_d = (dp_h_m[i] + dp_m_c[i]) * d
    answer = max(answer, catharsis - total_d)
    check = True

print(answer if check else "Impossible")