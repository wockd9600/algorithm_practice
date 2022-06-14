import heapq
import sys
input = sys.stdin.readline
INF = int(10e9)

def dijkstra():
    q = []
    r = 1 if circuit[0][0] == 1 else 0
    heapq.heappush(q, (r, r, 0, 0))


    dp = [[[INF for _ in range(m)] for _ in range(n)] for _ in range(2)]
    dp[r][0][0] = r

    while q:
        dist, rotate, x, y = heapq.heappop(q)

        if dist > dp[rotate][x][y]: continue

        for i in range(8):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or tx >= n or ty < 0 or ty >= m: continue

            cost, next_rotate = dist, 0
            
            if i < 2:
                if abs(circuit[x][y] - rotate) == 0: continue
                elif circuit[tx][ty] == 0:
                    cost += 1
                    next_rotate = 1
            if 2 <= i < 4:
                if abs(circuit[x][y] - rotate) == 1: continue
                elif circuit[tx][ty] == 1:
                    cost += 1
                    next_rotate = 1
                  
            if i >= 4 and abs(circuit[x][y] - rotate) == circuit[tx][ty]:
                cost += 1
                next_rotate = 1

            if cost < dp[next_rotate][tx][ty]:
                dp[next_rotate][tx][ty] = cost
                heapq.heappush(q, (cost, next_rotate, tx, ty))

    if circuit[n-1][m-1]: dp[0][n-1][m-1] = INF
    else: dp[1][n-1][m-1] = INF
    
    return dp

dx = [-1, 1, -1, 1, 1, 0, -1, 0]
dy = [1, -1, -1, 1, 0, 1, 0, -1]

n, m = map(int, input().split())
circuit = [[] for _ in range(n)]

for i in range(n):
    for j in input().rstrip():
        circuit[i].append(1 if j =='/' else 0)

dp = dijkstra()

answer = min(dp[1][n-1][m-1], dp[0][n-1][m-1])

print(answer if answer != INF else "NO SOLUTION")
