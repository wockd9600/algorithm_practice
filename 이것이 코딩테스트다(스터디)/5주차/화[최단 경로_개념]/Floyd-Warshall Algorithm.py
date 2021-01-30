INF = int(1e9)

# 노드와 간선을 입력 받는다.
n = int(input())
m = int(input())

# adjacency matrix
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자신의 거리는 0으로 초기화한다.
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# a노드에서 b노드로 가는데 걸리는 비용은 c이다.
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 거쳐가는 노드 k
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # a노드에서 b노드로 갈 때 바로 가는 것과 k노드를 거쳐 가는 것 중
            # 최소값을 입력한다.
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(graph[a][b], end=" ")
    print("")
