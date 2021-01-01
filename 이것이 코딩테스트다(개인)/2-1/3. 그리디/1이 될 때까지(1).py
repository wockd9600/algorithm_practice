"""
문제 : 상수 n이 주어지고 -1을 하거나 k의 배수이면 k로 나눌 수 있다.
       n이 1이 되기까지 최소 연산 수는??

아이디어 : k의 배수면 k로 나누고 아니면 -1을 한다. (1)
"""

n, k = map(int, input().split())
c = 0

while True:
    # (1) if, else
    if n % k == 0:
        n //= k
    else:
        n -= 1

    c += 1

    if n == 1:
        break

print(c)
