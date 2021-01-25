# 실패율 = 스테이지 도달했으나 아직 클리어 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# n = 5
# stages = [2,1,2,6,2,4,3,3]
n=4
stages=[4,4,4,4,4]
def solution(n,stages):
    ans = []
    for i in range(1,n+1):
        chal = 0
        err = 0
        for s in stages:
            if s>=i:
                chal+=1
            if s==i:
                err+=1
        if chal == 0:
            ans.append((0,i))
        else:
            ans.append(((err/chal),i))
    ans.sort(reverse=True,key=lambda x:(x[0],-x[1]))
    return [x[1] for x in ans]
print(solution(n,stages))

