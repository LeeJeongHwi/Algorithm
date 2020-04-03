num_of_good_words = 0

for _ in range(int(input())):
	word, temp = input(), ""
	while word != temp:
		print("TEMP:",temp,"WORD:",word)
		temp, word = word, word.replace("AA", "").replace("BB", "")
	if not word:
		num_of_good_words += 1

print(num_of_good_words)