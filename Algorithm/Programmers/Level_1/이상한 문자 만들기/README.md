# 이상한 문자 만들기

###### 문제 설명

문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

##### 제한 사항

- 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
- 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

##### 입출력 예

| s               | return          |
| --------------- | --------------- |
| try hello world | TrY HeLlO WoRlD |

##### 입출력 예 설명

try hello world는 세 단어 try, hello, world로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 TrY, HeLlO, WoRlD입니다. 따라서 TrY HeLlO WoRlD 를 리턴합니다.



### Code

```python
def solution(s):
    j = 0
    ans = []
    for i in range(len(s)):
        if s[i] == " ":
            j = 0
            ans.append(s[i])
            continue
        elif j%2==0:
            ans.append(s[i].upper())
            j+=1
        elif j%2!=0:
            ans.append(s[i].lower())
            j+=1
    return ''.join(ans)
```



### 접근 방법

여기서 핵심은 `공백` 을 기준으로 짝수 홀수를 정하는 것이다.

`j`는 공백 기준으로 index를 참조하는 것이다.

`split`으로 체크한 방법은 다음과 같다.

```python
def solution(s):
    ans = []
    for string in s.split(" "):
        newStr = ""
        for i in range(len(string)):
            if i%2==0:
                newStr+=string[i].upper()
            else:
                newStr+=string[i].lower()
        ans.append(newStr)
    return " ".join(ans)
```

프로그래머스는 split을 할 때 `" "` 로 공백을 체크해야한다.

