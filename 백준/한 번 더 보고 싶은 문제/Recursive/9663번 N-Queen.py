"""
백트래킹은 연산수가 많은 알고리즘에 속해서 연산 속도가 느린 파이썬에게 쥐약 같은 존재다.
N Queen 역시 가장 기초적으로 풀면 시간 초과가 발생한다.
그래서 여러가지 편법을 사용해야 한다.

1. Check(행, 열, 대각선에 겹치는지)를 할 때 모든 수를 대입해서 확인하는 것이 아니라 배열을 만들어서 해당 위치에 놓아도 되는지 확인해야 한다.
    하나씩 확인하는 순간 시간 초과가 발생한다.
2. N Queen은 x축 대칭이다.
    따라서 맨 윗줄의 반만 구한 수 x2를 해주면 된다.

https://blog.naver.com/wockd9600/222106414332
"""

# 퀸을 개수(=체스판 배열의 크기)를 입력 받는다.
N = int(input())
# 좌우, 대각선, 대각선에 퀸이 없는지 확인하는 값
a, b, c = [False]*N, [False]*(2*N-1), [False]*(2*N-1)
count=0

def nqueen(n):
    global count
    if n == N: # 퀸을 모두 모았을 시 카운트
        count+=1
        return

    # 첫 째줄은 반만 확인 하면 된다. (=나머지는 다 확인한다.)
    if n!=0:
        for i in range(N):
            # 해당 칸에 퀸이 없다면
            if not (a[i] or b[n+i] or c[n-i+N-1]):
                a[i] = b[n+i] = c[n-i+N-1] = True # 퀸을 넣고
                nqueen(n+1) # 다음 줄로 이동한다.
                a[i] = b[n+i] = c[n-i+N-1] = False
    else:
        for i in range(N//2):
            if not (a[i] or b[n+i] or c[n-i+N-1]):
                a[i] = b[n+i] = c[n-i+N-1] = True
                nqueen(n+1)
                a[i] = b[n+i] = c[n-i+N-1] = False
                
        count*=2 # 모두 구했으면 x2

        # N이 홀수라면 카운데에 퀸이 있을 때도 확인해줘야 한다.
        if N%2==1:
            a[(N//2)] = b[(N//2)] = c[-(N//2)+N-1] = True
            nqueen(n+1)
            a[(N//2)] = b[(N//2)] = c[-(N//2)+N-1] = False

nqueen(0)
print(count)
