from sys import stdin

n = int(stdin.readline())

time = list(map(int,stdin.readline().split()))

time.sort()
ans = time[0]
for i in range(1,len(time)):
	time[i] = time[i-1]+time[i]
	ans += time[i] 
print(ans)