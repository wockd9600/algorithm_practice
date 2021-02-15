"""
장애물 3개를 bfs로 세우고
선생의 시선에 학생이 발견되는지 확인한다.
"""
from collections import deque

# 선생님의 감시
def teachers_eye(x, y):
    # 선생님이 4방향을 감시
    for i in range(4):
        queue.append([x, y])
        # 한 방향씩 시야가 막힐 때까지 감시
        while queue:
            a, b = queue.popleft()
            tx = a + dx[i]
            ty = b + dy[i]
            # 복도의 범위를 넘지 않고
            if (0 <= tx and tx < n and 0 <= ty and ty < n):
                if hall[tx][ty] == 'X': # 비어 있다면 다음 칸도 감시
                    temp[tx][ty] = 'T'
                    queue.append([tx, ty])
                elif temp[tx][ty] == 'S': # 학생이 있다면
                    while queue:
                        queue.popleft()
                    return True
                
    # 학생을 못찾으면 이곳에 도달
    return False

def bfs(c):
    if c != 3:
        # 장애물 세우기
        for x in range(n):
            for y in range(n):
                if hall[x][y] == 'X':
                    hall[x][y] = 'O'
                    look_success = bfs(c+1)
                    hall[x][y] = 'X'
                    # 선생님이 학생 찾기를 성공하지 못하면
                    if not look_success:
                        return False
        return True
    
    # 장애물을 3개 설치 했다면
    else:
        # 임시 복도 temp 생성
        for x in range(n):
            for y in range(n):
                temp[x][y] = hall[x][y]
        # 선생님 찾기
        for x in range(n):
            for y in range(n):
                 # 찾으면 감시 시작
                if hall[x][y] == 'T':
                    look_student = teachers_eye(x, y)
                    # 들켰으면 다음 장애물 케이스로
                    if look_student:
                        return True
                    # 안 들켰으면 다음 선생님의 감시

        # 모든 선생님의 감시에서 들키지 않으면
        return False
    
# 복도의 크기
n = int(input())
# 복도 정보
hall = []
for _ in range(n):
    hall.append(list(input().split()))
# 임시 복도
temp =[[0] * n for _ in range(n)]

queue = deque([])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 선생님이 학생 찾기를 성공하지 못하면
if not bfs(0):
    print("YES")
# 성공하면
else:
    print("NO")
                    
