n = int(input())
materialN = sorted(list(map(int, input().split())))

m = int(input())
materialM = list(map(int, input().split()))
prepare = [False] * m

for i in range(m):
    start = 0
    end = n - 1
    target = materialM[i]
    while True:
        if start > end:
            break
        
        mid = (start + end) // 2

        if target == materialN[mid]:
            prepare[i] = True
            break

        if target < materialN[mid]:
            end = mid - 1

        else:
            start = mid + 1

print(" ".join("yes" if i else "no" for i in prepare))
