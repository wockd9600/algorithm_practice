# 부모 노드를 찾아줌.
def find_parent(parent, x):
    # 부모 노드가 자기 자신이 아니면
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) # 할아버지 노드를 찾으러 간다.
    # 부모 노드(고부모)를 찾으면
    return parent[x]

# 연결 정보 확인
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 노드, 엣지
v, e = map(int, input().split())

# 부모 노드가 무엇인지 판별하는 변수, 초기화
parent = [0]
for i in range(1, v + 1):
    parent.append(i) # 자기자신을 부모 노드 지정

for _ in range(e):
    # 엣지를 받고, 연결 정보 확인
    a, b = map(int, input().split())
    union_parent(parent, a, b)


print(parent)
for i in range(v):
    print(find_parent(parent, i))
