"""
pow 참고

"""

# x ^ y % m
def powmod(x, y, m):
    r = 1
    while y > 0:
        if y % 2 == 1:
            r *= x
            r %= m
        y //= 2
        x = x**2
        x %= m
    return r

print(powmod(int(input()), int(input()), int(input())))
