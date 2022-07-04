import sys
input = sys.stdin.readline

d, k = map(int, input().rstrip().split())
dp = [0] * (d + 1)
dp[1], dp[2] = 1, 1

for i in range(3, d + 1):
    dp[i] = dp[i-1] + dp[i-2]

a, b = dp[d-2], dp[d-1]

for i in range(1, k + 1):
    t = k - (a * i)
    
    if t % b == 0:
        print(i)
        print(t // b)
        break
