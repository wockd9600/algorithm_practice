n, m = map(int, input().split())
ball = sorted(list(map(int, input().split())))

def ChoiceBall(balls):
    currentBall = balls[0] # 현재 
    count = 0
    m = 0
    for i in range(len(balls)-1):
        t = i + 1
        if currentBall == balls[t]:
            m += 1
            continue

        count += len(balls[t::])
        count += m * len(balls[t::])
        currentBall = balls[t]
        m = 0

    return count

print(ChoiceBall(ball))
