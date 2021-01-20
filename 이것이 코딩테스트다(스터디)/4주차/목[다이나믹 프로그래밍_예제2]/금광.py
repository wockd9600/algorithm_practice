T = int(input())
for _ in range(T):
    
    n, m = map(int, input().split())
    gold = list(map(int, input().split()))
    
    dp = []
    index = 0
    for _ in range(n):
        dp.append(gold[index:index + m])
        index += m
    
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[j][i] += max(dp[j][i-1], dp[j+1][i-1])
            elif j == n-1:
                dp[j][i] += max(dp[j][i-1], dp[j-1][i-1])
            else:
                dp[j][i] += max(dp[j][i-1], dp[j+1][i-1], dp[j-1][i-1])

    print(max(dp[i][m-1] for i in range(n)))
