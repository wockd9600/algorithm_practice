import sys
input = sys.stdin.readline

n = int(input())
numbers = [float(input().rstrip('\n')) for _ in range(n)]
now = 1
answer = -1
for i in range(n):
    now *= numbers[i]
    answer = max(answer, now)
    if now < 1: now = 1

print(f'{answer:.3f}')
