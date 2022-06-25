import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 0, 1, 0, 1] + [0] * (n - 4)

for i in range(5, n + 1):
    t = sum([dp[i-1], dp[i-3], dp[i-4]])

    if t == 3: dp[i] = 0
    else: dp[i] = 1

print('SK' if dp[n] else 'CY')
