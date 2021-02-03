from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)
stdin = open('input.txt','r')

n = int(stdin.readline())
maps = [list(map(int,stdin.readline().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
def dfs(y,x):
    if (y,x) == (n-1,n-1):
        return 1
    if maps[y][x] == 0:
        return 0
    if dp[y][x] == -1:
        dp[y][x] = 0
        if y + maps[y][x] < n:
            dp[y][x]+=dfs(y+maps[y][x],x)
        if x + maps[y][x] < n:
            dp[y][x]+=dfs(y,x+maps[y][x])
    return dp[y][x]
dfs(0,0)
# for i in dp:
#     print(i)
print(dfs(0,0))