"""
Y, F, O (2, 3, 4)
input : 신청 N, 종류
answer : 최대 몇 번 게임
한 번 한 사람과 다시 같이 게임x
"""

n, t = map(str, input().split())

n = int(n)

user = set()
for _ in range(n):
    user.add(input())

user_num = len(user)

if t == 'Y': print(user_num)
elif t == 'F': print(user_num // 2)
else: print(user_num // 3)


"""
1
n,g,*l=open(0).read().split()
print(len({*l})//((3,2)[g<'O'],1)[g>'O'])

*l : 리스트로 받아옴
open(0).read() : 파일의 입력값을 다 긁어옴
((3,2)[g<'O'],1)[g>'O']) : 튜플에 인덱스를 조건식으로 사용한 삼항연산자


2
s,*a=open(0);print(len({*a})//'`YFO'.find(s[-2]))
"""