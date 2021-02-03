from sys import stdin
stdin = open("input.txt","r")
n = int(stdin.readline())
m = int(stdin.readline())
fix_Seat = [int(stdin.readline()) for _ in range(m)]
all_Seat = [0 for _ in range(n+1)]
# print(fix_Seat)

dp = [0 for _ in range(n+1)]
"""
i번과 i-1번을 변경했을 때 나오는 경우의 수
i = 0
경우의 수 없음 (변경 X) == 1

i = 1
1 번과 0번 변경 ==> X ==> 1
123456789 ==> 1

i = 2
2 번과 1번 변경 ==> 1개가 나옴 ==> 2
213456789 ==> 1

i = 3
3 번과 2번 변경 ==> 1개가 나옴 ==> 3
132456789 ==> 1

i = 4 ==> 픽스 값이라 변경 X ==> 3
i = 5 ==> 4번은 Fix값이라 변경 X ==> 3

i = 6
6 번과 5번 변경 ==> 3개가 나옴 ==> 6
123465789
213465789
132465789 ==> 3

i = 7 ==> 픽스 값이라 변경 X ==> 6
i = 8 ==> 7번이 픽스값이라 변경 X ==> 6
i = 9
9 번과 8번 변경 ==> 6개가 나옴 ==> 12

0 1 2 3 4 5 6 7 8  9
1 1 2 3 3 3 6 6 6 12

dp[i] = dp[i-2] + dp[i-1] ==> Fix가 없을 때
"""
dp[0] = 1
dp[1] = 1
for i in range(2,n+1):
    if i in fix_Seat:
        dp[i] = dp[i-1]
        continue
    if i-1 in fix_Seat:
        dp[i] = dp[i-1]
        continue
    dp[i] = dp[i-2] + dp[i-1]
# print(dp)
print(dp[n])