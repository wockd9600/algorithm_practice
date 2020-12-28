m , n = map(int, input().split())

#(1) min 함수로 행에서 가장 작은 값을 찾고 그 수들을 배열로 저장한다.
arr = [min(list(map(int, input().split()))) for _ in range(m)]

#(2)
print(max(arr))
