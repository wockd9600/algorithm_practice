n = int(input())
arr = list(map(int, input().split()))
z = list(map(int, input().split()))
zc = sum(z)

maxnum, minnum = -2000000000, 200000000

def bfs(num, z, n):
    if n == zc + 1:
        global maxnum, minnum
        if num < minnum:
            minnum = num
        if num > maxnum:
            maxnum = num
        return

    for i in range(4):
        if z[i] == 0:
            continue
        
        z[i] -= 1
        tnum = 0

        if i == 0:
            tnum = num + arr[n]
        elif i == 1:
            tnum = num - arr[n]
        elif i == 2:
            tnum = num * arr[n]
        else:
            tnum = int(num / arr[n])

        bfs(tnum, z, n+1)
        z[i] += 1

bfs(arr[0], z, 1)
print(maxnum, minnum)
