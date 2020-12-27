import sys
sys.setrecursionlimit(99999)

# 퀵 정렬
def quickSort(arr, start, end):
    if start >= end:
        return
    # pivot 값을 첫 번째 데이터, i는 두 번째, j는 마지막 데이터로 지정
    # ex) [3, 1, 5, 2, 4] (1)
    #      p  i        j
    pivot = start
    i = start + 1
    j = end

    # i와 j가 엇갈릴 때까지 반복한다.
    while i < j:

        # 왼쪽에서 pivot 값보다 큰 값을 찾는다.
        while i < end and arr[i] <= arr[pivot]:
            i += 1
            """ ex) [3, 1, 5, 2, 4] (2)
                     p     i     j
                    [3, 1, 2, 5, 4] (5)
                     p        j  i               """

        # 오른쪽에서 pivot 값보다 작은 값을 찾는다.
        while j > start and arr[j] > arr[pivot]:
            j -= 1
            """ ex) [3, 1, 5, 2, 4] (3)
                     p     i  j
                    [3, 1, 2, 5, 4] (6)
                     p     j     i               """

        # 만약 i와 j가 엇갈렸다면 j와 pivot 값을 바꿔준다.
        if i >= j:
            arr[j], arr[pivot] = arr[pivot], arr[j]
            """ ex) [2, 1, 3, 5, 4] (7)
                     p     j     i               """

        # 아니면 i와 j 값을 바꾼다.
        else:
            arr[i], arr[j] = arr[j], arr[i]
            """ ex) [3, 1, 2, 5, 4] (4)
                     p     i  j                """

    # 위의 반복문을 마치면 왼쪽은 pivot 값과 같거나 작고 오른쪽은 크게된다.
    """ ex) [2, 1, 3, 5, 4]
                   p                 """
    # 그럼 pivot 값은 정렬된 것이니 나머지 값을 정렬해준다.
    quickSort(arr, start, j-1)
    quickSort(arr, j+1, end)

arr = list(map(int, input().split()))

quickSort(arr, 0, len(arr)-1)
print(arr)
