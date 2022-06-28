from collections import deque
import sys
input = sys.stdin.readline
INF = int(10e9)

n = int(input())
pre = [-1] * (n + 1)

queue = deque([(n, 0)])

while queue:
    now, c = queue.popleft()

    if now == 1: break
    
    if now % 3 == 0 and pre[now//3] == -1:
        pre[now//3] = now
        queue.append((now//3, c + 1))

    if now % 2 == 0 and pre[now//2] == -1:
        pre[now//2] = now
        queue.append((now//2, c + 1))

    if pre[now-1] == -1:
        pre[now-1] = now
        queue.append((now-1, c + 1))

result = [1]
i = 1
while pre[i] != -1:
    result.append(pre[i])
    i = pre[i]
    
print(c)
print(' '.join(map(str, result[::-1])))
