from sys import stdin,setrecursionlimit
setrecursionlimit(10**9)
"""
number = [a,f,b,d,c,e]
A <-> F / B <-> D / C <-> E
"""
stdin = open("input.txt","r")
n=int(stdin.readline())
dice = []
max_score = 0 
for _ in range(n):
    a,b,c,d,e,f = map(int,stdin.readline().split())
    dice.append([a,f,b,d,c,e])
# for i in dice:
#     print(i)
# print("=====================")
def get_top(bottom):
    top = 0
    if bottom%2 == 1:
        top = bottom-1
    elif bottom%2 == 0:
        top = bottom+1
    return top
def get_max(top,bottom,diceNum):
    nlist = [dice[diceNum][x] for x in range(6) if x!=top and x!=bottom]
    return max(nlist)
def solve(diceNum,top,bottom,maxList): #n = 주사위번호,
    if diceNum == n: #주사위를 다 돌았음
        global max_score
        max_score = max(max_score,sum(maxList))
        return
    bottom_ = dice[diceNum].index(dice[diceNum-1][top])
    top_ = get_top(bottom_)
    maxList.append(get_max(top_,bottom_,diceNum))
    solve(diceNum+1,top_,bottom_,maxList)
for bottom in range(6):
    top = get_top(bottom)
    maxNum = get_max(top,bottom,0)
    solve(1,top,bottom,[maxNum])
print(max_score)
