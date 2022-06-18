n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    s = 0
    for j in range(i, -1, -1):
        if arr[i] > arr[j]:
            s = max(s, dp[j])

    dp[i] = arr[i] + s

print(max(dp))
