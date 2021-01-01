"""
걍 for문
"""

n = int(input())
sum = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            t = str(i) + str(j) + str(k)
            if '3' in t:
                sum += 1

print(sum)
