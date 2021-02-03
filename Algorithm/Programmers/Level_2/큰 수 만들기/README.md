# 큰 수 만들기

###### 문제 설명

어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

##### 제한 조건

- number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
- k는 1 이상 `number의 자릿수` 미만인 자연수입니다.

##### 입출력 예

| number     | k    | return |
| ---------- | ---- | ------ |
| 1924       | 2    | 94     |
| 1231234    | 3    | 3234   |
| 4177252841 | 4    | 775841 |

[출처](http://hsin.hr/coci/archive/2011_2012/contest4_tasks.pdf)



### Code

```python
def solution(number,k):
    strlen = len(number)
    anslen = strlen-k
    st=[number[0]]
    minus = 0 
    for i in range(1,strlen): 
        if st:
            while True:
                if st and st[-1] < number[i] and minus != k:
                    st.pop()
                    minus+=1
                    continue
                st.append(number[i])
                break
    if minus == 0:
        return ''.join(st[:anslen])
    return ''.join(st)
```

### Solution

[정답](https://scarletbreeze.github.io/articles/2019-07/pythonKit%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4(4)%ED%83%90%EC%9A%95%EB%B2%95%ED%81%B0%EC%88%98) 을 보고 해결함.

그리디 유형보단 Stack 문제에 가깝다.

`minus`는 뺀 갯수를 추적하는 변수이다.

`number[i]` 이 `top` 보다 작아질 때 까지 `stack`을 `pop`한다. 만약 `top`보다 작을시에는 그냥 `number[i]`를 `append`한다. 그리고 뺄 때 `pop`한 갯수를 체크해준다.

만약 `98765` 와 같이 내림차순으로 수가 정렬되어 있다면 빼지 않으므로 인덱스 `[0]`부터 `원래길이-k` 만큼 까지의 문자열을 리턴한다.

`4177252841, k=4` 를 예시로 들어보면

|  i   | number[i] | stack         | minus |
| :--: | --------- | ------------- | ----- |
|  0   | 4         | [4]           | 0     |
|  1   | 1         | [4,1]         | 0     |
|  2   | 7         | [7]           | 2     |
|  3   | 7         | [7,7]         | 2     |
|  4   | 2         | [7,7,2]       | 2     |
|  5   | 5         | [7,7,5]       | 3     |
|  6   | 2         | [7,7,5,2]     | 3     |
|  7   | 8         | [7,7,5,8]     | 4     |
|  8   | 4         | [7,7,5,8,4]   | 4     |
|  9   | 1         | [7,7,5,8,4,1] | 4     |

* `number[7]` 인 `8` 이 들어갈 땐  `2` 를 `pop`하고 난 뒤`minus` (= 뺀 갯수) 가 `k`와 동일하기 때문에 더 이상 `pop` 하지 않는다.

시간복잡도 : `O(n)`

`+6` 