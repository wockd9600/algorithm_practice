# 임의의 수 n과 나눌 수 k를 받는다.
n, k = map(int, input().split())
c = 0

while True:
    # k로 나눌 수 있으면 나눈다.
    if n % k == 0:
        n //= k
        c += 1
    # k로 나눌 수 없으면 나눌 수 있는 수 있는 수로 만든다.
    else:
        t = n % k
        n -= t
        c += t

    if n == 0:
        break

# 마지막에 0으로 만들었으니 +1을 해준다.
# => 1에서 0이 될 땐 항상 -1임.
print(c - 1)
