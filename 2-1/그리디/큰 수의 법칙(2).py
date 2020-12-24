n, m, k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
sum=0

c2 = m // (k + 1)
c1 = m - c2

sum = c1 * arr[0]
sum += c2 * arr[1]

print(sum)
