import heapq
import sys
input = sys.stdin.readline
INF = int(2e14)

def dijkstraf(s):
    q = []
    heapq.heappush(q, (0, s))
    
    dpf[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > dpf[now]: continue

        for next_node, l in mountain[now]:
            cost = dist + l

            if cost < dpf[next_node]:
                dpf[next_node] = cost
                heapq.heappush(q, (cost, next_node))

def dijkstraw(s):
    q = []
    heapq.heappush(q, (0, s, 0))
    
    state = [1, 0]
    cal = [0.5, 2]
    dpw[s][1] = 0

    while q:
        dist, now, cnt = heapq.heappop(q)

        if dist > dpw[now][state[cnt]]: continue

        for next_node, l in mountain[now]:
            cost = dist + l * cal[cnt]

            if cost < dpw[next_node][cnt]:
                dpw[next_node][cnt] = cost
                heapq.heappush(q, (cost, next_node, state[cnt]))

n, m = map(int, input().rstrip().split())

mountain = [[] for _ in range(n + 1)]

dpf = [INF] * (n + 1)
dpw = [[INF] * 2 for _ in range(n + 1)]

for _ in range(m):
    a, b, c, = map(int, input().rstrip().split())
    mountain[a].append((b, c))
    mountain[b].append((a, c))

dijkstraf(1)
dijkstraw(1)

answer = 0
for i in range(1, n + 1):
    if dpf[i] < min(dpw[i]): answer += 1

print(answer)