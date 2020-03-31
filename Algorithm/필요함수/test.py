arr=[1,2,3,4,5]
n=4
for i in range(0,n//2):
	arr[n-i-1],arr[i] = arr[i],arr[n-i-1]
print(arr)