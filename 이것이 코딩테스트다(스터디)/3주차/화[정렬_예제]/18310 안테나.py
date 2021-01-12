import sys

def msort(a):
    if len(a) <= 1:
        return a

    mid = len(a)//2
    l = a[:mid]
    r = a[mid:]

    ll = msort(l)
    rl = msort(r)

    return merge(ll, rl)

def merge(l, r):
    i, j = 0, 0
    sort = []

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            sort.append(l[i])
            i += 1
        else:
            sort.append(r[j])
            j += 1

    while i < len(l):
        sort.append(l[i])
        i += 1
    while j < len(r):
        sort.append(r[j])
        j += 1

    return sort

n = int(input())
house = msort(list(map(int, sys.stdin.readline().split())))

print(house[n//2] if n % 2 == 1 else house[n//2 - 1])
