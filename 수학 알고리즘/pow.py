"""
제곱할 때 사용하는 함수다. python에 이미 내장 되어 있다.
제곱할 때 3^5을 곱하기보다 5를 2진수로 바꿔서 곱해주는 게 훨씬 빠르다고 한다.
"""

# x^y
def pow(x, y):
    r = 1
    while y > 0:
        if y % 2 == 1:
            r *= x
        y //= 2
        x = x**2
    return r

print(pow(int(input()), int(input())))
