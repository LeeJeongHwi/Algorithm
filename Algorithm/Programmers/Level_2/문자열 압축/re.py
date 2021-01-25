
s=["aabbaccc","ababcdcdababcdcd","abcabcdede","abcabcabcabcdededededede","xababcdcdababcdcd"]

def solution(s):
    #1~n개씩 자르는 경우 중 가장 짧게 만드는 것
    strlen = len(s)
    ans = float("inf")
    for cut in range(1,strlen+1): # cut : 자르는 문자열의 수 갯수 count of cut string
        target = s[0:cut]
        temp = ""
        count = 0 #중복 문자열 체크
        for i in range(0,strlen,cut):
            if target == s[i:i+cut]:
                count+=1
                continue
            elif target != s[i:i+cut]:
                if count != 1:
                    temp += str(count)+target
                if count == 1:
                    temp += target
                target = s[i:i+cut]
                count = 1
        if count == 1:
            temp += target
        else:
            temp += str(count)+target
        ans = min(ans,len(temp))
    return ans


for st in s:
    print(solution(st))
