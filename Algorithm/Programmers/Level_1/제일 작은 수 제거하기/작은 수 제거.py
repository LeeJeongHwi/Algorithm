arr = [4,3,2,1]

def solution(arr):
    arr.pop(arr.index(min(arr)))
    if (len(arr)==0):
        return [-1]
    else:
        return arr
print(solution(arr))