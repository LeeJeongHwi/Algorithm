from sys import stdin
stdin = open("input.txt","r")

n = int(stdin.readline())
cars = [0]+list(map(int,stdin.readline().split()))
max_cars = int(stdin.readline())
dp = [[0 for _ in range(n+1)] for _ in range(4)]
# print(cars[1:])
max_score = 0
"""
dp[a][b] = 기관차 a개 일때, 객차 선택 값
"""
sum_person = [0 for _ in range(n+1)]
sum_person[1] = cars[1]
for i in range(2,n+1):
    sum_person[i] = sum_person[i-1]+cars[i]
# print(sum_person)
for i in range(1,4):
    for j in range(i*max_cars,n+1):
        sums = sum_person[j] - sum_person[j-max_cars]
        dp[i][j] = max(dp[i][j-1],dp[i-1][j-max_cars]+sums)
print(dp[3][n])