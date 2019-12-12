from sys import stdin

E,S,M = map(int,stdin.readline().split())
e,s,m,year = 1,1,1,1

while True:
        if(E==e and S==s and M==m):
                break
        else:
                e+=1
                if e==16:
                        e=1
                s+=1
                if s==29:
                        s=1
                m+=1
                if m==20:
                        m=1
        year+=1
print(year)

#Year-E = 15의 배수
#Year-S = 28의 배수
#Year-M = 19의 배수
