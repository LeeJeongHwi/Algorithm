"""
N = 3*(2^k)
Solution : https://lazineer.tistory.com/179
"""
# 현재의 도형을 뒤에 2개를 추가시키고 그다음 도형을 오른쪽으로 Shift 시킴
import math
from sys import stdin

n = int(stdin.readline())
figure = ["  *   "," * *  ","***** "]

def make_star(shift):
	c = len(figure)
	for i in range(c):
		#figure[i] == 현재의 도형
		figure.append(figure[i]+figure[i])
		figure[i] = ("   "*shift + figure[i] + "   " * shift)

k = int(math.log(n/3,2))
for i in range(k):
	make_star(int(pow(2,i)))

for i in figure:
	print(i)