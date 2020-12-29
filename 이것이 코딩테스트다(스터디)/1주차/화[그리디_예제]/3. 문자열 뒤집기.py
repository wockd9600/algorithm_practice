def fun(n):
    if n=='0':
        return False
    else:
        return True

binary = list(map(fun, input()))
c0 = 0 # 0으로 바꿀 때 횟수
c1 = 0 # 1로 바꿀 때 횟수
change = not(binary[0]) # 숫자가 바뀌는지 확인해주는 변수

for b in binary:
    # 숫자가 바뀔 때 카운트
    if change != b:
        if b:
            c0 += 1
        else:
            c1 += 1

        change = b

print(min(c0, c1))
