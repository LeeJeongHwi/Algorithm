s = "01033334444"
def solution(phone_number):
    return len(phone_number[:-4])*"*"+phone_number[-4:]
print(solution(s))