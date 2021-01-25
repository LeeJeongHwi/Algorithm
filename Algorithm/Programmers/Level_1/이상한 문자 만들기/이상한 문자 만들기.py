s = "trys CROSwv koreasdx hello world"

def solution(s):
    j = 0
    ans = []
    for i in range(len(s)):
        if s[i] == " ":
            j = 0
            ans.append(s[i])
            continue
        elif j%2==0:
            ans.append(s[i].upper())
            j+=1
        elif j%2!=0:
            ans.append(s[i].lower())
            j+=1
    return ''.join(ans)
        
def solution2(s):
    ans = []
    for string in s.split(" "):
        newStr = ""
        for i in range(len(string)):
            if i%2==0:
                newStr+=string[i].upper()
            else:
                newStr+=string[i].lower()
        ans.append(newStr)
    return " ".join(ans)
print(solution2(s))