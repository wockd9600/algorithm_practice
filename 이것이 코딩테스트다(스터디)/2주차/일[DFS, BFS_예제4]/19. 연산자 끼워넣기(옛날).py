"""
전체적으로 방법이 크게 달라지진 않았다.
최근에 배운 if문이 여러개 일 때
for문으로 줄이는 방법을 적용한게 유일한 차이점인듯.
"""
N = int(input())
a = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
b=[-1000000000, 1000000000]
r = 0
def insert(n, result):
    global plus, minus, multi, div, r
    if n == N-1:
        if b[0]<result: b[0]=result
        if b[1]>result: b[1]=result
        r = 0
        return
    for i in range(4):
        if i ==0 and plus!=0:
            r = result+a[n+1]
            plus-=1
            insert(n+1, r)
            plus+=1
        elif i == 1 and minus!=0:
            r = result-a[n+1]
            minus-=1
            insert(n+1, r)
            minus+=1
        elif i==2 and multi!=0:
            r = result*a[n+1]
            multi-=1
            insert(n+1, r)
            multi+=1
        elif i==3 and div !=0:
            r = int(result/a[n+1])
            div-=1
            insert(n+1, r)
            div+=1
insert(0, a[0])
print(b[0])
print(b[1])
