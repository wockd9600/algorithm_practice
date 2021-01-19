n = int(input())
c = []
for _ in range(n):
    c.append(list(map(int, input().split())))

dp = [0] * (n + 1)


for i in range(n):    
    if dp[i+1] < dp[i]:
        dp[i+1] = dp[i]
        
    t = c[i][0] + i
    
    if t > n:
        continue
    
    p = c[i][1] + dp[i]

    if dp[t] < p:
        dp[t] = p

print(dp[n])
