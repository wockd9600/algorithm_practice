n, k = map(int, input().split())
die = [i for i in range(1, n + 1)]
died = []
i = -1
while die:
    l = len(die)
    i += k
    while i >= l:
        i -= l
    # arr.pop(i)는 arr[i]를 제거한다.
    died.append(die.pop(i))
    i -= 1

print('<', ', '.join([str(i) for i in died]), '>', sep="")