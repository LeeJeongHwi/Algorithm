from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)
n = int(stdin.readline())

numlist = [x for x in range(n,0,-1)]
stack = []
target = []
answer = ""
def find(tragetlist,idx):
	global answer
	if idx > n-1:
		return True
	if stack and tragetlist[idx] == stack[-1]:
		answer += '-'
		stack.pop()
		idx+=1
	else:
		if not numlist and idx <n:
			return False
		stack.append(numlist.pop())
		answer+= '+'
	return find(tragetlist,idx)

for i in range(n):
	target.append(int(stdin.readline()))

if find(target,0):
	for a in answer:
		print(a)
else:
	print("NO")

#더 효율적인 코드
import sys
In = sys.stdin.readline
Out = sys.stdout.write

def produce(seq):
    cur = 1
    stack = [0]
    result = ''
    for x in seq:
        while cur <= x:
            stack.append(cur)
            result += '+\n'
            cur += 1
        if stack.pop() != x:
            Out("NO\n")
            return
        else:
            result += '-\n'
    Out(result)

def main():
    n = int(In())
    seq = [int(In()) for x in range(n)]
    produce(seq)

main()