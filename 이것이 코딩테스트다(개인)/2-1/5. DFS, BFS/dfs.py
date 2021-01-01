# 그래프 모양, 방문 노드, 방문 여부
def dfs(graph, v, visited):
    # v 노드 방문 처리
    visited[v] = True
    print(v, end=' ')

    # v 노드와 맞닿아 있는 모든 노드를 확인
    for i in graph[v]:
        # 만약 방문하지 않았다면 방문
        if not visited[i]:
            dfs(graph, i, visited)

# 그래프 모양을 그린다.
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9

dfs(graph, 1, visited)
