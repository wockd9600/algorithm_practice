"""
임의의 행렬에 방문해서 0인지 확인하고 0이라면 접해 있는 0인 부분을 전부 2로 만들고 카운트 1
위와 같이 for으로 모든 행렬 방문
"""

# 입력
n, m = map(int, input().split())
icetool = []

for i in range(n):
    icetool.append(list(map(int, input())))

# 음료수 얼리기
def makeIce(x, y):
    # 얼음틀을 넘어가면 무효
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    # 얼음틀이 비어있지 않다면 무효
    elif icetool[x][y] != 0:
        return 0

    # 얼음틀에 음료수를 넣는다.
    icetool[x][y] = 2

    # 해당 얼음틀 근처에 비어 있는 얼음틀을 찾는다.
    for _ in range(4):
        makeIce(x+1, y)
        makeIce(x-1, y)
        makeIce(x, y+1)
        makeIce(x, y-1)

    # 이곳에 도달하면 적어도 한 개의 얼음틀은 채운 게 된다.
    return 1

# 모든 행렬에 방문해서 적어도 한 개의 얼음틀에 음료수를 넣었으면 카운트한다.
c=0
for x in range(n):
    for y in range(m):
        c = c + 1 if makeIce(x, y) == 1 else c
        
print(c)
# 어떤 모양으로 얼었는지 보여주는 예
for i in range(n):
    print(icetool[i])
