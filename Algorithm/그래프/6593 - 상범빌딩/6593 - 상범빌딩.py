from sys import stdin
from collections import deque

dz = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dx = [1,-1,0,0,0,0]
def bfs(start,end,maps,visit):
    q = deque()
    q.append(start)
    visit[start[0]][start[1]][start[2]] = 1
    while q:
        z,y,x = q.popleft()
        for i in range(6):
            nz,ny,nx = dz[i]+z,dy[i]+y,dx[i]+x
            if 0<=nz<floor and 0<=ny<n and 0<=nx<m:
                if maps[nz][ny][nx] == '.' and visit[nz][ny][nx] == 0:
                    visit[nz][ny][nx] = visit[z][y][x]+1
                    q.append((nz,ny,nx))
                if maps[nz][ny][nx] == 'E' and visit[nz][ny][nx] == 0:
                    print("Escaped in",visit[z][y][x],"minute(s).")
                    return
    print("Trapped!")

def searchSE(maps):
    start,end =0,0
    for k in range(floor):
        for i in range(n):
            for j in range(m):
                if maps[k][i][j] == 'S':
                    start = [k,i,j]
                if maps[k][i][j] == 'E':
                    end = [k,i,j]
    return start,end
def solve(floor,n,m):
    visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(floor)]
    maps = []
    for i in range(floor):
        ms = [[x for x in stdin.readline().rstrip()] for _ in range(n)]
        maps.append(ms)
        stdin.readline()
    start,end = searchSE(maps)
    bfs(start,end,maps,visit)
#main
if __name__ == "__main__":
    stdin = open('input.txt','r')
    while True:
        floor,n,m = map(int,stdin.readline().split())
        if (floor,n,m) == (0,0,0):
            break
        solve(floor,n,m)

    