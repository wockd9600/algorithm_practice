"""
최대 공약수를 구하는 함수
a를 b를 나눈 나머지(c)가 0이 아니면 다시
b를 c로 나누고 나머지(d)가 0이면 c가 최대 공약수다.
"""
# Greatest Common Divisor
def GCD(a,b):
    if(b==0):
        return a
    else:
        return GCD(b,a%b)

# lamda (일회용 함수)
# 인수 a, b를 받아와 b가 0이 아니면 gcd(b, a % b)를 실행한다.
gcd = lambda a, b : a if not b else gcd(b, a % b)