def solution(s):
    List = []
    if len(s) == 1:
        return 1
   
    for pp in range(1, len(s)//2 + 1):
        i = 0
        p = pp
        count = 1
        string = ""
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
    print(List)
    return answer

print(solution(input()))
