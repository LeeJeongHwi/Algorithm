def solution(board, moves):
    answer = 0
    basket = []
    for select in moves:
        for item in board:
            if item[select-1] == 0:
                continue
            if basket:
                if basket[-1] == item[select-1]:
                    item[select-1] = 0
                    basket.pop()
                    answer += 2
                    break
            basket.append(item[select-1])
            item[select-1] = 0
            break
    return answer