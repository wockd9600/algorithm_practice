import heapq
import sys
input = sys.stdin.readline
INF = int(2e14)

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))

    dp = [[INF] * (m + 1) for _ in range(n)]
    dp[0][0] = 0

    while q:
        dist, expense, now = heapq.heappop(q)

        if dist > dp[now][expense]: continue
        
        for next_node, e, d in graph[now]:
            cost = dist + d
            next_expense = expense + e

            if next_expense <= m and cost < dp[next_node][next_expense]:
                for i in range(next_expense, m + 1):
                    if dp[next_node][i] > cost:
                        dp[next_node][i] = cost
                    else: break
                heapq.heappush(q, (cost, next_expense, next_node))
                
    return dp[n-1][m]

for _ in range(int(input())):
    n, m, k = map(int, input().rstrip().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(k):
        u, v, c, d = map(int, input().rstrip().split())
        u -= 1; v -= 1
        graph[u].append((v, c, d))

    answer = dijkstra()
    print(answer if answer != INF else 'Poor KCM')