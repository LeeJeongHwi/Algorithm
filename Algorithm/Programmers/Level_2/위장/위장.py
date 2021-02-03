clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes2 = [['a','aa'],['b','aa'],['c','aa'],['a_a','bb'],['b_b','bb'],['c_c','bb'],['aaa','cc'],['bbb','cc'],['ccc','cc']]
clothes3 = [['a','a'],['b','b'],['c','c']]
def solution(clothes):
    state = dict()
    # Dict 생성
    for wear,part in clothes:
        if part not in state:
            state[part] = 1
        else:
            state[part] +=1
    ans = 1
    for i in state.values():
        ans *= i+1
    return ans-1
print(solution(clothes2))
