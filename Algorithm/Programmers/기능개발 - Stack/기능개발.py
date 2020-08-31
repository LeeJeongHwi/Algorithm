def solution(progresses,speeds):
    answer = []
    days = 0
    complete = []
    for i in range(len(progresses)):
        # print(complete)
        if days != 0:
            if progresses[i] + (speeds[i]*days) >= 100:
                complete.append([progresses[i],speeds[i]])
                continue
            else:
                answer.append(len(complete))
                complete.clear()
        days = 0
        while progresses[i] < 100:
            days += 1
            progresses[i] += speeds[i]
        complete.append([progresses[i],speeds[i]])
    answer.append(len(complete))
    return answer

progresses = [93,30,55]
speeds = [1,30,5]

print(solution(progresses,speeds))