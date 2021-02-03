p = ["(()())()",")(","()))((()"]
def check(p): # Bracket Balance Check
    st = []
    for br in p:
        if br == "(":
            st.append(br)
        elif br == ")":
            if st:
                st.pop()
            else:
                return False
    if st:
        return False
    else:
        return True

def split_uv(p):
    u,v = "",""
    rightCount, leftCount = 0,0
    for br in p:
        if br == "(":
            rightCount +=1
        elif br == ")":
            leftCount +=1
        if rightCount == leftCount:
            if rightCount != 0 and leftCount != 0:
                u = p[:rightCount+leftCount]
                v = p[rightCount+leftCount:]
                return u,v
    
def reshape(p):
    if p == "":
        return p
    u,v = split_uv(p)
    if not check(u):
        ans = "("
        ans += reshape(v)
        ans += ")"
        subans = ""
        for i in u[1:-1]:
            if i == "(":
                subans += ")"
                continue
            subans+="("
        ans += subans
        return ans
    return u+reshape(v)

def solution(p):
    #Balance Check
    if not check(p): #if False, we have to Rearrange
        return reshape(p)
    return p

for pi in p:
    print(solution(pi))