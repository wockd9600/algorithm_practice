import sys, heapq
# 보석 수, 가방 수
n, k = map(int, sys.stdin.readline().split())
# 보석과 가방을 담을 힙(최소)
arr = []
# 보석의 무게와 가치 입력
for _ in range(n):
    a, b = map (int, sys.stdin.readline().split())
    heapq.heappush(arr, (a, b))
# 가방 가치는 보석보다 크게 설정한다.
bag = 1000001
# 가방의 용량 입력
for _ in range(k):
    heapq.heappush(arr,((int(sys.stdin.readline()), bag)))

# 보석을 담을 힙(최대)
jew = []
ans = 0
while arr:
    # 최소힙의 첫번째 데이터가 가방이면
    if arr[0][1] == bag:
        # 가방 데이터는 버린다.
        heapq.heappop(arr)
        # 최대힙에 담긴 데이터가 없다면(가방에 담을 수 있는 보석이 없다면)
        if not jew:
            continue
        # 해당 가방에 담을 수 있는 값이 담겨 있고 최대힙이므로
        # 보석의 가치가 제일 큰 데이터가 가장 앞에 있다.
        ans += -heapq.heappop(jew)[0]
    # 가방이 아니면
    else:
        # 최대힙에 보석을 넣는다.
        a, b = heapq.heappop(arr)
        heapq.heappush(jew, (-b, a))
print(ans)
