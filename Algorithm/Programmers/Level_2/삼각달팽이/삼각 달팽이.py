# https://daphne-dev.github.io/2020/09/24/algo-022/
def solution(n):
    arr = [[0 for _ in range(i+1)] for i in range(n)]
    # 경우의수 는 3가지
    # 1. y축이 증가하면서 수가 증가
    # 2. x축이 증가하면서 수가 증가
    # 3. y,x축이 감소하면서 수가 증가
    size = n
    num = 0
    x = 0
    y = -1
    while True:
        # 1번
        for _ in range(size):
            num += 1
            y += 1
            arr[y][x] = num
        size-=1
        if size == 0:
            break
        # 2번
        for _ in range(size):
            num += 1
            x += 1
            arr[y][x] = num
        size-=1
        if size == 0:
            break
        # 3번
        for _ in range(size):
            num += 1
            x -= 1
            y -= 1
            arr[y][x] = num
        size-=1
        if size == 0:
            break
    answer = []
    for i in arr:
        answer.extend(i)
    return answer
# print(solution(4))