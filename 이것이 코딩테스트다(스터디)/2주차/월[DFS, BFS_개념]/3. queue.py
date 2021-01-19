from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(4)
queue.popleft()
print(queue)


# 데이터를 넣고 빼는 속도가 리스트에 비해 효율적
