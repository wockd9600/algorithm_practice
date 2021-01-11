def insectionSort(arr):
    # index 1부터 차례대로 수를 선택. 단, 선택된 수의 왼쪽은 전부 정렬 되어있다.
    for i in range(1, len(arr)):
        # i 전의 수 중 선택된 수보다 작은 수를 만날 때까지 옮겨준다.
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

arr = list(map(int, input().split()))

insectionSort(arr)
print(arr)
