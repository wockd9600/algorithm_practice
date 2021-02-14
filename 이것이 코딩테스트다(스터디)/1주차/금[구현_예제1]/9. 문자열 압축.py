"""
문자열을 두 개 단위로 압축할 때부터
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
        i = 0 # 확인 중인 문자의 index
        count = 1 # 압축된 횟수
        string = "" # 압축된 문자열 결과
        
        p = pp # 압축할 길이
        while True:
            j = i + p # 확인해야 할 index
            
            # 압축할 수 있다면 횟수를 저장한다.
            if s[i:j] == s[j:j+p]:
                count += 1
                i += p
            # 압축할 수 없다면
            else:
                # 압축 중이 아니었다면 해당 문자열을 그대로 저장한다.
                if count == 1:
                    string += s[i:j]
                # 압축 중이었다면 해당 문자열과 압축 횟수를 저장한다.
                else:
                    string += str(count) + s[i:j]
                    count = 1
                i += p # 압축 확인하지 않은 다음 index로 넘긴다.

            if i >= len(s): # 압축 확인은 문자열의 길이까지만 한다.
                break
        List.append(string) # 압축된 문자열 저장
    answer = min(List) # 압축된 문자열 중 가장 짧은 문자열 return
    return answer

print(solution(input()))
