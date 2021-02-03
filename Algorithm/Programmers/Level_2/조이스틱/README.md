# 조이스틱

###### 문제 설명

조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

```
▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
```

예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.

```
- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
```

만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

##### 제한 사항

- name은 알파벳 대문자로만 이루어져 있습니다.
- name의 길이는 1 이상 20 이하입니다.

##### 입출력 예

| name   | return |
| ------ | ------ |
| JEROEN | 56     |
| JAN    | 23     |

[출처](https://commissies.ch.tudelft.nl/chipcie/archief/2010/nwerc/nwerc2010.pdf)

※ 공지 - 2019년 2월 28일 테스트케이스가 추가되었습니다.



### Code

```python
alpha = [chr(x) for x in range(65,91)]
def reverseCheck(target):
    now = 0
    while alpha[now] != target:
        now -= 1
    return now

def check(target):
    now = 0
    while alpha[now] != target:
        now += 1
    return now

def ShortestPath(name,now,namelen):
    # Shortest Path
    l = r = 0
    if name[now] != "-":
        return "R",now,0
    while l!=namelen-1:
        l+=1
        if name[now-l] != "-":
            break
    while now+r<namelen:
        if now == namelen-1:
            r = now
            break
        r+=1
        if name[now+r] != "-":
            break
        if now+r == namelen-1:
            r+=now
            break
    # print("[ L :",l,", R :",r,"]")
    if l < r:
        if now-l < 0:
            return "L",namelen-(abs(now-l)),l
        return "L",now-l,l
    else:
        return "R",now+r,r
def solution(name):
    count = 0
    name = list(name.replace("A","-"))
    namelen = len(name)
    now = 0
    while True:
        if namelen - name.count("-") == 0:
            break
        direct,selected,moveCount = ShortestPath(name,now,namelen)
        # print(direct,selected,moveCount)
        now = selected
        count += moveCount
        count += min(abs(reverseCheck(name[now])),check(name[now]))
        name[now] = '-'
    return count

# 반례 데이터
print(solution("BBBAAAB")) #8
print(solution("ABABAAAAABA")) #10
print(solution("CANAAAAANAN")) #48
print(solution("ABAAAAABAB")) #8
print(solution("ABABAAAAAB")) #8
print(solution("BABAAAAB")) #7
print(solution("AAA")) #0
print(solution("ABAAAAAAABA")) #6
print(solution("AAB")) #2
print(solution("AABAAAAAAABBB")) #11
print(solution("ZZZ")) #5
print(solution("BBBBAAAAAB")) #10
print(solution("BBBBAAAABA")) #12
print(solution("BBBAAAB"))#9
print(solution("ABABAAAAABA")) #11
```

### Solution

우선.. 그리디 문제는 아닌 것 같은데, 그리디식으로 풀어야 답이 된다.

> 하지만 그리디를 보장하지 않음

가장 헷갈린 점은 "어디서 그리디이어야 하는가?" 였다.

그리디를 적용할 지점은 총 2곳이다.

1. 현재 지점에서 가장 가까운 곳에 "알파벳을 바꿀 지점"을 찾아가는데 드는 moveCount의 최소 횟수
2. 타겟 알파벳과 동일하게 맞추기 위해서 역순으로 바꿀 것인지, 아닌지에 대해서 최소 횟수

> 하지만 실제로 이 방식대로 풀면 "진짜 최소 횟수"는 나오지 않는다.

`reverseCheck()` : 이전 알파벳 방향으로 움직인 횟수를 체크

`check()`: 다음 알파벳 방향으로 움직인 횟수를 체크

`shortestPath()` : 오른쪽 , 왼쪽 방향 중 바꿀 지점을 찾아가는 움직임 최소 횟수를 구함

`alpha`는 ["A","B"..."Z"] 로 구성되어 있는 배열이다.

처음에 `name`을 `replace`함수로 `"A"를 "-"`  로 바꿔준 이유는 좀 더 바꿀 알파벳을 쉽게 찾기 위함





`+8`

가장 오래걸린 TC : 5 (`0.06ms`)