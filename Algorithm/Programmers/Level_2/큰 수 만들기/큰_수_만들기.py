number = "4177252841"
k = 4
def solution(number,k):
    strlen = len(number)
    anslen = strlen-k
    st=[number[0]]
    minus = 0 
    for i in range(1,strlen):
        
        if st:
            while True:
                if st and st[-1] < number[i] and minus != k:
                    st.pop()
                    minus+=1
                    print(st)
                    continue
                st.append(number[i])
                print(st)
                break
    if minus == 0:
        return ''.join(st[:anslen])
    return ''.join(st)
            
        

print(solution(number,k))