# 학생 수 입력
n = int(input())

# 학생 이름과 점수 입력
arr = []
for _ in range(n):
    name, score = input().split()
    arr.append((name, int(score)))

# 성적이 낮은 순서대로 출력
print(" ".join(i[0] for i in sorted(arr, key=lambda student: student[1])))
