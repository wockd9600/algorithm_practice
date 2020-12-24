m , n = map(int, input().split())

arr = [min(list(map(int, input().split()))) for _ in range(m)]

print(max(arr))
