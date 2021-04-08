import sys, heapq

# 외치는 정수의 개수
n = int(sys.stdin.readline())
# 작은 값을 저장할 힙과 큰 값을 저장할 힙으로 나눈다.
left_heap = []
right_heap = []
# n번 말하기
for i in range(n):
    # 수빈이가 외친 값 입력
    num = int(sys.stdin.readline())
    # 돌아가면서 left_heap과 right_heap에 넣어준다. (left_heap 먼저)
    if i % 2:
        # 큰 값이 저장된 right힙에서 필요한 값은 최솟값이므로 최소 힙
        heapq.heappush(right_heap, num)
    else:
        # 작은 값이 저장된 left힙에서 필요한 값은 최댓값이므로 최대 힙
        heapq.heappush(left_heap, -num)
    
    # 만약 left힙에 right힙보다 큰 값이 저장되었으면 바꿔준다.
    if right_heap and -left_heap[0] > right_heap[0]:
        heapq.heappush(right_heap, -heapq.heappop(left_heap))
        heapq.heappush(left_heap, -heapq.heappop(right_heap))

    # left힙에서 가장 큰 값 출력
    print(-left_heap[0])
