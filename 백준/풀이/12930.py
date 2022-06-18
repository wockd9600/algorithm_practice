import heapq
import sys
input = sys.stdin.readline
INF = int(10e9)

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, 0, 0, 0, s))
    dp = [[INF] * n for _ in range(n)]

    while q:
        total, dist1, dist2, cnt, now = heapq.heappop(q)

        if cnt >= n: continue
        if total > dp[now][cnt]: continue

        for i in range(n):
            if w1[now][i] == INF: continue

            td1 = dist1 + w1[now][i]
            td2 = dist2 + w2[now][i]
            cost = td1 * td2
            
            if cost < dp[i][cnt]:
                dp[i][cnt] = cost
                heapq.heappush(q, (cost, td1, td2, cnt + 1, i))

    return dp[1]

n = int(input())
w1 = [[INF] * n for _ in range(n)]
w2 = [[INF] * n for _ in range(n)]

for i in range(n):
    temp = input()
    for j in range(n):
        if temp[j] == '.': continue
        w1[i][j] = int(temp[j])

for i in range(n):
    temp = input()
    for j in range(n):
        if temp[j] == '.': continue
        w2[i][j] = int(temp[j])

dp = dijkstra(0)
answer = min(dp)
print(answer if answer != INF else -1)
