from sys import stdin

n = int(stdin.readline())
numlist = list(map(int,stdin.readline().split()))
sign = ['+','-','*','//']
op = list(map(int,stdin.readline().split()))

ans = []
maxAns = -(10**9)
minAns = 10**9
def operation(ans):
	result = numlist[0]
	# print(*ans)
	for i in range(n-1):
		# print("계산 전:",result,"연산자 :",ans[i])
		if ans[i] == '+':
			result += numlist[i+1]
		elif ans[i] == '-':
			result -= numlist[i+1]
		elif ans[i] == '*':
			result *= numlist[i+1]
		elif ans[i] == '//':
			if result < 0:
				result = -(abs(result)//numlist[i+1])
			else:
				result = result//numlist[i+1]
		# print("계산 후:",result)
	return result

def dfs(cnt):
	global maxAns,minAns
	if cnt== n-1:
		calcNum = operation(ans)
		maxAns=max(maxAns,calcNum)
		minAns=min(minAns,calcNum)
		# print("MAX,MIN",maxAns,minAns)
		return
	for i in range(4):
		if op[i] == 0:
			continue
		op[i] -= 1
		ans.append(sign[i])
		dfs(cnt+1)
		ans.pop()
		op[i] += 1
dfs(0)
print(maxAns)
print(minAns)

#더 좋은 답안

def calc(num,idx,add,sub,multi,division):
	if idx == n:
		maxv = max(num,maxv)
		minv = min(num,minv)
		return
	else:
		if add:
			calc(num+numlist[idx],idx+1,add-1,sub,multi,division)
		if sub:
			calc(num-numlist[idx],idx+1,add,sub-1,multi,division)
		if multi:
			calc(num*numlist[idx],idx+1,add,sub,multi-1,division)
		if division:
			calc(int(num/numlist[idx]),idx+1,add,sub,multi,division-1)
calc(numlist[0],1,a,b,c,d)
#abcd는 +-*/
