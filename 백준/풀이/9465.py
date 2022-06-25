import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    cardt = list(map(int, input().rstrip().split()))
    cardb = list(map(int, input().rstrip().split()))

    dp = [[0] * 2 for _ in range(n)]
    dp[0][0], dp[0][1] = cardt[0], cardb[0]
    
    if n == 2:
        dp[1][0] = cardt[0] + cardb[1]
        dp[1][1] = cardt[1] + cardb[0]
    else:
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1], dp[i-2][1]) + cardt[i]
            dp[i][1] = max(dp[i-1][0], dp[i-2][0]) + cardb[i]

    print(max(dp[n-1][0], dp[n-1][1]))
