"""
가장 작은 떡과 그 다음으로 작은 떡의 차만큼 길이를 설정한다.

"""
n, m = map(int, input().split())
ddeoks = sorted(list(map(int, input().split())), reverse=True)
ddeokSum = 0
j = 0
for i in range(n-1, -1, -1):
    h = ddeoks[i] - ddeoks[i-1]
    for _ in range(j):
