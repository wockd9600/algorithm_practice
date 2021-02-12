# Prime Number (소수)

import math

n = 1000
prime_bool = [True] * (n + 1)

for i in range(2, int(math.sqrt(n)) +1):
    if prime_bool[i]:
        j = 2
        while i * j <= n:
            prime_bool[i * j] = False
            j += 1

for i in range(n):
    if prime_bool[i]:
        print(i, end=" ")

"""
에라토스테네스의 체
임의의 숫자 n까지의 소수를 구할 때 모든 수를 하나씩 비교하며 소수인지 확인하는 작업은 너무 비효율적이다.
따라서 체에 걸러내듯이 소수가 아닌 것들을 걸러내면 소수만 남게 된다.
시간 복잡도는 NloglogN으로 빠르지만 메모리를 n만큼 잡아 먹는다.
"""
