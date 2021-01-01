"""
문제 : 어떤 캐릭터가 n x n 행렬에서 움직일 수 있다. 시작 지점이 1,1 라고 한다면
       마지막에 캐릭터는 어디에 있는가. 단, 캐릭터가 n x n 행렬 밖으로 나가려는 행동은 무효처리 된다.

의문점 : 모범 답안으로 상하좌우(2) 가 제공되어 있는데 더 효율적인 건지 잘 모르겠다.
"""

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
