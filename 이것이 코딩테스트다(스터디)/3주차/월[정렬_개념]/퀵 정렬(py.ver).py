import sys
sys.setrecursionlimit(99999)

# 퀵 정렬
def quickSort(arr):
    # 리스트의 길이가 1 이하면 그대로 리턴
    if len(arr) <= 1:
        return arr

    # 리스트의 중간값을 pivot값으로 설정한다.
    pivot = arr[len(arr) // 2]

    left_arr = []
    right_arr = []  
    middle_arr = []
    
    # pivot 값보다 작은 값, 큰 값, 같은 값을 분류한다.
    for num in arr:
        if num < pivot:
            left_arr.append(num)
        elif num > pivot:
            right_arr.append(num)
        else:
            middle_arr.append(num)

    # 작은 값 리스트를 정렬 후 같은 값과 더하고 큰 값 리스트를 정렬 후 더해준다.
    return quickSort(left_arr) + middle_arr + quickSort(right_arr)

arr = list(map(int, input().split()))

print(quickSort(arr))
