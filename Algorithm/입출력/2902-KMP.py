from sys import stdin

S = stdin.readline().rstrip()
nS = []
for i in S:
	if i >= 'A' and i <= 'Z':
		nS.append(i)
print(''.join(nS))

# #다른사람 풀이
# A = list(input().split("-"))

# for i in range(len(A)):
#     print(A[i][0],end = "")
# A의 요소들 안에 0번째 요소는 모두 대문자