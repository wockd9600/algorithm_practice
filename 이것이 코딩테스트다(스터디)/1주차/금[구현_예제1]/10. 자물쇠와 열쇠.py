"""
키의 불필요한 부분을 없앤다. (4면 중 홈이 없는 면)
구해진 키로 자물쇠를 맞췄을 때 자물쇠의 범위와 같거나 넘어가면 true
못 맞추면 90도 돌려서 위의 행위 반복
같은 모양이 270도를 돌린 키로도 맞출 수 없으면 false
"""

def solution(key, lock):
    answer = True
    key = makeKey(key) # key의 불필요한 부분을 없앰.
    """
    키를 자물쇠에 넣고 맞는지 확인.
    키의 오른쪽 아래 가장자리 부분부터를
    자물쇠의 x축 0 y축 0 부터 넣어보고
    자물쇠가 다 1인지 검사
    키를 자물쇠의 x축으로 한 칸 옮긴 뒤 검사
    자물쇠의 한계에 닿으면 y축 한 칸 옮기고 x축 0으로 
    반복
    
    """    


# 90도 회전한 키
def rotate_90(a):
    n = len(a)
    m = len(a[0])
    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]

    return result



# 키의 불필요한 부분을 없앤다. (4면 중 홈이 없는 면)
def makeKey(key):
    keyLen = len(key)

    
    # 위, 아래, 왼, 오른
    keySize = [0, keyLen, 0, keyLen]
    
    key01 = [0, keyLen-1, 0, keyLen-1]
    key02 = [keyLen, -1, keyLen, -1]
    key03 = [0, 0]
    keyStep = [1, -1, 1, -1]

    for s in range(4):
        count = 0
        allBlank = True
        for i in range(key01[s], key02[s], keyStep[s]):
            for j in range(key03[s], keyLen):
                if s <= 1:
                    if key[i][j] == 1:
                        allBlank = False
                        break
                else:
                    if key[j][i] == 1:
                        allBlank = False
                        break
            if allBlank:
                count += 1
                allBlank = True
                continue
            break
        if s % 2 == 0:
            keySize[s] += count
            key03.append(keySize[0])
        else:
            keySize[s] -= count
    makedKey = []
    for i in range(keySize[0], keySize[1]):
        makedKey.append(list(key[i][keySize[2]:keySize[3]]))

    return makedKey
    

# key 입력
key = []
for _ in range(3):
    key.append(list(map(int, input().split())))

# lock 입력   
lock = []
for _ in range(3):
    lock.append(list(map(int, input().split())))

# 자물쇠 열기
print(solution(key, lock))
