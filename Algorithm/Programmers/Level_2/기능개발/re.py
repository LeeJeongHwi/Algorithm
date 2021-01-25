from collections import deque
from math import ceil
progresses = [93, 30, 55]
speeds = [1, 30, 5]

def solution(progresses,speeds):
    complete = deque()
    ans = []
    comp_count = 0
    for p,s in zip(progresses,speeds):
        day = ceil((100-p)/s) # 완료 날짜
        if not complete:
            complete.append(day)
            continue
        if complete[0] < day:
            comp_count+=1
            complete.popleft()
            ans.append(comp_count)
            comp_count=0
            complete.append(day)
        else:
            comp_count+=1
    if complete:
        ans.append(comp_count+1)
    return ans
print(solution(progresses,speeds))