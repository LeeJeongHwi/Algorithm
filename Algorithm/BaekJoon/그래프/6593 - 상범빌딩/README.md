# 6593 상범빌딩 
### > Gold 4
#### 초기접근
1. 3차원 배열의 Visit을 사용한다
2. 접근을 동서남북상하로 체크한다
3. (New) Visit[i][j] = (Old) Visit[i][j] + 1로 저장
4. E를 발견했을 때 가장 최저이기 때문에, Flag를 True로 하고 BFS를 빠져나온다.
 4-1. Q에 노드가 없는데, E의 visit이 0이면 못갔다는 뜻이다.

#### 접근방법 수정
- "S"와 "E"의 위치를 구해서 start,end를 만든다. (1-1)
- 만약 map의 nz,ny,nx 가 'E' 이면 print하고 return (4)
- 전체 Q에 노드가 없다면 while을 벗어나기 때문에 print(trapped) 출력 후 BFS 함수 종료 (4-1)

> 사용한 알고리즘 및 자료구조 : BFS / Deque

결과 : AC!
