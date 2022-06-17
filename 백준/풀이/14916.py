INF = int(10e9)

n = int(input())
dp = [INF] * (6)
dp[2], dp[4], dp[5] = 1, 2, 1

for i in range(6, n + 1):
    dp.append(min(dp[i-2], dp[i-5]) + 1)

print(dp[n])