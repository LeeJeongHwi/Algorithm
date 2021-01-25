# 다리를 지나는 트럭

###### 문제 설명

트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

| 경과 시간 | 다리를 지난 트럭 | 다리를 건너는 트럭 | 대기 트럭 |
| --------- | ---------------- | ------------------ | --------- |
| 0         | []               | []                 | [7,4,5,6] |
| 1~2       | []               | [7]                | [4,5,6]   |
| 3         | [7]              | [4]                | [5,6]     |
| 4         | [7]              | [4,5]              | [6]       |
| 5         | [7,4]            | [5]                | [6]       |
| 6~7       | [7,4,5]          | [6]                | []        |
| 8         | [7,4,5,6]        | []                 | []        |

따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

##### 제한 조건

- bridge_length는 1 이상 10,000 이하입니다.
- weight는 1 이상 10,000 이하입니다.
- truck_weights의 길이는 1 이상 10,000 이하입니다.
- 모든 트럭의 무게는 1 이상 weight 이하입니다.

##### 입출력 예

| bridge_length | weight | truck_weights                   | return |
| ------------- | ------ | ------------------------------- | ------ |
| 2             | 10     | [7,4,5,6]                       | 8      |
| 100           | 100    | [10]                            | 101    |
| 100           | 100    | [10,10,10,10,10,10,10,10,10,10] | 110    |

[출처](http://icpckorea.org/2016/ONLINE/problem.pdf)

※ 공지 - 2020년 4월 06일 테스트케이스가 추가되었습니다.



### Code

```python
from collections import deque
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
```

### 풀이

`pop`속도를 위하여 `deque`를 사용함 

* [0] 번째 원소를 `pop`시킬 때 `O(1)` 이 소요됨 , 만약 `list`로 한다면 `O(n)` 이 걸리기 때문에 더 느리다.

`nowWeight`는 현재 다리위에 올라가 있는 Weight를 추적하는 변수이다.

`q`와 `truck_weight`가 모두 비워져야 모든 truck이 옮겨진 것이므로 while문 처음에 체크를 해주고 모두 비워져있는 경우 `break`

제한된 weight와 현재 다리위에 올라가져있는 weight에 추가로 더 올릴 `truck_Weight`를 더했을 때 제한된 weight보다 작으면 트럭을 올릴 수 있다는 뜻이므로 `truck_weight.popleft()` 를 수행한다.

`[popWeight,time]` 에서 time을 넣어주는 이유는 가장 먼저 들어온 트럭이 가장 먼저 나가고 1초에 1개씩만 움직이므로 하나만 체크해주면 된다. 따라서 `현재시간 - 들어간 시간 = 다리길이` 인 경우 다 넘어갔다는 뜻이므로 `q`에서 나오고 `nowWeight` 를 Update 시켜준다. 



다른 사람은 Class 로 해결했는데, 얼마나 걸린지 모르겠다..

<img src="C:\Users\wjdgn\AppData\Roaming\Typora\typora-user-images\image-20210116004151703.png" alt="image-20210116004151703" style="zoom:50%;" />