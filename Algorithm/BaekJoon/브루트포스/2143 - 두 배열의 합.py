from sys import stdin

t = int(input())

n = int(input())

a = list(map(int,stdin.readline().split()))

m = int(input())

b = list(map(int,stdin.readline().split()))

aset = [0]
bset = [0]

def twoPointer(arr,arrSize,sumset):
	left , right = 0,0
	result = 0

	while True:
		if result >= t:
			result -= arr[left]
			left+=1
			sumset.append(result)
		elif right == arrSize:
			break
		else:
			result += arr[right]
			right+=1
			sumset.append(result)

twoPointer(a,n,aset)
twoPointer(b,m,bset)

print(aset)
print(bset)
cnt = 0
for an in aset:
	for bn in bset:
		if an+bn == t:
			cnt+=1
print(cnt)