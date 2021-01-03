# 이진 탐색 재귀함수로 구현
target = int(input())
arr = sorted(list(map(int, input().split())))

def binary_search(arr, target, start, end):
    print(arr[start:end])
    if start > end:
        return

    mid = (start + end)//2

    if target == arr[mid]:
        return mid

    if target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

print(binary_search(arr, target, 0, len(arr)-1) + 1)
