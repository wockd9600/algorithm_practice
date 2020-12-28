n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

print(" ". join(str(i) for i in sorted(arr, reverse = True)))
