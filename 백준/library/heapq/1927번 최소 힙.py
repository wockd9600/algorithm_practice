import sys, heapq
# 연산의 개수
n = int(sys.stdin.readline())
# 힙으로 사용할 list
heap = []

for _ in range(n):
    # 연산 종류
    cmd = int(sys.stdin.readline())
    # 연산이 0이 아닌 게 아니라면 (ㅋㅋ)
    if not cmd:
        # 힙이 비어있지 않으면 최솟값 출력
        if heap:
            print(heapq.heappop(heap))
        # 비어있으면 0출력
        else:
            print(0)
    # 연산이 자연수라면 해당 수 삽입
    else:
        heapq.heappush(heap, cmd)