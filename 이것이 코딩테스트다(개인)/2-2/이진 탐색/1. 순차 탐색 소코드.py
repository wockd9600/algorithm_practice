# 순차 탐색 코드 구현
target = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    if target == arr[i]:
        print(i+1)
