n, m, k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
sum = arr[0]

for i in range(1, m):
    if i % k != 0:
        sum += arr[0]
    else:
        sum += arr[1]

print(sum)
