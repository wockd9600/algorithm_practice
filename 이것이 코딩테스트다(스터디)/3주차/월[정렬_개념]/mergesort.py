import sys

#mergesort
def msort(a):
    if len(a) <=1:
        return a

    # 전달 받은 리스트를 반으로 나눈다.
    mid= len(a)//2
    left = a[:mid]
    right = a[mid:]

    # 반으로 나눈 리스트를 msort에 리커시브한다.
    left1 = msort(left)
    right1 = msort(right)

    # left1와 right1을 merge해서 return한다.
    return merge(left1, right1)

def merge(left, right):
    # i는 left의 가장 왼쪽, j는 right의 가장 왼쪽을 가르킨다.
    i, j = 0, 0
    sort = [] # 정렬된 후의 리스트
    # left와 right 둘 중 하나를 전부 소비할 때까지 반복한다.
    while i<len(left) and j<len(right):
        # left의 가장 왼쪽이 right의 가장 왼쪽보다 작으면 sort에 넣는다.
        if left[i]<=right[j]:
            sort.append(left[i])
            i+=1
        else:
            sort.append(right[j])
            j+=1


    # left와 right 둘 중 하나의 리스트를 전부 소비하고
    # 남은 리스트를 sort에 넣어준다.
    while i<len(left):
        sort.append(left[i])
        i+=1
    while j<len(right):
        sort.append(right[j])
        j+=1
    return sort

# 수의 개수 입력
N = int(sys.stdin.readline())
# 리스트 입력
a = [ int(sys.stdin.readline()) for _ in range(N) ]

# mergesort
a = msort(a)

# 출력
for i in range(N):
    print(a[i])
