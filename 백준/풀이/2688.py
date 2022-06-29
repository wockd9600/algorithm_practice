import sys
input = sys.stdin.readline

dp = [[0] * (10) for _ in range(65)]
for i in range(10): dp[1][i] = 1

for i in range(2, 65):
    for j in range(10):
        for k in range(j, 10):
            dp[i][k] += dp[i-1][j]

for _ in range(int(input())):
    n = int(input())
    print(sum(dp[n]))
