import sys
sys.setrecursionlimit(99999)

# 퀵 정렬
def quickSort(arr):
    # 리스트의 길이가 1 이하면 그대로 리
    if len(arr) <= 1:
        return arr

    # 리스트의 중간값을 pivot값으로 설정한다.
    pivot = arr[len(arr) // 2]

    # pivot 값보다 작은 것과 큰 것을 분류한다.
    left_arr = [i for i in arr if i <= pivot]
    right_arr = [i for i in arr if i > pivot]

    return quickSort(left_arr) + [pivot] + quickSort(right_arr)

arr = list(map(int, input().split()))

print(quickSort(arr))
