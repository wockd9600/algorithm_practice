"""
문제 : 체스에서 나이트의 위치가 주어질 때 움직일 수 있는 경우의 수는?

아이디어 : 일단 움직이고 나서 체스판을 벗어나는지 확인한다. (1)
"""

# 나이트의 위치
loc = input()
x = int(ord(loc[0])) - 96
y = int(loc[1])

    #      UL 0     UR 1     RU 2     RL 3    DR 4    DL 5     LD 6      LU 7    
moves = [(-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1)]

c = 0
for move in moves:
    #(1)
    t1 = x + move[0]
    t2 = y + move[1]

    if t1 >= 1 and t1 <= 8 and t2 >= 1 and t2 <= 8:
        c+=1

print(c)
