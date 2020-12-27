from collections import deque

# deque를 이용한 bfs
def bfs(graph, start, visited):
    # 첫 노드를 deque에 넣는다.
    queue = deque([start])
    # 첫 노드 방문 처리
    visited[start] = True

    # deque에 데이터가 없을 때까지 반복
    while queue:
        # 현재 deque 중 가장 먼저 들어온 노드 꺼내기
        v = queue.popleft()
        print(v, end=' ')

        # 해당 노드와 접촉한 모든 노드 검사
        for i in graph[v]:
            # 만약 접촉한 노드를 방문하지 않았다면
            if not visited[i]:
                # deque에 넣고 방문 처리
                queue.append(i)
                visited[i] = True

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

bfs(graph, 1, visited)
