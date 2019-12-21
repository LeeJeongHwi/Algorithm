print((1043 % 1000) % 10) # 1의 자리
print((1043 % 100) // 10) # 10의 자리
print((1043 % 1000) // 100) # 100의 자리
print((1043 // 1000)) #1000의 자리

temp_node = 1033
print("1 : ",temp_node%10)
for i in range(1,10):
	k = ((temp_node+i) % 1000) % 10
	k += ((temp_node // 1000) * 1000) + (((temp_node % 1000)//100) * 100) + ((1043 % 100) // 10) * 10
	print(k)