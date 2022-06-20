n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    s = [0]
    for j in range(i, -1, -1):
        if arr[j] > arr[i]:
            s.append(dp[j])
    
    dp[i] = max(s) + 1

print(max(dp))