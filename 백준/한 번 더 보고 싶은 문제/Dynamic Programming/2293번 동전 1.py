mport sys
# 동전 수, 원하는 금액
n, k = map(int, sys.stdin.readline().split())
# dp cashing
dp =[1] + [0] * k
# 동전 목록
coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline()))

for coin in coins:
    for i in range(1, k + 1):
        # index - coin >= 0이면
        # dp[index] = dp[index] + dp[index - coin] 이다
        if i - coin >= 0:
            dp[i] += dp[i - coin]
print(dp[k])