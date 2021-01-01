"""
https://blog.naver.com/wockd9600/222185492118
문제 : 교재 118p

아이디어 : 1번 상황 2번 상황 3번 상황을 모두 차례대로 진행한다.
"""

# 행렬의 모양을 입력 받는다.
n, m = map(int, input().split())
# 현민이의 최초 위치(a, b), 방향(d)을 입력 받는다.
a, b, d = map(int, input().split())
# 맵의 지형을 입력 받는다.
gameMap = [list(map(int, input().split())) for _ in range(m)]



# 현민이가 왼쪽으로 움직일 때와 뒤로 움직일 때 값을 설정한다.
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 보고 있는 방향별 맵 한계치
mapLimmit = [n, m, n, m]


# c로 몇 번 회전했는지 확인한다.
c=0
# 현민이가 최초 위치 방문.
gameMap[a][b] = 2
visit = 1


#시작
while True:
    
    # 왼쪽으로 회전
    d = 3 if d == 0 else d - 1
    
    # 현민이가 앞으로 갔다고 가정
    ta = a + moves[d][0]
    tb = b + moves[d][1]

    # 만약 현민이가 왼쪽으로 움직였을 때 해당 위치가 방문할 수 있고(값이 0이고) 맵의 한계 값을 넘지 않으면
    if gameMap[ta][tb] == 0 and ta >= 1 and ta <= mapLimmit[d] and tb >= 1 and tb <= mapLimmit[d]:
        # 해당 위치 확정, 방문, 회전 수 초기화
        gameMap[ta][tb] = 2
        a, b = ta, tb
        c = 0
        visit += 1
    # 방향만 바꾸고 회전 횟수를 카운트한다.
    else:
        c += 1

    # 회전 횟수가 4번일 경우 방문할 곳이 없다. 따라서 해당 방향에서 뒤로 움직인다.
    if c >= 4:
        a = a - moves[d][0]
        b = b - moves[d][1]
        # 만약 뒤가 바다거나(1) 맵의 한계치를 넘으면 종료한다.
        if gameMap[a][b] == 1 or a < 1 or a > mapLimmit[d] or b < 1 or b > mapLimmit[d]:
            break
        c = 0
    
    
print(visit)
