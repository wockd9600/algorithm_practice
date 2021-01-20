n = int(input())
sol = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i + 1, n):
        if sol[i] > sol[j] and dp[i] + 1 > dp[j]:
            dp[j] = dp[i] + 1

print(n - max(dp))
