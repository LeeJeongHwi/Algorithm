from itertools import combinations

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

chiken = []
home = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home.append((i, j))
        if board[i][j] == 2:
            chiken.append((i, j))

chiken_distance = [[abs(h[0] - c[0]) + abs(h[1] - c[1]) for c in chiken] for h in home]
print(chiken_distance)
chikenable = combinations(range(len(chiken)), M)
min_v = float('inf')

for case in chikenable:
    print(case)
    sum_v = 0
    for h in chiken_distance:
        sum_v += min([h[idx] for idx in case])
    min_v = min(min_v, sum_v)

print(min_v)