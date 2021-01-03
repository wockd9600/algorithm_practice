n = int(input())
materialN = set(list(map(int, input().split())))

m = int(input())
materialM = sorted(list(map(int, input().split())))
prepare = [False] * m

for m in materialM:
    if m in materialN:
        print("yes", end=' ')
    else:
        print("no", end=' ')
