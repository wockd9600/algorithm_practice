#List

arr = [i * i for i in range(1, 10 +1) if i % 2 == 0] # (1)

arr = [[i for i in range(10 +1)] for j in range(10)] # (2)
arr = [[0] * 10] * 10

a = [i for i in range(1, 10 +1)] # (3)
remove_values = {3, 4, 5}
arr = [i for i in a if i not in remove_values]


"""
# 1
파이썬에서 리스트를 초기화할 때 조건문과 반복문을 사용할 수 있다.


# 2
1. 2차원 배열 초기화 방식
2. 이런 식으로 초기화하면 2차원 배열이 아니라 동일한 1차원 배열을 10개 생성하는 것이다.


# 3
배열에서 특정한 값을 지워주고 싶을 때

# *
튜플은 리스트에 비해 공간 효율적이다.
"""


#Library

data = ['a', 'b', 'c']
from itertools import permutations # (1)
permu = list(permutations(data, 3))

from itertools import combinations
combi = list(combinations(data, 2))

from itertools import product
prod = list(product(data, repeat=2))

from itertools import combinations_with_replacement
cwr = list(combinations_with_replacement(data, 2))

"""
# 1
반복되는 데이터를 처리
1. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a') ...]
2. [('a', 'b'), ('a', 'c'), ('b', 'c')]
3. [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c') ...]
4. [('a', 'a'), ('a', 'b'), ('b', 'b'), ('b', 'c'), ('c', 'c')]
"""


import heapq # (2)

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
result = heapsort([1, 4, 2, 6, 7])

"""
# 2
우선순위 큐 기능을 구현하고자 할 때 사용
파이썬은 기본적으로 최소힙으로 구현하기 때문에 오름차순으로 정렬된다.
맥스힙으로 내림차순 정렬하기 위해선 heap에 -value를 넣고 result.append(-)하면 된다.
"""


from collections import counter # (3)
arr = Counter(['1', '2', '3', '3', '2', '1', '1'])
c = arr['1']

"""
# 3
카운터 해준다.
c의 value는 3
"""
