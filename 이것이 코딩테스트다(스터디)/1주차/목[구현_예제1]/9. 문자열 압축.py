"""
문자열을 한 개 단위로 압축할 때부터
문자열의 길이 나누기 2만큼 단위로 압축할 때까지 모두 구한 후
뭐가 제일 짧은지 비교한다.
"""

# 문자열 압축
def solution(s):
    List = []
    # 문자열의 길이가 1이면 압축x
    if len(s) == 1:
        return 1

    # 길이 나누기 2만큼 단위로 압축할 때까지 모두 구한다.
    for pp in range(1, len(s)//2 + 1):
        # 확인 중인 문자의 index
        i = 0
        count = 1
        string = ""
        
        p = pp
        while True:
            j = i + p
            if s[i:j] == s[j:j+p]:
                count += 1
                i += p
            else:
                if count == 1:
                    string += s[i:j]
                else:
                    string += str(count) + s[i:j]
                    count = 1
                i += p

            if i >= len(s):
                break
        List.append(string)
    answer = min(List)
    return answer

print(solution(input()))
