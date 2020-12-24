import time

start = time.time()

n = int(input())
move = input().split()
a = [1, 1]

for i in move:
    if i == 'U':
        if a[0] == n+1: continue
        a[0] -= 1

    elif i == 'D':
        if a[0] == n+1: continue
        a[0] += 1

    elif i == 'L':
        if a[1] == n+1: continue
        a[1] -= 1

    else:
        if a[1] == n+1: continue
        a[1] += 1

print(a)

finish = time.time()

print(finish - start)
