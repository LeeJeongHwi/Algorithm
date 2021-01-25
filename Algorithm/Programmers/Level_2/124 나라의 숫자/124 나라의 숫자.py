numbers = [1,2,3,4,5,6,7,8,9,10,11,13,14,15]
def solution(n):
    ans = []
    number = n
    while True:
        remain = number%3
        number = number//3
        if remain == 0:
            number -= 1
        ans.append(str(remain))
        if number == 0:
                break
        if number < 3:
            if number == 0:
                break
            ans.append(str(number))
            break
    return "".join(reversed(ans)).replace("0","4")

    

for i in numbers:
    print(solution(i))