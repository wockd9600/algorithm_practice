def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

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

edges = []
result = 0

# cost
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 비용순으로 모든 엣지를 정렬함.
edges.sort()

# 작은 비용순으로 확인한다.
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
