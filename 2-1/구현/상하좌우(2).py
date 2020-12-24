import time

start = time.time()

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


finish = time.time()

print(finish - start)
