s = input()
num = 0
string = []
for ch in s:
    if '0' <= ch and ch <= '9':
        num += int(ch)
    else:
        string.append(ch)
if num == 0: num = ""
print("".join(i for i in sorted(string)), end="")
print(num)
