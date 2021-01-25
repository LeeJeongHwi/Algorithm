from collections import deque
bridge_length = 100
weight = 100
truck_weight = [10]

def solution(bridge_length,weight,truck_weight):
    q = deque()
    truck_weight = deque(truck_weight)
    time = 0
    nowWeight = 0
    while True:
        time+=1
        # print(q,time)
        if not q:
            if not truck_weight:
                break
        if truck_weight:
            if weight >= nowWeight+truck_weight[0]:
                popWeight = truck_weight.popleft()
                q.append([popWeight,time])
                nowWeight+=popWeight
        if q:
            if time-q[0][1]==bridge_length-1:
                popWeight , _ = q.popleft()
                nowWeight-=popWeight
    return time
print(solution(bridge_length,weight,truck_weight))