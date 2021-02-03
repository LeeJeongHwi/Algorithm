citations = [10,11,12,13]

# n 개의 논문중, h번 이상 인용된 논문이 h편 이상 / 나머지 논문이 h 번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-index

def solution(citations):
    paper = len(citations)
    citations.sort(reverse=True)
    # i 는 논문의 수 , h는 인용횟수
    # 인용횟수 == 논문의 수 , 인용횟수 < 논문의 수
    for i,h in enumerate(citations):
        print("index :",i+1,"h :",h)
        if i+1==h:
            return h
        elif i+1>h:
            return i
    return paper

print(solution(citations))