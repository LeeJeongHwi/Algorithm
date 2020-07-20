#solution : https://www.comcbt.com/xe/ctest/2757427
from sys import stdin
stdin = open("input.txt","r")
"""
Red Dot --> Blue Dot --> Yellow Dot
"""
lens = int(stdin.readline())
dots = [list(map(int,stdin.readline().split())) for _ in range(3)]
# print(dots)

#길이가 긴 쪽으로 접는다
for i in range(0,3):
    if dots[i][0] != dots[i][1]:
        mid = (dots[i][0]+dots[i][1])/2
        if (lens-mid)>mid: #오른쪽으로 접기(왼쪽꺼가 오른쪽으로)
            # print("Mid,Len :",mid,lens)
            for j in range(i+1,3):
                for k in range(0,2):
                    if dots[j][k] > mid: #dot이 왼쪽에 있다.
                        # 4 --> 0.5 / 3 --> 1.5 
                        dots[j][k] = lens-dots[j][k]
                    else: #dot이 오른쪽에 있다.
                        # 5 --> 0.5 / 10 --> 5.5       ==> -4.5
                        dots[j][k] += lens-(mid*2)
            lens-=mid
        else:
            for j in range(i+1,3):
                for k in range(0,2):
                    if dots[j][k] > mid:
                        dots[j][k] = mid-(dots[j][k]-mid)
            lens = mid
    # for d in dots:
    #     print(d)
print(lens)
    # print("=======")