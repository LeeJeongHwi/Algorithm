import math
a,b,v = map(int,input().split())
print(math.ceil((v-b)/(a-b)))

# 만약 10미터
# 3 1 8

# 3-2 5-4 7-6 8

# 2미터씩 올라가는데
# 1미터씩 떨어짐
# 그리고 최대 5미터를 올라가야함
# 2-1 3-2 4-3 5
# B-A/V-1 씩 올라감 
