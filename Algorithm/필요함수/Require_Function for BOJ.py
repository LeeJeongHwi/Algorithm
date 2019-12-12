#BOJ 필요한 함수

import sys
sys.setrecursionlimit(N)

# 파이썬은 제귀함수 제한이 1000으로 되어있다
# 즉 그 수를 넘어가면 런타임에러를 뱉는다. 그래서 그 제한을 해제시키는 것

#list를 만들때 [0]번째에 0 넣고 만드는 법

arr = [0] + list(map(int,sys.stdin.readline().split())