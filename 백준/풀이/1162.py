import heapq
import sys
input = sys.stdin.readline
INF = int(10e9)

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, 0, s))

    dp[s] = [0 for _ in range(k + 1)]

    while q:
        dist, paved, now = heapq.heappop(q)

        if dist > dp[now][paved]: continue

        for next_node, l in graph[now]:
            cost = dist + l

            if cost < dp[next_node][paved]:
                dp[next_node][paved] = cost
                heapq.heappush(q, (cost, paved, next_node))
            
            if paved < k and dist < dp[next_node][paved+1]:
                dp[next_node][paved+1] = dist
                heapq.heappush(q, (dist, paved + 1, next_node))
         
n, m, k = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]
dp = [[INF] * (k + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(1)

print(min(dp[n]))