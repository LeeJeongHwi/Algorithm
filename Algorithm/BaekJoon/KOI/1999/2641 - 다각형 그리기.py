from sys import stdin
from collections import deque
from copy import deepcopy
# 1 오른쪽 / 2 위쪽 / 3 왼쪽 / 4 아래쪽

size = int(stdin.readline())
train = deque(list(map(int,stdin.readline().split())))
tc=int(stdin.readline())

ans = []

def reverses(tests):
	for i in range(size):
		if tests[i] == 1:
			tests[i] = 3
		elif tests[i] == 2:
			tests[i] = 4
		elif tests[i] == 3:
			tests[i] = 1
		elif tests[i] == 4:
			tests[i] = 2
	return tests

def rotates(tests,command):
	for _ in range(size):
		tests.rotate(command)
		if tests == train:
			ans.append(test)
			return True

for _ in range(tc):
	test = deque(list((map(int,stdin.readline().split()))))
	test_copy1 = deepcopy(test)
	test_copy2 = deepcopy(test)
	#회전검사
	if not rotates(test_copy1,1):
		test_copy2 = reverses(test_copy2)
		# print("reverse direction : ",test_copy2)
		test_copy2.reverse()
		rotates(test_copy2,1)
print(len(ans))
for i in ans:
	print(*i)