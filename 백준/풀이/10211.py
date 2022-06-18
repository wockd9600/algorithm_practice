import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().rstrip('\n').split()))
    now = -1
    answer = -1000001

    for i in range(n):
        if now < 0: now = numbers[i]
        else:  now += numbers[i]
        answer = max(answer, now)

    print(answer)
