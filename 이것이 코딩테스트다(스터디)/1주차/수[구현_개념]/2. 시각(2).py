"""
걍 for문
"""

n = int(input())
sum = 0
sum01 = 0

# 3이 들어가지 않는 시간의 3을 포함하는 시간을 카운트
for j in range(60):
    for k in range(60):
        t = str(j) + str(k)
        # 문자열에 3이 있으면 카운트
        if '3' in t:
            sum01 += 1

# 시간 카운트
for i in range(0, n+1):
    # 3이 들어가지 않으면
    if not '3' in str(i):
        sum += sum01

    #3이 들어가
    else:
        sum += 3600

print(sum)
