"""
밀러 라빈 소수 판별법
말로 설명하기 어려우니 구글 검색

n이 소수일 때 (n>3) n-1은 짝수이다.
n-1은 임의의 홀수 d와 s에 대해 다음과 같이 나타낼 수 있다.

n-1 = d * 2^s
근거 : 짝수는 약수로 반드시 2를 포함하고 있음.

a ^ (d * 2 ^ (r - 1)) % n 이 -1 이거나
a ^ d % n 이 1 or - 1이면 n은 홀수임.
증명은 구글 검
"""

# x^y%m
def powmod(x, y, m):
    r = 1
    while y > 0:
        if y % 2:
            r = (r * x) % m
        y //= 2
        x = x**2 % m
    return r

def miller_rabin(n, a):
    d = (n - 1) // 2
    while (d % 2 == 0):
        if (powmod(a, d, n) == n-1):
            return True
        d //= 2
    tmp = powmod(a, d, n)
    return True if tmp == n-1 or tmp == 1 else False

print(miller_rabin(int(input()), int(input())))
