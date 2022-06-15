dp = [1] * 30
for i in range(1, 30):
    dp[i] = dp[i-1] * i

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(dp[m] // (dp[m-n] * dp[n]))
