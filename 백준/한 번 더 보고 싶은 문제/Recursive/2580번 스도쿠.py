"""
스도쿠 만들긴데 한창 백트래킹 공부하고 있을 때라 크게 어려웠던 문제는 아니었다.
지금 다시 만들려면 좀 오래 걸릴 거 같긴하다..
"""

# 스도쿠 모양을 입력 받는다.
board=[list(map(int,input().split())) for _ in range(9)]

def check(x, y, n):
    for i in range(9):
        if board[x][i]==n or board[i][y]==n:
            return False
        if board[(x//3)*3+i//3][(y//3)*3+i%3] == n:
            return False
    return True


def sudoku(x, y):
    # 스도쿠를 모두 채우거나 범위를 벗어나면 함수를 종료한다.
    if x==9:
        for row in board:
            print(" ".join(map(str, row)))
            exit()

    # 확인 중인 칸(x, y)이 채워져 있으면 다음 칸으로 이동한다.
    if board[x][y]!=0:
        sudoku(x, y+1) if y!=8 else  sudoku(x+1, 0)

    else:
        for i in range(1, 10):
            if check(x, y, i): # 확인 중인 칸에 i를 놔둬 된다면
                # i를 놓고 다음 칸으로 넘어간다.
                board[x][y] = i
                sudoku(x, y+1) if y!=8 else  sudoku(x+1, 0)

            
            if i == 9:
                board[x][y]=0

sudoku(0, 0)
