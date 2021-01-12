import sys
from collections import deque
n = int(input())
card = []
for _ in range(n):
    card.append(int(sys.stdin.readline()))

card.sort()

"""
문제점
처음에 받은 카드를 정렬한 후 작은 수 끼리 합치고
다시 합친 카드끼리 합치면 될 줄 알았는데
처음에 합치면서 합쳐도 받은 수보다 작으면 합친 카드를 합쳐야 한다.
예를 들어
1 2 3 4 5 6 7 8 9 를 받았으면
1 + 2 는 3이다. 4보다 작으니까
3 + 3으로 들어가야하는데
구현은 가능하겠지만 무조건 시간초과 날듯

"""

for i in card:
    t.append(i

sum = 0
tsum = 0
if n != 1:
    while True:
        i = 0
        tsum = card[i] + card[i+1]
        while card[i] <= tsum:
            i += 1
        i -= 2
        for j in range(2, len(card)):
            if j == i:
                t.append(tsum)
            t.appned(j)
            
else:
    sum = card[0]
print(sum)
