import sys
input = sys.stdin.readline
INF = int(10e9)

n = int(input())
e = [0]
for _ in range(n - 1):
    e.append(list(map(int, input().rstrip().split())))
k = int(input())
dp = [[INF] * (n + 3) for _ in range(n + 3)]
for i in range(n): dp[1][i] = 0
for i in range(1, n):
    for j in range(1, n):
        if i == j: dp[i+3][j] = min(dp[i+3][j], dp[i][j] + k)
        dp[i+1][j] = min(dp[i+1][j], dp[i][j] + e[i][0])
        dp[i+2][j] = min(dp[i+2][j], dp[i][j] + e[i][1])

print(min(dp[n]))
