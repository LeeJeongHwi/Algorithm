n = 3
lost = [1,2]
reserve = [2,3]

def solution(n,lost,reserve):
    new_lost = list(set(lost)-set(reserve))
    new_reserve = list(set(reserve)-set(lost))
    # print(new_lost)
    # print(new_reserve)
    now = n - len(new_lost)
    for i in new_lost:
        if i+1 in new_reserve:
            new_reserve[new_reserve.index(i+1)] = -1
            now+=1
        elif i-1 in new_reserve:
            new_reserve[new_reserve.index(i-1)] = -1
            now+=1
    return now

print(solution(n,lost,reserve))