"""
문자와 숫자를 따로 더 한다.
"""
# 입력
s = input()
#sumNumber
num = 0
# sumString
string = []

# 문자열 훑기
for ch in s:
    # 숫자면 num에 더하고
    if '0' <= ch and ch <= '9':
        num += int(ch)
    # 문자면 string에 추가한다.
    else:
        string.append(ch)
        
if num == 0: num = ""
print("".join(i for i in sorted(string)), end="")
print(num)
