import sys
input = sys.stdin.readline
INF = int(2e14)

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

dp = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(r):
    a, b, c = map(int, input().split())
    dp[a][b] = c
    dp[b][a] = c

for node in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if start == end: dp[start][end] = 0
            if dp[start][end] > dp[start][node] + dp[node][end]:
                dp[start][end] = dp[start][node] + dp[node][end]

answer = 0
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if dp[i][j] <= m: cnt += items[j-1]

    answer = max(answer, cnt)    

print(answer)
