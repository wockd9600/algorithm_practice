"""
테이블이 W개씩 H행이 있을 때
세로로 N칸, 가로로 M칸을 비우고 앉아야 한다.
"""

h, w, n, m = map(int, input().split())
answer = 0

i, j = 0, 0

while i < h:
    while j < w:
        answer += 1        
        j += (m + 1)
    i += (n + 1)
    j = 0

print(answer)

"""
hn = (h + n) // (1 + n)
wm = (w + m) // (1 + m)
칸을 간격 +1로 나누고 반올림함
왜 이렇게 되지

print(hn * wm)
"""