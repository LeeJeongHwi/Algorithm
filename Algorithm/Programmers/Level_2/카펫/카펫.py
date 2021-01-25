brown = 24
yellow = 24

def solution(brown,yellow):
    height = 1
    while ((brown-(height*2)) // 2)-2 != 0:
        width = ((brown-(height*2)) // 2)-2
        if width*height == yellow and width>=height:
            return [width+2,height+2]
        height+=1
    
    

print(solution(brown,yellow))


#세로의 길이를 완전탐색