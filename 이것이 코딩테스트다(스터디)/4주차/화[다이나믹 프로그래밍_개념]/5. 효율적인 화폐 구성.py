n, m = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()

dp = [-1] * (m + 1)

for coin in coins:
    if coin > m:
        break
    dp[coin] = 1

for i in range(coins[0], m + 1):
    if dp[i] == -1:
        continue

    for coin in coins:
        t = i + coin
        if t < m + 1 and (dp[t] == -1 or dp[t] > dp[i] + 1):
            dp[t] = dp[i] + 1

print(dp[m])
