def selectionSort(arr):
    # index 0부터 차례대로 수를 선택한다.
    for i in range(len(arr)):
        m = i
        # 선택된 i 다음 수부터 차례대로 검사한다.
        for j in range(i+1, len(arr)):
            # 가장 작은 수를 찾는다.
            if arr[j] < arr[m]:
                m = j
        # 선택된 i와 가장 작은 수를 스왚한다. (가장 작은 수가 왼쪽으로 온다.)
        arr[i], arr[j] = arr[j], arr[i]

arr = list(map(int, input().split()))

selectionSort(arr)

print(arr)
