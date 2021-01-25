numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
hands = {"right":"R","left":"L"}
keyPad={1:(1,1),2:(1,2),3:(1,3),4:(2,1),5:(2,2),6:(2,3),7:(3,1),8:(3,2),9:(3,3),"*":(4,1),0:(4,2),"#":(4,3)}
def solution(numbers,hand):
    r_hand = "#"
    l_hand = "*"
    ans = ""
    for num in numbers:
        if num in [3,6,9]: #Right
            r_hand = num
            ans+="R"
        elif num in [1,4,7]: #Left
            l_hand = num
            ans+="L"
        elif num in [2,5,8,0]:
            r_dist = abs(keyPad[r_hand][0]-keyPad[num][0]) + abs(keyPad[r_hand][1]-keyPad[num][1])
            l_dist = abs(keyPad[l_hand][0]-keyPad[num][0]) + abs(keyPad[l_hand][1]-keyPad[num][1])
            if r_dist < l_dist:
                ans+="R"
                r_hand = num
            elif r_dist > l_dist:
                ans+="L"
                l_hand = num
            else:
                ans+=hands[hand]
                if hand=="right":
                    r_hand = num
                else:
                    l_hand = num
    return ans
print(solution(numbers,hand))