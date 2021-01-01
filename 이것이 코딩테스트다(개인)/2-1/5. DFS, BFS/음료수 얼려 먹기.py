n, m = map(int, input().split())
icetool = []

for i in range(n):
    icetool.append(list(map(int, input())))

print(icetool)
        
def makeIce(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    elif icetool[x][y] != 0:
        return 0

    icetool[x][y] = 2
    
    for _ in range(4):
        makeIce(x+1, y)
        makeIce(x-1, y)
        makeIce(x, y+1)
        makeIce(x, y-1)

    return 1

c=0
for x in range(n):
    for y in range(m):
        c = c + 1 if makeIce(x, y) == 1 else c
        
print(c)
for i in range(n):
    print(icetool[i])
