# 전화번호 목록

###### 문제 설명

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

- 구조대 : 119
- 박준영 : 97 674 223
- 지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

##### 제한 사항

- phone_book의 길이는 1 이상 1,000,000 이하입니다.
- 각 전화번호의 길이는 1 이상 20 이하입니다.

##### 입출력 예제

| phone_book                        | return |
| --------------------------------- | ------ |
| ["119", "97674223", "1195524421"] | false  |
| ["123","456","789"]               | true   |
| ["12","123","1235","567","88"]    | false  |

##### 입출력 예 설명

입출력 예 #1
앞에서 설명한 예와 같습니다.

입출력 예 #2
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

입출력 예 #3
첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

------

**알림**

2019년 5월 13일, 테스트 케이스가 변경되었습니다. 이로 인해 이전에 통과하던 코드가 더 이상 통과하지 않을 수 있습니다.

[출처](https://ncpc.idi.ntnu.no/ncpc2007/ncpc2007problems.pdf)



### Code

```python
def solution(phone_book):
    phone_book.sort()
    l = len(phone_book)
    for i in range(0,l):
        for j in range(i+1,l):
            if not (phone_book[j].find(phone_book[i])):
                return False
    return True
```

### Solution

최적화시킬 부분을 찾기 위해서 우선 완전탐색으로 풀어볼까..? 하면서 풀었는데.. 맞았다.

문제 구분은 해쉬인데.. 흠



우선 `phone_book`을 사전순으로 정렬했다. 그리고 단순하게 하나씩 비교했다.

`find`함수는 인자로 주어진 문자열이 해당 문자열에 있는지 찾는 함수이다.

그에 따라 0,-1 을 반환하는데, 0이면 문자열이 존재한다는 뜻이므로 False 를 Return 한다.

이 코드는 최악의 경우 `O(n^2)` 인데.. 왜 통과한지 모르겠다.

> 효율성 측면에선 3.x ms 가 나왔다.

 

다른 풀이 코드에서 `startswith` 이라는 함수를 보았다.

```
str1.startswith(str2, beg=0,end=len(string));
```

* `str2` : 찾으려는 문자열
* `beg` : 시작지점
* `end` : 종료지점

만약 존재하면 `True`를 반환하고 아니면 `False`를 반환한다.

[Python Docs 참고](https://docs.python.org/3/library/stdtypes.html?highlight=startswith#str.startswith)



해쉬로 푼 다른사람의 코드도 있다.

```python
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
```
