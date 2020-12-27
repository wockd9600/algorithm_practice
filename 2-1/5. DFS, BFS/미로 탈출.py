"""
문제 풀이
1. queue에 어떻게 2차원 배열을 적용할까? => x, y를 넣는다.
2. 이동하는 법은 구현에서 배웠던 dx, dy를 적용.
"""

from collections import deque

# 행렬 모양을 받는다.
n, m = map(int, input().split())

# N x M 행렬을 받는다.
miro = []
for i in range(n):
    miro.append(list(map(int, input())))

# 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 미로 탈출
def exit_miro(x, y):
    # 큐 생성
    queue = deque()
    queue.append((x, y))

    # 시작 (큐가 빌 때까지 반복한다)
    while queue:
        # 현재 위치를 큐에서 꺼낸다.
        x, y = queue.popleft()

        # 네 방향 모두 검사
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            # N x M 행렬을 벗어나면 방문x
            if tx < 0 or ty < 0 or tx >=n or ty >= m:
                continue

            # 괴물 있는 곳 방문x
            if miro[tx][ty] == 0:
                continue

            # 해당 노드 첫 방문시
            if miro[tx][ty] == 1:
                # 해당 노드에 전 노드에 저장된 값 +1
                miro[tx][ty] = miro[x][y] + 1
                # 큐에 해당 노드 넣
                queue.append((tx, ty))

    return miro[n -1][m - 1]

print(exit_miro(0, 0))
