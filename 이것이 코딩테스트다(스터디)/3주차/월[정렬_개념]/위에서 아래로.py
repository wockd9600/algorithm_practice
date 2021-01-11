
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

# 그냥 높은 수부터 출력하는 거 같은데..
print(" ". join(str(i) for i in sorted(arr, reverse = True)))
