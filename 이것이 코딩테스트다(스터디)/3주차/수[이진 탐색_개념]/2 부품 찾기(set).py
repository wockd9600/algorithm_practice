# 전자 매장의 부품 개수, 부품 번호
n = int(input())
materialN = set(list(map(int, input().split())))

# 손님의 요구 부품 개수, 부품 번호
m = int(input())
materialM = sorted(list(map(int, input().split())))

# 손님의 요구하는 부품을 살펴본다.
for m in materialM:
    # 요구하는 부품이 매장에 있으면 yes
    if m in materialN:
        print("yes", end=' ')
    # 없으면 no!
    else:
        print("no", end=' ')

"""
파이썬에서 set은 탐색 문제에 효율적이다.
"""
