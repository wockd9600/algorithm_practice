import heapq
import sys
input = sys.stdin.readline
INF = int(10e9)

def dijkstra(s, e):
    q = []
    heapq.heappush(q, (0, 1))
    dp = [INF] * (n + 1)
    dp[1] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > dp[now]: continue

        for next_node, l in graph[now]:
            if s == now and e == next_node or s == next_node and e == now: continue

            cost = dist + l

            if cost < dp[next_node]:
                dp[next_node] = cost
                if not s: pre[next_node] = now
                heapq.heappush(q, (cost, next_node))
    
    return dp[n]

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
pre = [0 for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().rstrip().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

dijkstra(0, 0)

answer = -1
e = n

while pre[e] != 0:
    s = pre[e]
    answer = max(answer, dijkstra(s, e))
    e = s
print(answer)