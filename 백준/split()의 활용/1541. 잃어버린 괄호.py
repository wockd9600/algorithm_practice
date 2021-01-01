s = input().split('-')
cnt = 0
for ch in s[0].split('+'):
    cnt += int(ch)
for ch in s[1:]:
    for c in ch.split('+'):
        cnt -= int(c)
print(cnt)
