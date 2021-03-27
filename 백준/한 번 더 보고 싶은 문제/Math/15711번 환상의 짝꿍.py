"""
두 수의 합을 소수로 나눌 수 있는 방법은
1. 합이 3보다 큰 짝수이다. (골든 바흐의 추측)
2. 합 -2가 소수이다. (합이 홀수라면 홀수 + 짝수 조합인데 짝수인 소수는 2 밖에 없다)

합 - 2가 소수인지 판별하면 되는데 수가 너무 커서 에라토스테네스의 체로 할 수 있을 거 같지 않았다.
(꾸겨넣으니까 되는 거 같긴한데 시간제한이 1초라 그것도 안될 줄 알았음.)
그래서 소수를 판별하는 수학적 지식을 습득했다.
"""
import math

# x^y%m
def powmod(x, y, m):
    r = 1
    while y > 0:
        if y % 2:
            r = (r * x) % m
        y //= 2
        x = x**2 % m
    return r

# 밀러 라빈 소수 판별법 (자세한 설명 x)
def miller_rabin(n, a):
    d = (n - 1) // 2
    while (d % 2 == 0):
        if (powmod(a, d, n) == n-1):
            return True
        d //= 2
    tmp = powmod(a, d, n)
    return True if tmp == n-1 or tmp == 1 else False


def isPrime(n):
    if n <= 1:
        return False
    if n <= 10000:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
        
    for a in alist:
        if not miller_rabin(n, a):
            return False
    return True


t = int(input())
alist = [2, 7, 61]
for _ in range(t):
    # 두 수 입력
    a, b = map(int, input().split())
    # 두 수의 합
    n = a + b
    # 두 수의 합이 4보다 작으면 인연x
    if n < 4:
        print('NO')
    # 두 수의 합이 4보다 큰 짝수면 인연o
    elif n % 2 == 0:
        print("YES")
    # 두 수의 합이 홀 수라면 밀러 라빈 소수 판별법 이용
    else:
        n -= 2
        print('YES' if isPrime(n) else 'NO')
