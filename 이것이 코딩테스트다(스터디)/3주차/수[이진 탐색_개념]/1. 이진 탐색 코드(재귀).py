"""
Binary Search(이진 탐색) 알고리즘은 Sequential Search와 같이 순서대로 탐색하는 방법이 아닌 반씩 나눠서 탐색하는 방식이다. 

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]에서 5를 찾을 때
6을 확인한다. 6은 5가 아니고 5보다 크기 때문에 6 이후 값은 확인할 필요가 없다. 
3을 확인한다. 3은 5가 아니고 5보다 작기 때문에 3 이전 값은 확인할 필요가 없다.
5를 확인한다. 5는 5가 아니고 5보다 작기 때문에 4 이전 값은 확인할 필요가 없다
5를 확인한다. 5는 5가 맞으므로 탐색이 종료된다.

"""
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
