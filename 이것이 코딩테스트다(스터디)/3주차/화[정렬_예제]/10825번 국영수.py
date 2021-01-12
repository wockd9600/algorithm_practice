import sys
n = int(input())
student = []
for i in range(n):
    a = sys.stdin.readline().split()
    student.append((a[0],int(a[1]),int(a[2]),int(a[3])))

student.sort(key = lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for x in student:
    print(x[0])
