from itertools import combinations

while True:
    arr =  list(map(int, input().split()))
    if arr[0] == 0:
        break
    del arr[0]
    # combinations(arr, x)는 len(arr)Cx의 조합을 뱉어내는 라이브러리
    for combi in combinations(arr, 6):
        for i in combi:
            print(i, end=' ')
        print("")
    print("")