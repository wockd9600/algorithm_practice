# 기둥과 보가 두 개 다 있는 경우 때문에 코드가 길어짐..
def checkWall(x, y, type):
    if type == 1:
        if wall[x][y] == 0 or wall[x][y] == 2:
            return True
    else:
        if wall[x][y] == 1 or wall[x][y] == 2:
            return True
    return False

# 벽에 주어진 위치의 보나 기둥을 설치한다.
def build(type, x, y):
    # 보 설치
    if type == 1:

        # 바닥이면 설치x
        if y <= 0:
            return
                
        # 설치하려는 위치에 기둥이 있으면 설치
        if checkWall(x, y-1, 1):
            # 설치하려는 위치 위에도 기둥이 있다면
            # 해당 좌표에 기둥과 보가 있다는 의미로 2를 입력
            wall[x][y] = 2 if wall[x][y] == 0 else 1

        # 설치하려는 위치 오른쪽에 기둥이 있으면 설치
        elif checkWall(x+1, y-1, 1):
            wall[x][y] = 2 if wall[x][y] == 0 else 1
                    
        # 해당 위치의 왼쪽에도 보가 있고 오른쪽에도 보가 있으면 설치
        elif (checkWall(x-1, y, 1)) and (checkWall(x+1, y, 1)):
            wall[x][y] = 1

    # 기둥 설치
    else:
        # 해당 위치가 바닥이면 설치
        if y == 0:
            wall[x][y] = 0

        # 해당 위치에 기둥이 있으면 설치
        elif checkWall(x, y-1, 0):
            # 원래 보가 있던 자리면 2
            wall[x][y] = 2 if wall[x][y] == 1 else 0

        # 해당 위치 왼쪽에 보가 있으면 설치
        elif x != 0 and (checkWall(x-1, y, 0)):
            wall[x][y] = 2 if wall[x][y] == 1 else 0


#벽에서 주어진 위치의 보나 기둥을 삭제한다.
def delete(type, x, y):
    # 보 삭제
    if type == 1:
                
        # 삭제하려는 위치 오른쪽에 보가 없으면 삭제x
        if checkWall(x+1, y, 1) or checkWall(x+1, y-1, 1):
            return

        # 삭제하려는 위치에 기둥이 있고 왼쪽에 아무 것도 없으면 삭제 x
        if x != 0 and wall[x][y] == 2 and !checkWall(x-1, y, 1):
            return

        # 해당 위치에 보와 기둥이 있었으면 보만 삭제한다.
        wall[x][y] = 0 if wall[x][y] == 2 else 3

    # 기둥 삭제
    else:
        # 기둥 위에 기둥만 있으면 삭제x
        if wall[x][y+1] == 1:
            return

        # 기둥 왼쪽 위에 보가 있어도 삭제 x
        elif x != 0 and (wall[x-1][y+1] == 1 or wall[x-1][y+1] == 2):
            return
        # 기둥 위에 보가 있어도 삭제 x
        elif wall[x][y+1] == 1 or wall[x][y+1] == 2:
            return
                    
        wall[x][y] = 0 if wall[x][y] == 2 else 0 


def solution(n, build_frame):
    # 임시 벽을 만든다.
    wall = [[3] * (n+1) for _ in range(n+1)]

    # 벽에 기둥과 보를 설치하자.
    for build in build_frame:
        
        # x, y, 기둥(0) or 보(1), 설치(0) or 삭제(1)
        x, y = build[0], build[1]
        type, func = build[2], build[3]

        # 설치
        if func == 1:
            build(type, x, y)
            
        # 삭제
        else:
            delete(type, x, y)

    answer = []
    print(wall)
    # 건축 결과 배열에 추가
    for x in range(n):
        for y in range(n):
            if wall[x][y] != 3:
                if wall[x][y] == 2:
                    answer.append([x, y, 0])
                    answer.append([x, y, 1])
                else:
                    if wall[x][y] == 1:
                        answer.append([x, y, 1])
                    else:
                        answer.append([x, y, 1])
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    print(answer)
    return answer
n = int(input())
arr = []
while True:
    t = list((map(int, input().split())))
    if len(t) < 4:
        break
    arr.append(t)
solution(n, arr)
