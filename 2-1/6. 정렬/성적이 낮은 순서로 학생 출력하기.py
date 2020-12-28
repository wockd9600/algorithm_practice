n = int(input())
arr = []

for _ in range(n):
    name, score = input().split()
    arr.append((name, int(score)))

print(" ".join(i[0] for i in sorted(arr, key=lambda student: student[1])))
