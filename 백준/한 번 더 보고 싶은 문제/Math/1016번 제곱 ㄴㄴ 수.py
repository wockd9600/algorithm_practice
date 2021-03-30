"""
2 3 5 7 11 13 17
4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196
제곱수는 모두 소수의 제곱수로 나타낼 수 있다.
소수의 제곱수를 구한 뒤 list를 만들어 판별해준다.
"""
import math

#min, max
a, b = map(int, input().split())

# 구해야할 소수 범위
n = int(math.sqrt(b))

# 에라토스테네스의 체로 소수들을 걸러낸다.
check = [True] * (n + 1)
for i in range(2, int(math.sqrt(n))+1):
    if check[i]:
        for j in range(2*i, n+1, i):
            check[j] = False

# 걸러낸 소수를 제곱수로 만들어 list에 저장한다.
prime_list = []
for i in range(2, n+1):
    if check[i]:
        prime_list.append(i*i)

#min~max 범위의 판별 리스트를 만든다.
c = [1] * (b - a + 1)
# 소수 제곱수로 나눌 수 있는 수를 제외 시켜준다.
for i in prime_list:
    """ 이런 테크닉이 아직 부족하다
    a(min)를 i(제곱수)로 나누면 몫 j를 얻을 수 있다.
    이때 j는 x.xxx로 도출되는데 .xxx값이 0이라면
    a는 i로 딱 나누어 떨어지고 a는 제곱수(i)의 배수이다.
    딱 떨어지지 않으면 쓰레기 값이 생기는데 이때 ceil(올림)을 해준다.
    그리고 j*i를 해주면 min보다 큰 첫번째 제곱수의 배수를 얻을 수 있다.
    """
    j = math.ceil(a / i)
    while i * j <= b:
        c[i * j - a] = 0
        j += 1

print(sum(c))
