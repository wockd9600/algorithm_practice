
# 숫자 목록 수(n), 더할 횟수(m), 반복 가능 횟수(k)를 받는다.
n, m, k = map(int, input().split())
# 숫자 목록
arr = sorted(list(map(int, input().split())), reverse=True)
sum=0

# k번 만큼 반복 할 수 있으니 k + 1 번째 마다 두 번째로 큰 숫자를 사용한다.
c2 = m // (k + 1)
# 두 번째로 큰 숫자를 제외한 나머지 숫자는 첫 번째로 큰 숫자다.
c1 = m - c2

# 계
sum = c1 * arr[0]
sum += c2 * arr[1]

print(sum)
