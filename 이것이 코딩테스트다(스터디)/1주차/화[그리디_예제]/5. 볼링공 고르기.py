"""
정렬해 같은 공의 무게끼리 모은다.

선택된 공보다 무거운 공을 모두 더한다. (1)
선택된 공과 (같은 공의 무게 개수 -1)을 무거운 공 모두와 곱한다. (2)
첫 번째부터 마지막 공까지 해당 위의 행위를 반복한다.
"""

# 입력
n, m = map(int, input().split())
ball = sorted(list(map(int, input().split())))


# 서로 무게가 다른 볼링공을 선택하는 경우의 수 구하기
def ChoiceBall(balls):
    count = 0
    # 현재 공의 무게
    currentBall = balls[0] 
    # 현재 공의 무게와 같은 공의 개수 (현재 공은 포함x)
    m = 0
    
    # 시작
    for i in range(len(balls)-1):
        # 다음 공의 index
        t = i + 1
        # 만약 현재 공과 다음 공의 무게가 같다면 
        if currentBall == balls[t]:
            m += 1
            continue

        # 다르다면 (1)과 (2)를 한다.
        count += len(balls[t:])
        count += m * len(balls[t:])
        currentBall = balls[t]
        m = 0

    return count

print(ChoiceBall(ball))
