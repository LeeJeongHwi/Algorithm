# [1,2,3,4,5]
# [2,1,2,3,2,4,2,5]
# [3,3,1,1,2,2,4,4,5,5]
def solution(answers):
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(1999):
        a1+=[1,2,3,4,5]
    for i in range(1249):
        a2+=[2,1,2,3,2,4,2,5]
    for i in range(999):
        a3+=[3,3,1,1,2,2,4,4,5,5]
    col=[0,0,0]
    for i in range(len(answers)):
        if a1[i] == answers[i]:
            col[0]+=1
        if a2[i] == answers[i]:
            col[1]+=1
        if a3[i] == answers[i]:
            col[2]+=1
    answer = [i+1 for i,x in enumerate(col) if max(col) == x]
    return answer