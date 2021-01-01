"""
작은 수부터 [a]까지 더한 수보다 [a+1]의 수가 더 크면
a에 1을 더한 값을 만들 수 없다.

"""
# 입력
n = int(input())
coins = sorted(list(map(int, input().split())))

num = 1
for coin in coins:
    if num < coin: break
    num += coin

print(num)
