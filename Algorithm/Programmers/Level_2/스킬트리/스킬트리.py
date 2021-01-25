test = ["A","B","CB","DB","DC","CE"]
skill = 'CBD'

def setSkill(skill,now_Skill,skill_len,substr):
    result = []
    for i in range(skill_len):
        now_Skill = now_Skill.replace(skill[i],str(i+1))
    for now_s in now_Skill:
        if "A" <= now_s <= "Z":
            continue
        result.append(int(now_s))
    if result in substr:
        print(result,now_Skill)
        return True
        

def solution(skill,skill_trees):
    count = 0
    skill_len = len(skill)
    init = [i+1 for i in range(skill_len)]
    substr = [[]]+[init[0:i+1] for i in range(skill_len)]
    for now_Skill in skill_trees:
        if setSkill(skill,now_Skill,skill_len,substr):
            count+=1
    return count

print(solution(skill,test))