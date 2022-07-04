import sys
input = sys.stdin.readline

n = int(input())
m = int(input())


dp = [[0] * 2 for _ in range(n + 1)]
dp[0][0], dp[1][1] = 1, 1

for i in range(2, n + 1):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = dp[i-1][1] + dp[i-1][0]

answer = 1
s = 0
for _ in range(m):
    i = int(input())
    answer *= sum(dp[i-s-1])
    s = i

print(answer * sum(dp[n-s]))
