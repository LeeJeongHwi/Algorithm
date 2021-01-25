
prices = [3,4,2,6,5]
def solution(prices):
    ans = []
    st = [] # -1 : top
    limit= len(prices)
    for i,price in enumerate(prices):
        # print("now : ",i,price,limit-(i+1))
        if not st:
            st.append((price,limit-(i+1),i))
            continue
        while True:
            if not st:
                st.append((price,limit-(i+1),i))
                break
            if st[-1][0] > price:
                pop_price,pop_time,pop_i = st.pop()
                ans.append((pop_time-(limit-(i+1)),pop_i))
            else:
                st.append((price,limit-(i+1),i))
                break
    while st:
        _,time,i = st.pop()
        ans.append((time,i))
    ans.sort(key=lambda x:x[1])
    return [x[0] for x in ans]

    
print(solution(prices))