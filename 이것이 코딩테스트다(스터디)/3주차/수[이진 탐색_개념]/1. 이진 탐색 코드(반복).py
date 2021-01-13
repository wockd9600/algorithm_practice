# 이진 탐색 반복문으로 구현
target = int(input())
arr = sorted(list(map(int, input().split())))

start = 0
end = len(arr) - 1

while True:
    print(arr[start:end])
    if start > end:
        print("none")
        break
    mid = (start + end)//2

    if target == arr[mid]:
        print(mid + 1)
        break

    if target < arr[mid]:
        end = mid - 1
    else:
        start = mid + 1
