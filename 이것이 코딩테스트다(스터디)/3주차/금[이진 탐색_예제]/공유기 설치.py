"""
집의 거리를 이분 탐색
"""

# 집의 개수, 공유기 개수
n, c = list(map(int, input().split(' ')))

# 집의 좌표
h = []
for _ in range(n):
     h.append(int(input()))

h.sort()

start = h[1] - h[0] # 집의 좌표 중에 가장 작은 값
end = h[-1] - h[0] # 집의 좌표 중에 가장 큰 값

answer = 0
while(start <= end):
    mid = (start + end) // 2
    # 첫째 집은 무조건 공유기 설치
    value = h[0]
    count = 1
    # 현재의 mid 값(거리 값)을 이용해 공유기를 설치
    for i in range(1, n):
        if h[i] >= value + mid:
            value = h[i]
            count += 1
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid # 최적의 결과 저장
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리 감소
        end = mid - 1

print(result)
