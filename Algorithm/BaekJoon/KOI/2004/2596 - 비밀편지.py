from sys import stdin
stdin = open("input.txt","r")

n = int(stdin.readline())
words = {
    "000000" : "A",
    "001111" : "B",
    "010011" : "C",
    "011100" : "D",
    "100110" : "E",
    "101001" : "F",
    "110101" : "G",
    "111010" : "H",
}
words_key = ["000000","001111","010011","011100","100110","101001","110101","111010"]
strs = "0"+stdin.readline().rstrip()
def check(s):
    for w in words_key:
        count = 0
        for i in range(0,6):
            if s[i] != w[i]:
                count+=1
        if count==0:
            return words[s]
        if count==1:
            return words[w]
    return 0
def solve():
    ans = []
    s = ""
    for i in range(1,(6*n)+1):
        if i%6 == 0:
            s+=strs[i]
            new = check(s)
            if new == 0:
                print(int(i/6))
                return
            else:
                ans.append(new)      
            s=""
        else:
            s+=strs[i]
    
    print("".join(ans))
solve()