import heapq
import sys
input = sys.stdin.readline
INF = int(10e9)

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s, 0))

    dp = [[INF] * (k + 1) for _ in range(n + 1)]
    dp[1] = [0 for _ in range(k + 1)]
    pre = [[-1] * (k + 1) for _ in range(n + 1)]
    print('-')
    while q:
        dist, now, free = heapq.heappop(q)

        if dist > dp[now][free]: continue
        print(now, dist, free)

        for next_node, l in network[now]:
            cost = dist + l
            
            if cost < dp[next_node][free]:
                dp[next_node][free] = cost
                heapq.heappush(q, (cost, next_node, free))
                pre[next_node][free] = now
            
            if free < k and dist < dp[next_node][free+1]:
                dp[next_node][free+1] = dist
                heapq.heappush(q, (dist, next_node, free + 1))
                pre[next_node][free+1] = now
    print(pre)
    return dp

n, p, k = map(int, input().rstrip().split())

network = [[] for _ in range(n + 1)]

for _ in range(p):
    a, b, c = map(int, input().rstrip().split())
    network[a].append((b, c))
    network[b].append((a, c))

dp = dijkstra(1)
print(dp)