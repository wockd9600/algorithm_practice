nums = list(map(int, input()))
sum = 0
for num in nums:
    if num == 0 or num == 1 or sum == 0 or sum == 1:
        sum += num
    else:
        sum *= num
print(sum)
