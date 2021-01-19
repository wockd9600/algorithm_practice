"""
0을 뒤집는 경우와 1을 뒤집는 경우를 구해서
뭐가 더 뒤집는 횟수가 적은지 비교한다.

* 해당 문제는 for문 한 번 돌릴 때 두 가지 일을 동시에 하면서 반복문의 사용을 줄이고 있다. (그리디)
"""

# 0이랑 1만 입력 받으니 메모리 절약을 위해 boolean 타입으로 변환한다.
# 0 = False, 1 = True
def fun(n):
    if n=='0':
        return False
    else:
        return True

binary = list(map(fun, input()))
c0 = 0 # 모든 수를 0으로 만들 때 뒤집는 횟수
c1 = 0 # 모든 수를 1로 만들 때 뒤집는 횟수

# 숫자가 바뀌는지 확인해주는 변수
# 처음 수의 반대로 초기화 (1)
change = not(binary[0])

for b in binary:
    # 만약 숫자가 바뀌면 카운트
    # 처음엔 (1)에 의해 b와 change가 다르다.
    if change != b:
        # b가 1이면 0으로 만들어야하니 c0를 카운트한다.
        if b:
            c0 += 1
        # 0이면 1로 만들어야하니 c1을 카운트한다.
        else:
            c1 += 1

        change = b

print(min(c0, c1))
