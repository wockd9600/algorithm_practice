import heapq
import sys
input = sys.stdin.readline
INF = int(10e9)

def changeToNumberList(arr):
    temp = []
    for a in arr:
        ao = ord(a)
        if ao < 91: temp.append(ao-65)
        else: temp.append(ao-97+26)
    return temp


def dijkstra(r):
    q = []
    heapq.heappush(q, (0, 0, 0))

    dp = [[INF] * m for _ in range(n)]
    dp[0][0] = 0

    while q:
        dist, x, y = heapq.heappop(q)

        if dist > dp[x][y]: continue

        for dx, dy in dmove:
            tx, ty = x + dx, y + dy
            if tx < 0 or tx >= n or ty < 0 or ty >= m: continue
            if abs(graph[tx][ty] - graph[x][y]) > t: continue
            
            if r:
                cost = 1 if graph[tx][ty] >= graph[x][y] else (graph[tx][ty] - graph[x][y]) ** 2
            else:
                cost = 1 if graph[tx][ty] <= graph[x][y] else (graph[tx][ty] - graph[x][y]) ** 2

            cost += dist
            if cost < dp[tx][ty]:
                dp[tx][ty] = cost
                heapq.heappush(q, (cost, tx, ty))
    
    return dp

dmove = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m, t, d = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(changeToNumberList(list(input().rstrip())))

dp = dijkstra(0)
dp_r = dijkstra(1)

answer = 0
for i in range(n):
    for j in range(m):
        time = dp[i][j] + dp_r[i][j]
        if time <= d and graph[i][j] > answer:
            answer = graph[i][j]

print(answer)