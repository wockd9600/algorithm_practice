n = input()
mid = len(n)//2
sumleft = 0
sumright = 0

for i in n[:mid]:
    sumleft += int(i)
for i in n[mid:]:
    sumright += int(i)
    
if sumleft == sumright:
    print("LUCKY")
else:
    print("READY")
