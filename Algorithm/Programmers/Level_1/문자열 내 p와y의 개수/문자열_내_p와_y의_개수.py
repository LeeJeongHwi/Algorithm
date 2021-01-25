s = "pPoooyY"

def solution(s):
    return bool(not (s.count("p")+s.count("P"))-(s.count("y")+s.count("Y")))

print(solution(s))