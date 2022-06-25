import sys
input = sys.stdin.readline

dp = [1, 1, 3, 5] + [0] * (247)
for i in range(4, 251):
    dp[i] = dp[i-1] + dp[i-2] * 2
    
while True:
    try: n = int(input())
    except: break
    print(dp[n])
