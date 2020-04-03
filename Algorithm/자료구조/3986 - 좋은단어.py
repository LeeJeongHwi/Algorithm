from sys import stdin
n = int(input())
count=0
for i in range(n):
	s = stdin.readline().rstrip()
	ac = s.count("A")
	bc = s.count("B")
	if ac%2!=0 or bc%2!=0:
		continue

	for i in range(len(s)//2):
		if (s==''):
			count+=1
			break
		s = s.replace('BB',"").replace('AA',"")
		s = s.replace("AA","").replace("BB","")
print(count)

#좋은 풀이

num_of_good_words = 0

for _ in range(int(input())):
	word, temp = input(), ""
	while word != temp:
		print("TEMP:",temp,"WORD:",word)
		temp, word = word, word.replace("AA", "").replace("BB", "")
	if not word:
		num_of_good_words += 1

print(num_of_good_words)