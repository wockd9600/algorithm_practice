"""
난이도 2단계라기엔 좀 쉬웠음 차라리 바닥 공사가 더 어려운듯..
난이도를 정하는 기준이 뭐
"""

n = int(input())
w = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = w[0]
dp[2] = max(w[1], w[0])

for i in range(3, n + 1):
    dp[i] = max(dp[i-1], dp[i-2] + w[i-1])

print(dp[n])
