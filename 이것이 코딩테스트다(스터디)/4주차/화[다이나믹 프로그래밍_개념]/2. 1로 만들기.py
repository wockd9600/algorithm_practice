x = int(input())
dp = [0] * 30001
dp[0] = 30000
dp[2] = 1

for i in range(3, x + 1):
    t5 = i // 5 if i % 5 == 0 else 0
    t3 = i // 3 if i % 3 == 0 else 0
    t2 = i // 2 if i % 2 == 0 else 0
    t1 = i - 1
    dp[i] = 1 + min(dp[t5], dp[t3], dp[t2], dp[t1])

print(dp[x])
