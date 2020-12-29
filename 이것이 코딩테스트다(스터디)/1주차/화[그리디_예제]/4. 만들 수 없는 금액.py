n = int(input())
coins = sorted(list(map(int, input().split())))

num = 1
for coin in coins:
    if num < coin: break
    num += coin

print(num)
