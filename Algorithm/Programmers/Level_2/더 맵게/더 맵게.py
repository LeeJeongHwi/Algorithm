# 섞인 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지않은 음식의 스코빌 지수 * 2)
# 스코빌 지수가 k 이상이 될 때 가지 석는다.
# 결과적으로 섞은 횟수를 Return 한다.


scvoille = [1, 2, 3, 9, 10, 12]
K = 7

import heapq as hq
def solution(scvoille,K):
    hq.heapify(scvoille)
    count = 0
    while scvoille:
        mins = hq.heappop(scvoille)
        try:
            mins2 = hq.heappop(scvoille)
        except:
            return -1
        mixed_sc = mins+(mins2*2)
        count+=1
        hq.heappush(scvoille,mixed_sc)
        if scvoille[0] >= K:
            return count

        

print(solution(scvoille,K))