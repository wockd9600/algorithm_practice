import sys
input = sys.stdin.readline
INF = int(10e9)

n = int(input())
arr = [0] + list(map(int, input().rstrip().split()))
dp = [INF] * (n + 1)

for i in range(1, n + 1):
    dp[i] = arr[i]
    
    for j in range(1, i // 2 + 1):
        dp[i] = min(dp[i], dp[i-j] + dp[j])

print(dp[n])
