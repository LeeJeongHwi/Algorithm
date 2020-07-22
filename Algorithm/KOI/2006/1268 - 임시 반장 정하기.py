from sys import stdin
stdin = open("input.txt","r")
n = int(stdin.readline())
students = [list(map(int,stdin.readline().split())) for _ in range(n)]
def check(number,grade,same_class):
    # i == 현재 i번째 학생, number = n번째 학생, grade == 비교 학년
    for i in range(number+1,n):
        if students[i][grade] == students[number][grade]:
            if same_class[i] == 0:
                same_class[i] = 1
    for i in range(number-1,-1,-1):
        if students[i][grade] == students[number][grade]:
            if same_class[i] == 0:
                same_class[i] = 1
max_count,max_index = -1,1001
for i in range(0,n):
    same_class = [0 for _ in range(n)]
    for j in range(5):
        check(i,j,same_class)
    count = same_class.count(1)
    if max_count < count:
        max_index = i
        max_count = count
    elif max_count == count and i < max_index:
        max_index = i
    # print(i+1,same_class)
print(max_index+1)