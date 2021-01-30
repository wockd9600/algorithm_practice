def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

v, e = map(int, input().split())

parent = [0]
for i in range(1, v + 1):
    parent.append(i)

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)


print(parent)
for i in range(v):
    print(find_parent(parent, i))
