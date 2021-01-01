"""
문제 : 배열의 길이 n, 연산수 m, 반복 가능 수 k
       배열에 주어진 숫자를 m번을 더해서 가장 큰 수를 만들어야 한다.
       숫자는 최대 k번 반복해서 더할 수 있고 다른 수를 더 하면 다시 더할 수 있다.
       ex) 배열 [4, 2, 1, 5] m=6, k=2 일 때 5+5+3+5+5+3 = 26

아이디어 : 배열을 정렬해서 첫 번째와 두 번째로 큰 숫자를 얻는다. (1)
           첫 번째 수를 k번 더하고 두 번째를 한 번 더하고를 반복한다. (2) 
"""

n, m, k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True) #(1)
sum = arr[0]

for i in range(1, m):
    #(2) if, else
    if i % k != 0:
        sum += arr[0]
    else:
        sum += arr[1]

print(sum)
