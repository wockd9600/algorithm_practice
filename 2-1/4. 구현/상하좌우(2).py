"""
문제 : 어떤 캐릭터가 n x n 행렬에서 움직일 수 있다. 시작 지점이 1,1 라고 한다면
       마지막에 캐릭터는 어디에 있는가. 단, 캐릭터가 n x n 행렬 밖으로 나가려는 행동은 무효처리 된다.

의문점 : 상하좌우(1)와 차이점은?
"""

n = int(input())
move = list(map(str,input().split()))

x,y = 1,1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_type =['L','R','U','D']

for i in move:
    for j in range(len(move_type)):
        if i == move_type[j]:
            tx = x+dx[j]
            ty = y+dy[j]
            
    if tx < 1 or tx > n or ty < 1 or ty > n:
        continue
    else:
        x,y = tx,ty

print(x,y)
