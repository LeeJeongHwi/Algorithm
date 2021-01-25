# 카펫

###### 문제 설명

Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

![carpet.png](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/b1ebb809-f333-4df2-bc81-02682900dc2d/carpet.png)

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
- 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
- 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

##### 입출력 예

| brown | yellow | return |
| ----- | ------ | ------ |
| 10    | 2      | [4, 3] |
| 8     | 1      | [3, 3] |
| 24    | 24     | [8, 6] |

[출처](http://hsin.hr/coci/archive/2010_2011/contest4_tasks.pdf)

※ 공지 - 2020년 2월 3일 테스트케이스가 추가되었습니다.
※ 공지 - 2020년 5월 11일 웹접근성을 고려하여 빨간색을 노란색으로 수정하였습니다.



### Code

```python
def solution(brown,yellow):
    height = 1
    while ((brown-(height*2)) // 2)-2 != 0:
        width = ((brown-(height*2)) // 2)-2
        if width*height == yellow and width>=height:
            return [width+2,height+2]
        height+=1
```

### Solution

`height` 를 기준으로 완전탐색을 수행했다. (height가 더 짧기 때문)

`height` 와 `width`는 Yellow의 갯수를 탐색하기 위한 용도이다.

`((brown - (height*2))) // 2) -2 ` 는 `height`의 수가 증가함과 동시에 Yellow를 담을 가로 길이가 `-1`씩 줄어들게되므로 0이 되면 해당 문제가 성립되지 않아 조건문으로 걸었다.

문제에서 가로길이가 세로길이보다 길다고 했으므로 `width>=height` 를 걸어주었고 `width*height` 는 yellow의 갯수를 의미한다.



`+2점`