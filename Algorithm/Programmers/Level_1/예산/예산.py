d = [1,3,2,5,4]
budget = 9
# Greedy
def solution(d,budget):
    d.sort()
    for i in range(len(d)):
        if budget-d[i] >= 0:
            budget-=d[i]
            continue
        return i
    return len(d)
print(solution(d,budget))