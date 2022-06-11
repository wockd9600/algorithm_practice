import heapq
import sys
input = sys.stdin.readline
INF = int(10e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, 0, start[0], start[1]))

    dp = [[[INF, 0] for _ in range(m)] for _ in range(n)]
    
    dp[start[0]][start[1]] = [0, 0]

    while q:
        dist, smell , x, y = heapq.heappop(q)

        if dist > dp[x][y][0]: continue

        for dx, dy in dmove:
            tx, ty = x + dx, y + dy
            
            if tx < 0 or tx >= n or ty < 0 or ty >= m: continue
            
            cost = 1 if graph[tx][ty] == 'g' else 0
            cost += dist

            smell_cost = trash[tx][ty] + smell

            if cost < dp[tx][ty][0] or (cost == dp[tx][ty][0] and smell_cost < dp[tx][ty][1]):
                dp[tx][ty][0] = cost
                dp[tx][ty][1] = smell_cost
                heapq.heappush(q, (cost, smell_cost, tx, ty))
    
    return dp

dmove = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())

graph = []
s, e = [], []
trash = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(input().rstrip()))

for i in range(n):
    for j in range(m):
        if graph[i][j] == '.': continue
        elif graph[i][j] == 'S': s = [i, j]
        elif graph[i][j] == 'F': e = [i, j]
        elif graph[i][j] == 'g':
            for di, dj in dmove:
                ti, tj = i + di, j + dj
                if ti < 0 or ti >= n or tj < 0 or tj >= m: continue

                if graph[ti][tj] == '.': trash[ti][tj] = 1

dp = dijkstra(s)

print(' '.join(map(str, dp[e[0]][e[1]])))