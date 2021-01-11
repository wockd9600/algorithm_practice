
# 배열의 크기, 교체 횟수
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 내림차순, b는 오름차순으로 정렬
a.sort()
b.sort(reverse=True)

# 교체 횟수 k번 반복
for i in range(k):
    # b가 더 크면 a와 교체
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
# k번 교체해서 출력할 수 있는 가장 큰 sum값
print(sum(a))
