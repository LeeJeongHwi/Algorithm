# 주식가격

###### 문제 설명

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

##### 제한사항

- prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
- prices의 길이는 2 이상 100,000 이하입니다.

##### 입출력 예

| prices          | return          |
| --------------- | --------------- |
| [1, 2, 3, 2, 3] | [4, 3, 1, 1, 0] |

##### 입출력 예 설명

- 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
- 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
- 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
- 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
- 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

※ 공지 - 2019년 2월 28일 지문이 리뉴얼되었습니다.



### Code

```python
def solution(prices):
    ans = []
    st = [] # -1 : top
    limit= len(prices)
    for i,price in enumerate(prices):
        # print("now : ",i,price,limit-(i+1))
        if not st:
            st.append((price,limit-(i+1),i))
            continue
        while True:
            if not st:
                st.append((price,limit-(i+1),i))
                break
            if st[-1][0] > price:
                pop_price,pop_time,pop_i = st.pop()
                ans.append((pop_time-(limit-(i+1)),pop_i))
            else:
                st.append((price,limit-(i+1),i))
                break
    while st:
        _,time,i = st.pop()
        ans.append((time,i))
    ans.sort(key=lambda x:x[1])
    return [x[0] for x in ans]

```



### 풀이

해당 문제는 `stack/queue`로 구분되어 있는데, 아무리 생각해도 `for`문 으로 밖에 생각이 나지 않았다. 내가 푼 코드도 과연 `O(n^2)` 인지 `O(n)` 인지 모르겠다.

`stack`에는 `[price, 스택에 머무를 시간(= prices전체길이 - (index +1)), index]` 이렇게 들어간다.

알고리즘은 `Top`의 `price`가 현재 시각의 `price`보다 작을 때 `stack.pop`을 수행한다. 만약 자기보다 작은 `price`라면 stack에 현재 시간이 들어간다.

`pop`된 원소들은 `ans`에 `[스택에 머무를 시간(=전체길이 - (index+1)) - pop할 때의 시간, index]` 이 들어간다.

`while`문 바로 밑에 있는 `if not st`문은 stack에 다 빠져나갔을 경우를 위한 예외처리 문이다. (순서를 바꾸면 예외처리 문을 없애도 될 것 같음)

마지막으로 스택에 남아있는 원소들을 ans에 옮겨주고 , index 순으로 정렬한다.



ex)

> **(price, time, index)**
>
> st = [(1,4,0),(2,3,1),(3,2,2)] <- (2,1,3) 이 들어올려 할 때 (3,2,2) pop 하고 , (들어간 타임 - 비교한 시간 , index) 을 ans에 append
>
> st = [(1,4,0),(2,3,1),(2,1,3)] <- (3,0,4) ==> st = [(1,4,0),(2,3,1),(2,1,3),(3,0,4)]

