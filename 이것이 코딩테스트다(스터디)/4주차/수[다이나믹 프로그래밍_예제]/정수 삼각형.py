import sys

N = int(input())
t = [ list(map(int, sys.stdin.readline().split())) for _ in range(N)]


for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            t[i][j] = t[i-1][j] + t[i][j]
        elif j == i:
            t[i][j] = t[i-1][j-1] + t[i][j]
        else:
            t[i][j] = max(t[i-1][j-1], t[i-1][j]) + t[i][j]

print(max(t[N-1]))
