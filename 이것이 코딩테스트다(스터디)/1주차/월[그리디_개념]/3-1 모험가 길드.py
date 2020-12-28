N = int(input())
heros = list(map(int, input().split()))
heros.sort()

def group(heros):
    # 그룹 수 카운트
    c = 0

    # 공포도가 1인 모험가는 따로 처리한다.
    for i in heros:
        if i == 1:
            c +=1
        else:
            break

    # 공포도가 1이 아닌 모험가부터 시작
    i = 0
    if c != 0:
        i = c - 1
    # 해당 그룹의 공포도
    last = heros[i]
    while i < len(heros):
        # 임의의 그룹의 마지막 모험가의 index
        t = last + i - 1

        # 그룹의 마지막 모험가의 index가 총 모험가 수를 넘을 수 없다.
        if t >= len(heros):
            break

        # 그룹의 마지막 모험가의 공포도와 해당 그룹의 공포도와 같으면 그룹 확정
        if heros[t] == last:
            i = t + 1
            c += 1
            last = heros[i]
        # 아니면 부족한 인원을 추가로 모집한다.
        else:
            last = heros[t]

        print(c)
            
    return c

print(group(heros))
