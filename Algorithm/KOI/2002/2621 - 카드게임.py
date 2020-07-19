from sys import stdin
from collections import Counter
def isSequencial(nlist):
    for i in range(1,5):
        if nlist[i-1]+1 == nlist[i]:
            continue
        return False
    return True
def rule1():
    return 900+max(cardNumber)
def rule2():
    for n in counterNumber:
        if counterNumber[n] == 4:
            return 800+n
def rule3():
    ans = 0
    for n in counterNumber:
        if counterNumber[n] == 3:
            ans += 10*n
        elif counterNumber[n] == 2:
            ans += n
    return ans+700
def rule4():
    return 600+max(cardNumber)
def rule5():
    return 500+max(cardNumber)
def rule6():
    for n in counterNumber:
        if counterNumber[n] == 3:
            return 400+n
def rule7():
    num = []
    for n in counterNumber:
        if counterNumber[n] == 2:
            num.append(n)
    if num:
        return 300 + max(num)*10 + min(num)
def rule8():
    for n in counterNumber:
        if counterNumber[n] == 2:
            return 200+n
def rule9():
    return 100+max(cardNumber)
stdin = open("input.txt","r")
cardAlpha = []
cardNumber = []
for _ in range(5):
    alpha,num = stdin.readline().split()
    cardAlpha.append(alpha)
    cardNumber.append(int(num))
counterAlpha = Counter(cardAlpha)
counterNumber = dict(sorted(Counter(cardNumber).items(),key=lambda x:x[1],reverse=True))
# print(counterAlpha)
# print(counterNumber)
rules = [rule1(),rule2(),rule3(),rule4(),rule5(),rule6(),rule7(),rule8(),rule9()]
def solve():
    rule = 10
    if len(counterAlpha) == 1:
        if isSequencial(sorted(cardNumber)):
            rule = min(rule,1)
            return rule
        else:
            rule = min(rule,4)
    if len(counterNumber) == 2:
        for n in counterNumber:
            if counterNumber[n] == 4:
                rule = min(rule,2)
                break
            elif counterNumber[n] == 3:
                rule = min(rule,3)
                break
    elif isSequencial(sorted(cardNumber)):
        rule = min(rule,5)
    elif len(counterNumber) == 3:
        for n in counterNumber:
            if counterNumber[n] == 3:
                rule = min(rule,6)
                break
            elif counterNumber[n] == 2:
                rule = min(rule,7)
                break
    elif len(counterNumber) ==4:
        for n in counterNumber:
            if counterNumber[n] == 2:
                rule = min(rule,8)
                break
    else:
        rule = min(rule,9)
    return rule
print(rules[solve()-1])