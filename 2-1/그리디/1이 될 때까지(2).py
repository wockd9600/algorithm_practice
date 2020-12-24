n, k = map(int, input().split())
c = 0

while True:
    if n % k == 0:
        n //= k
        c += 1
    else:
        cc = n % k
        n -= cc
        c += cc

    if n == 1:
        break

print(c)
