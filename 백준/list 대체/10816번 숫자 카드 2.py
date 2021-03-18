n = int(input())
cardList = list(map(int, input().split()))
m = int(input())
targetList = list(map(int, input().split()))

dic = {}
for target in cardList:
    if target in dic:
        dic[target] += 1
    else:
        dic[target] = 1

print(' '.join(str(dic[target]) if target in dic else '0' for target in targetList))
