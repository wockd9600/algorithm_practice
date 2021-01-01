"""
걍 for문
"""

n = int(input())
sum = 0

# 시간, 분,  초를 문자열로 초기화
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            t = str(i) + str(j) + str(k)
            # 문자열에 3이 있으면 카운트
            if '3' in t:
                sum += 1

print(sum)
