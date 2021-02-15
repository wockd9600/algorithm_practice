# 화페 종류 수, 목표 금액
n, m = map(int, input().split())

# 화폐 종류 입력
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()

# index 금액까지 최소 경우의 수 dp
dp = [-1] * (m + 1)

# 목표 금액 m보다 큰 coin은 사용x, coin이 있으면 최소 경우의 수를 1로 초기화
for coin in coins:
    if coin > m:
        break
    dp[coin] = 1

# 특정 금액 만들기
for i in range(coins[0], m + 1):
    if dp[i] == -1: # i금액을 만들 수 없으면 다음으로 넘어간다.
        continue

    #dp[i]에는 항상 i금액이 되기 위한 최소의 경우의 수가 저장되어 있다.
    
    for coin in coins:
        t = i + coin
        # t금액이 만들어진 적이 없거나 dp[t]보다 dp[i] + 1가 더 작으면 바꿔준다.
        if t < m + 1 and (dp[t] == -1 or dp[t] > dp[i] + 1):
            dp[t] = dp[i] + 1

print(dp[m])
