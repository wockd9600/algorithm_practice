import sys
input = sys.stdin.readline

n = int(input())
l = [0] + list(map(int, input().rstrip().split()))
j = [0] + list(map(int, input().rstrip().split()))

dp = [[0] * 100 for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(100):
        if w < l[i]:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-l[i]] + j[i])

print(dp[n][99])