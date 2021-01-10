"""
1초마다 바이러스가 퍼지는 함수를 만든다.
"""
from collections import deque

# 행렬 모양, 바이러스 개수
n, k = map(int, input().split())

# 시험관 정보
test = []
# 각 바이러스 위치 정보
graph = [[] for _ in range(k+1)]

# 1. 시험관 정보의 입력
# 2. 바이러스의 위치 정보 입력
for i in range(n):
    arr = list(map(int, input().split()))
    test.append(arr)
    for j in range(n):
        if arr[j] != 0:
            graph[arr[j]].append([i, j])

# 몇 초 뒤, x, y의 바이러스
s, x, y = map(int, input().split())

#     R  D  L   U
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 바이러스의 위치 정보를 바이러스 번호 순으로 큐에 넣는다.
queue = deque([])
# 바이러스의 총 개수
p = 0
# 바이러스의 위치 정보를 큐에 넣는다.
for i in range(1, k+1):
    for j in graph[i]:
        queue.append(j)
        p += 1

# 감염 시작, 시간이 되면 멈추게 설정
t = 0
while t != s:
    # 방문해야 하는 위치의 개수를 저장
    # 처음엔 바이러스의 총 개수, 두 번째부턴 감염 시킨 바이러스의 개수다.
    c = p
    p = 0
    for _ in range(c):
        a, b = queue.popleft()
        for i in range(4):
            tx = a + dx[i]
            ty = b + dy[i]
            # 감염시키려는 위치가 시험관 내부이면서 감염되지 않은 공간이어야 한다.
            if  (0 <= tx and tx < n) and (0 <= ty and ty < n) and test[tx][ty] == 0:
                test[tx][ty] = test[a][b]
                queue.append([tx, ty])
                p += 1
    t += 1

print(test[x-1][y-1])
