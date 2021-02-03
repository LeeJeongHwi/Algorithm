#pypy3 으로 문제해결 - python3 시간초과
from sys import stdin
from collections import deque
import copy

n,m = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]
visit = [[0]*(m) for _ in range(n)]
newMaps = copy.deepcopy(maps)

def melts(sy,sx,maps,newMaps,visit):
	queue = deque()
	queue.append((sy,sx))
	visit[sy][sx] = 1
	while queue:
		y,x = queue.popleft()
		for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
			ny = y+dy
			nx = x+dx
			if 0<=ny<n and 0<=nx<m:
				if maps[ny][nx] == 0:
					if newMaps[y][x] != 0:
						newMaps[y][x] -= 1
				elif visit[ny][nx] == 0:
					visit[ny][nx] = 1
					queue.append((ny,nx))
def solve():
	global maps
	year = 0
	while True:
		count = 0
		newVisit = copy.deepcopy(visit)
		for i in range(n):
			for j in range(m):
				if maps[i][j] != 0 and newVisit[i][j] == 0:
					count+=1
					melts(i,j,maps,newMaps,newVisit)
					if count >= 2:
						return year
		if count == 0:
			return 0
		maps = copy.deepcopy(newMaps)
		year+=1

print(solve())

#효율적인 코드 - https://www.acmicpc.net/source/17917774

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def melt(year):
    visited = [[0] * M for _ in range(N)]
    Q = deque()
    check = 0
    divided = 0
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if iceberg[i][j] and not visited[i][j]:
                check = 1
                divided += 1
                visited[i][j] = 1
                Q.append((i, j))

                while Q:
                    x, y = Q.popleft()
                    cnt = 0
                    for d in range(4):
                        tx, ty = x + dx[d], y + dy[d]
                        if not visited[tx][ty] and not iceberg[tx][ty]:
                            cnt += 1
                        elif not visited[tx][ty] and iceberg[tx][ty]:
                            visited[tx][ty] = 1
                            Q.append((tx, ty))
                    if iceberg[x][y] - cnt < 0:
                        iceberg[x][y] = 0
                    else:
                        iceberg[x][y] -= cnt
    if divided > 1:
        return year
    elif not divided:
        return 0

    if check:
        return melt(year+1)


N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]
print(melt(0))