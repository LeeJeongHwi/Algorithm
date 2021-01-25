# H-Index

###### 문제 설명

H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과[1](https://programmers.co.kr/learn/courses/30/lessons/42747#fn1)에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 `n`편 중, `h`번 이상 인용된 논문이 `h`편 이상이고 나머지 논문이 h번 이하 인용되었다면 `h`의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
- 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

##### 입출력 예

| citations       | return |
| --------------- | ------ |
| [3, 0, 6, 1, 5] | 3      |

##### 입출력 예 설명

이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

※ 공지 - 2019년 2월 28일 테스트 케이스가 추가되었습니다.

------

1. https://en.wikipedia.org/wiki/H-index 위키백과 [↩](https://programmers.co.kr/learn/courses/30/lessons/42747#fnref1)



### Code

```python
def solution(citations):
    paper = len(citations)
    citations.sort(reverse=True)
    # i 는 논문의 수 , h는 인용횟수
    # 인용횟수 == 논문의 수 , 인용횟수 < 논문의 수
    for i,h in enumerate(citations):
        if i+1==h:
            return h
        elif i+1>h:
            return i
    return paper
```

### Solution

우선 이 H-index에 대해서 설명이 좀 필요하다.

H-index는 인용횟수와 논문의 수와 같아질 때, 혹은 논문의 수보다 인용의 수가 더 적을 때 H-index라고 한다.

위키백과를 참조했을 때 `25 8 5 3 3`  에서 [3]번째 인덱스의 3이 논문의 수 4보다 작기 때문에 그때의 index인 3을 리턴하게 된다.

만약 모든 배열을 다 탐색했을 때 H-index가 없다면 제일 마지막 index가 H-index이다.

다른 사람의 풀이 중 위키백과에 나온 `max(min(f(i),i)) ,f(i) == 인용`  식을 완벽히 구현한 사람이 있었다.

```python
max(map(min,enumerate(sorted(citations,reverse=True),start=1)))
```



세상엔 천재가 너무 많다.