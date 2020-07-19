from sys import stdin
stdin = open("input.txt","r")

maps = [list(map(int,stdin.readline().split())) for _ in range(19)]

def check(y,x,dyx,bh):
    count = 1
    while True:
        y+=dyx[0] #y+dy
        x+=dyx[1] #x+dx
        #한 방향으로 이동
        if 0<=y<19 and 0<=x<19:
            if maps[y][x] == bh:
                count+=1
            else:
                break
        else:
            break
    return count

ans = []
def search(y,x,bh):
    d = [(0,1),(0,-1),(-1,1),(1,-1),(1,0),(-1,0),(1,1),(-1,-1)]
    for i in range(8):
        if 0<=y+d[i][0]<19 and 0<=x+d[i][1]<19:
            if maps[y+d[i][0]][x+d[i][1]] == bh:
                count = check(y,x,d[i],bh)
                if count == 5:
                    #역방향 검사
                    if i%2==0:
                        if 0<=y+d[i+1][0]<19 and 0<=x+d[i+1][1]<19:
                            if maps[y+d[i+1][0]][x+d[i+1][1]] == bh:
                                continue
                    elif i%2==1:
                        if 0<=y+d[i-1][0]<19 and 0<=x+d[i-1][1]<19:
                            if maps[y+d[i-1][0]][x+d[i-1][1]] == bh:
                                continue
                    # print(bh)
                    # print(y+1,x+1)
                    ans.append([y+1,x+1])
def solve():
    for i in range(19):
        for j in range(19):        
            if (maps[i][j] == 1 or maps[i][j] == 2):
                if search(i,j,maps[i][j]) :
                    continue
    return False
solve()
if ans :
    ans.sort(key=lambda x:(x[1],x[0]))
    print(maps[ans[0][0]-1][ans[0][1]-1])
    print(*ans[0])
else:
    print(0)