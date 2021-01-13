"""
n이 1,000,000이고 시간 제한이 2초니까 O(n^2)으로는 풀기 힘들 것 같다.

절단기의 길이를 이분 탐색으로 찾는다. logN
떡을 전부 잘라본다 N
손님이 요구한 떡의 길이 m보다 총 떡의 길이가 길면 절단기를 짧게 하고
짧으면 길게 해서 적절한 값을 찾는다.

"""
# 떡의 개수와 손님이 원하는 떡의 길이
n, m = map(int, input().split())
# 가게에 있는 떡 리스트
ddeoks = sorted(list(map(int, input().split())), reverse=True)

# 떡의 범
long = ddeoks[0]
shot = 0

answer = 0
while long >= shot:
    sum = 0
    # 절단기 길이를 정한다.
    cutter = (long + shot) // 2

    # 절단기로 자른다.
    for ddeok in ddeoks:
        if ddeok > cutter:
            sum += ddeok - cutter
        else:
            break
        
    # 떡의 양이 맞으면 반복문 종료
    if sum == m:
        break

    # 요구한 떡보다 잘린 떡이 많다면
    if sum > m:
        shot = cutter + 1
        answer = cutter
    # 요구한 떡이 적다면
    else: long = cutter - 1

print(cutter)


#피드백
"""
이 문제는 내가 이분 탐색을 어디에 적용해야 할까라고 생각해서 풀 수 있었던 문제지
그냥 풀었으면 못 풀었을 거 같다.
적용 능력을 더 향상시켜야..
"""
