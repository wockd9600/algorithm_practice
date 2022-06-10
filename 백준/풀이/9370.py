import heapq
import sys
input = sys.stdin.readline
INF = int(10e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    dp = [INF] * ( n + 1)
    dp[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > dp[now]: continue

        for next_node, l in graph[now]:
            cost = dist + l

            if cost < dp[next_node]:
                dp[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    
    return dp

testcase = int(input())

for _ in range(testcase):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    destination = []

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    for _ in range(t):
        destination.append((int(input())))

    dp_s = dijkstra(s)
    dp_g = dijkstra(g)
    dp_h = dijkstra(h)

    answer = []

    for de in destination:
        if dp_s[de] == dp_s[g] + dp_g[h] + dp_h[de] or dp_s[de] == dp_s[h] + dp_h[g] + dp_g[de]:
            answer.append(de)
    
    answer.sort()

    print(' '.join(map(str, answer)))