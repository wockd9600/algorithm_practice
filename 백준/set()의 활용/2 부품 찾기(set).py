n = int(input())
materialN = set(list(map(int, input().split())))

m = int(input())
materialM = sorted(list(map(int, input().split())))
prepare = [False] * m

for m in materialM:
    if m in materialN:
        print("yes", end=' ')
    else:
        print("no", end=' ')

"""
Set
파이썬에서 탐색할 땐 set함수를 활용할 수 있다.
set은 정렬이란 개념이 없기 때문에 index를 사용하지 않는다. 또한 수학의 집합 개념이라고 생각할 수 있고 중복이 없다.
해시 테이블로알려진 데이터 구조를 기반으로 한다.
참고 : https://www.geeksforgeeks.org/sets-in-python/
"""
