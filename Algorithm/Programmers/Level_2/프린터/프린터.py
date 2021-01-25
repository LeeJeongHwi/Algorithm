from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    ans = []
    for i,p in enumerate(priorities):
        q.append((i,p))
    while q:
        i,p = q.popleft()
        if q:
            if p >= max(q,key=lambda x:x[1])[1]:
                ans.append((i,p))
                if i == location:
                    return len(ans)
                continue
            q.append((i,p))
        else:
            ans.append((i,p))
#    for i in range(len(ans)):
 #       if ans[i][0] == location:
  #          answer = i+1
   #         break
    #return answer