import sys
input = sys.stdin.readline
INF = int(10e9)

while True:
    n = int(input())
    if n == 0: break

    arr = []
    for _ in range(n): arr.append(int(input()))

    dp = [-INF] * n
    dp[0] = arr[0]
    for i in range(1, n):
        if dp[i-1] < 0: dp[i] = arr[i]
        else: dp[i] = dp[i-1] + arr[i]

    print(max(dp))
