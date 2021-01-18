"""
왜 세로모양은 i-2에 적용이 안될
"""

n = int(input())
dp = [0] * (n + 1)

dp[1] = 1

for i in range(2, n + 1):
    if i % 2 == 0:
        dp[i] = (dp[i-1] * 2 + 1) % 796796 
    else:
        dp[i] = (dp[i-1] * 2 - 1) % 796796

print(dp[n])

