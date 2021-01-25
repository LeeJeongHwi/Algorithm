# S **1 / D **2 / T **3
# * : 2배 / # : -1배
# *는 다른 스타상과 중첩됨 *
import re
dartResult = ["1S2D*3T","1D2S#10S",'1D2S0T',
              '1S*2T*3S','1D#2S*3S','1T2D3D#',
              "1D2S3T*"]
option = {"*":"*2","#":"*(-1)","S":"**1",
          "D":"**2","T":"**3"}
def solution(result):
    number = re.findall("\d+",result)
    options = re.findall("\D+",result)
    change = [0,0,0]
    for i in range(len(number)):
        change[i] = number[i]
        for o in options[i]:
            if o == "*" and i != 0:
                change[i-1] *= 2
                change[i] *=2
            else:
                change[i] = eval(str(change[i])+option[o])
    return sum(change)

for i in dartResult:
    print(solution(i))
