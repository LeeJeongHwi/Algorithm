alpha = [chr(x) for x in range(65,91)]
def reverseCheck(target):
    now = 0
    while alpha[now] != target:
        now -= 1
    return now

def check(target):
    now = 0
    while alpha[now] != target:
        now += 1
    return now

def ShortestPath(name,now,namelen):
    # Shortest Path
    l = r = 0
    if name[now] != "-":
        return "R",now,0
    while l!=namelen-1:
        l+=1
        if name[now-l] != "-":
            break
    while now+r<namelen:
        if now == namelen-1:
            r = now
            break
        r+=1
        if name[now+r] != "-":
            break
        if now+r == namelen-1:
            r+=now
            break
    # print("[ L :",l,", R :",r,"]")
    if l < r:
        if now-l < 0:
            return "L",namelen-(abs(now-l)),l
        return "L",now-l,l
    else:
        return "R",now+r,r
def solution(name):
    count = 0
    name = list(name.replace("A","-"))
    namelen = len(name)
    now = 0
    while True:
        if namelen - name.count("-") == 0:
            break
        direct,selected,moveCount = ShortestPath(name,now,namelen)
        # print(direct,selected,moveCount)
        now = selected
        count += moveCount
        count += min(abs(reverseCheck(name[now])),check(name[now]))
        name[now] = '-'
    return count

print(solution("BBBAAAB")) #8
print(solution("ABABAAAAABA")) #10
print(solution("CANAAAAANAN")) #48
print(solution("ABAAAAABAB")) #8
print(solution("ABABAAAAAB")) #8
print(solution("BABAAAAB")) #7
print(solution("AAA")) #0
print(solution("ABAAAAAAABA")) #6
print(solution("AAB")) #2
print(solution("AABAAAAAAABBB")) #11
print(solution("ZZZ")) #5
print(solution("BBBBAAAAAB")) #10
print(solution("BBBBAAAABA")) #12
print(solution("BBBAAAB"))#9
print(solution("ABABAAAAABA")) #11