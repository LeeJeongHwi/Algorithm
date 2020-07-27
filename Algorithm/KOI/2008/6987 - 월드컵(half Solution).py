from sys import stdin
stdin = open("input.txt",'r')
ans = []
#a,b,c,d,e,f 경기해야함 ==> 총 15경기
t1=[0,0,0,0,0,1,1,1,1,2,2,2,3,3,4]
t2=[1,2,3,4,5,2,3,4,5,3,4,5,4,5,5]
def dfs(game):
    global flag
    if flag : return
    if game == 15:
        flag = True
        return
    team1 = t1[game]
    team2 = t2[game]
    #team1가 이기는 경우
    if win[team1] > 0 and lose[team2] > 0:
        # print("team1 Win")
        win[team1]-=1
        lose[team2]-=1
        dfs(game+1)
        win[team1]+=1
        lose[team2]+=1
    #team2가 이기는 경우 
    if lose[team1] >0 and win[team2] > 0:
        # print("team2 Win")
        lose[team1] -=1
        win[team2] -=1
        dfs(game+1)
        lose[team1] +=1
        win[team2] +=1
    #팀이 비기는 경우
    if draw[team1] >0 and draw[team2] >0:
        # print("Team Draw")
        draw[team1] -=1
        draw[team2] -=1
        dfs(game+1)
        draw[team1] +=1
        draw[team2] +=1
for i in range(4):
    score = list(map(int,stdin.readline().split()))
    win = [score[0],score[3],score[6],score[9],score[12],score[15]]
    draw = [score[1],score[4],score[7],score[10],score[13],score[16]]
    lose = [score[2],score[5],score[8],score[11],score[14],score[17]]
    flag = False
    if sum(win) + sum(draw) + sum(lose) != 30:
        ans.append(0)
        continue
    dfs(0)
    if flag:
        ans.append(1)
    else:
        ans.append(0)    
print(*ans)