import sys
# 높이 입력
N = int(input())
# 삼각형의 모양 입력
t = [ list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 삼각형의 두 번째부터 맨 아래까지 가장 커질 수 있는 경우의 수만 가지고 내려온다.
for i in range(1, N):
    for j in range(i+1):
        # 맨 왼쪽에 있는 수들은 반드시 맨 왼쪽에 있는 수만 가지고 내려온다.
        if j == 0:
            t[i][j] = t[i-1][j] + t[i][j]
        # 맨 오른쪽에 있는 수들은 반드시 맨 오른쪽에 있는 수만 가지고 내려온다.
        elif j == i:
            t[i][j] = t[i-1][j-1] + t[i][j]
        # 나머지는 왼쪽과 오른쪽 중 큰 수를 가지고 내려온다.
        else:
            t[i][j] = max(t[i-1][j-1], t[i-1][j]) + t[i][j]

print(max(t[N-1]))
