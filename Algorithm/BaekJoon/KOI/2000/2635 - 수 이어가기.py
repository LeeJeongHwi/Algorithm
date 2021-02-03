n = int(input())

max_Len = 1
max_List = [n]
def solve(second_num,ans):
	global max_List,max_Len
	i = 1
	ans.append(second_num)
	while ans[i-1]-ans[i]>=0:
		ans.append(ans[i-1]-ans[i])
		i+=1
	len_Ans = len(ans)
	if len_Ans > max_Len:
		max_Len = len_Ans
		max_List = ans
for i in range(1,n+1):
	ans = [n]
	solve(i,ans)
print(max_Len)
print(*max_List)