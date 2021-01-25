strings = ["abcd","abce","cdx"]
n = 2

def solution(strings,n):
    return sorted(sorted(strings),key=lambda x:x[n])

print(solution(strings,n))