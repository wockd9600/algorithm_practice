n = int(input())
dp = [0, 1] + [int(10e9)] * (n - 1)

for i in range(2, n + 1):
    j = 1

    while j ** 2 <= i:
        dp[i] = min(dp[i], dp[i - (j ** 2)] + 1)
        j += 1

print(dp[n])

5
4


20
19