import sys
input = sys.stdin.readline

n, s, m = map(int, input().rstrip().split())
v = list(map(int, input().rstrip().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1

for i in range(1, n + 1):
    for j in range(m + 1):
        if dp[i-1][j]:
            for x in [j + v[i-1], j - v[i-1]]:
                if 0 <= x <= m:
                    dp[i][x] = 1

answer = -1
for i in range(m, -1, -1):
    if dp[n][i]:
        answer = i
        break

print(answer)
