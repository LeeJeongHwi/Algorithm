#solution : https://home-body.tistory.com/126
from sys import stdin

m,n = map(int,stdin.readline().split())

t = int(stdin.readline())

w = [0]
h = [0]
max_w = 0
max_h = 0
for _ in range(t):
	cut,cut_num = map(int,stdin.readline().split())
	if cut == 0:
		w.append(cut_num)
	elif cut == 1:
		h.append(cut_num)
w.sort()
w.append(n)
h.sort()
h.append(m)

# print(w)
# print(h)
for i in range(len(w)-1):
	if w[i+1]-w[i] > max_w:
		max_w = w[i+1]-w[i]
for i in range(len(h)-1):
	if h[i+1]-h[i] > max_h:
		max_h = h[i+1]-h[i]

print(max_h*max_w)