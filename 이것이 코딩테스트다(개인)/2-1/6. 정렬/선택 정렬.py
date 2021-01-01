def selectionSort(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[j] = arr[j], arr[i]

arr = list(map(int, input().split()))

selectionSort(arr)

print(arr)
