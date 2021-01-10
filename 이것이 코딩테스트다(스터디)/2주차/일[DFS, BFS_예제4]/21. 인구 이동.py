from collections import deque
import sys
input = sys.stdin.readline

# 연합 시키기
def union(x, y):
    move_q = deque() # 연합이 된 나라 위치
    people, cnt = 0, 0 # 연합의 총 인구, 연합의 나라 수
    
    visited[x][y] = 1 # 연합에 추가
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        move_q.append([x, y])
        people += country[x][y]
        cnt += 1
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            # 땅을 벗어나지 않고
            if 0 <= tx < n and 0 <= ty < n and not visited[tx][ty]:
                # 인구 차가 범위 내에 있으면
                if l <= abs(country[x][y] - country[tx][ty]) <= r:
                    visited[tx][ty] = cnt
                    queue.append([tx, ty])

    # 연합에 추가 했던 나라들 인구 이동
    while move_q:
        x, y = move_q.popleft()
        country[x][y] = people // cnt

    # 연합 생성 실패 시 0 리턴
    if cnt == 1:
        return 0
    # 성공 시 1 리턴
    return 1

# 땅 크기, 연합이 될 수 있는 최소 인구 차이, 최대 인구 차이
n, l, r = map(int, input().split())
# 땅 정보
country = []
for _ in range(n):
    country.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 인구 이동 횟수
ans = 0

while True:
    queue = deque()
    visited = [[0]*n for _ in range(n)] # 연합 참가 여부
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += union(i, j)

    # 더 이상 만들 연합이 없으면 반복 종료
    if not cnt:
        break
    ans += 1

print(ans)
