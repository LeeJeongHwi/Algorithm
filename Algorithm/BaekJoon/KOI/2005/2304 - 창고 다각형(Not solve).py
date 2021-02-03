from sys import stdin
stdin = open("input.txt","r")
n = int(stdin.readline())
squares = [list(map(int,stdin.readline().split())) for _ in range(n)]
squares.sort(key=lambda x:x[0])
def get_max():
    max_height = [0,0]
    for i in range(0,n):
        if max_height[1] < squares[i][1]:
            max_height = squares[i]
    return max_height
max_height = get_max()
first = squares[0]
last = squares[-1]
right,left = [squares[0]],[squares[-1]]
#Max 기준으로 Right Check
def right_Check():
    mh = first[1]
    for i in range(1,squares.index(max_height)):
        if mh < squares[i][1]:
            mh = squares[i][1]
            right.append(squares[i])
    right.append(max_height)
def left_Check():
    mh = last[1]
    for i in range(n-2,squares.index(max_height),-1):
        if mh < squares[i][1]:
            mh = squares[i][1]
            left.append(squares[i])
    left.append(max_height)
    left.reverse()
right_Check()
left_Check()
# print(right)
# print(left)
ans = []
def calcRight(right):
    lr = len(right)
    for i in range(1,lr):
        x = right[i][0]-right[i-1][0]
        y = right[i-1][1]
        # print(x,y)
        ans.append(x*y)
def calcLeft(left):
    ll = len(left)
    for i in range(ll-1,0,-1):
        x = left[i][0] - left[i-1][0]
        y = left[i][1]
        # print(x,y)
        ans.append(x*y)
calcRight(right)
calcLeft(left)
ans.append(max_height[1])
print(sum(ans))