# 전자 매장의 부품 개수, 부품 번호
n = int(input())
materialN = sorted(list(map(int, input().split())))

# 손님의 요구 부품 개수, 부품 번호
m = int(input())
materialM = list(map(int, input().split()))

prepare = [False] * m # 부품이 내장에 있는지 여부

# 손님이 원하는 부품이 매장에 있는지 조사한다.
for i in range(m):
    start = 0
    end = n - 1
    target = materialM[i] # 찾을 부품
    while True:
        if start > end:
            break
        
        mid = (start + end) // 2

        if target == materialN[mid]:
            prepare[i] = True # 부품이 있다면 yes
            break

        if target < materialN[mid]:
            end = mid - 1

        else:
            start = mid + 1

print(" ".join("yes" if i else "no" for i in prepare))
