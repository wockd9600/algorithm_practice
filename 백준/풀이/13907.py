import heapq
import sys
input = sys.stdin.readline
INF = int(10e9)

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, 0, start))
    dp[start] = [0] * (n + 1)

    while q:
        dist, cnt, now = heapq.heappop(q)
        
        f = 0
        for i in range(1, cnt):
            if dist > dp[now][i]:
                f = 1
                break
        if dist > dp[now][cnt] or f or now == end: continue

        for next_node, l in graph[now]:
            cost = dist + l

            if cost < dp[next_node][cnt+1]:
                dp[next_node][cnt+1] = cost
                heapq.heappush(q, (cost, cnt + 1, next_node))

n, m, k = map(int, input().split())
s, d = map(int, input().split())

graph = [[] for _ in range(n + 1)]
dp = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

dijkstra(s, d)

a = dp[d]
print(min(a))
for _ in range(k):
    p = int(input())
    a = [x + i * p for i, x in enumerate(a)]
    print(min(a))
