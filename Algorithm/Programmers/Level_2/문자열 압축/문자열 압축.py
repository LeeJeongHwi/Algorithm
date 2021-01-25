test_set = ['aabbaccc','ababcdcdababcdcd','abcabcdede','abcabcabcabcdededededede','xababcdcdababcdcd']
def solution(s):
    slen = len(s)
    min_len = float('inf')
    for cut in range(1,slen+1):
        target = s[:cut]
        count = 0
        result = []
        for i in range(cut,slen+1,cut):
            if target == s[i-cut:i]:
                count+=1
                continue
            elif target != s[i-cut:i]:
                if count == 1:
                    result += target
                else:
                    result += str(count)+target
                target = s[i-cut:i]
                count = 0
                count+=1
        if count == 1:
            result += target
        else:
            result += str(count)+target
        if slen != i-1:
            result+=s[i:]
        min_len = min(min_len,len(result))
        # print(result)
    return min_len

            
for s in test_set:
    print(solution(s))