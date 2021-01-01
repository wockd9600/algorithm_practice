"""
가장 큰 수를 구하기 위해선
1이나 0일 때는 더하고 나머지는 곱하면 된다.
"""
# 숫자 입력
nums = list(map(int, input()))
sum = 0

for num in nums:
    # 숫자가 1 또는 0일 땐 더 한다. sum이 0일 때도 더 해야 한다.
    if num == 0 or num == 1 or sum == 0:
        sum += num
    # 그 외는 곱하면 된다.
    else:
        sum *= num
print(sum)
