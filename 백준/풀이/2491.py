n = int(input())
numbers = list(map(int, input().rstrip().split()))

dp_d = [1] * n
dp_a = [1] * n

for i in range(1, n):
    if numbers[i] <= numbers[i-1]:
        dp_d[i] = dp_d[i-1] + 1
    
    if numbers[i] >= numbers[i-1]:
        dp_a[i] = dp_a[i-1] + 1

print(max(max(dp_d), max(dp_a)))