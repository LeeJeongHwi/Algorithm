from sys import stdin
stdin = open("input.txt","r")

r = int(stdin.readline()) #사진틀의 개수
n = int(stdin.readline()) #추천 개수
reco = list(map(int,stdin.readline().split()))
pic = []
pic_num = 0
def time_plus(pic):
    for i in range(0,pic_num):
        pic[i][2] += 1
for i in reco:
    flag = False #변경 여부
    if pic_num != r:
        for j in range(pic_num):
            if pic[j][0] == i:
                pic[j][1]+=1
                flag = True
                break
        if not flag:
            pic.append([i,1,0])
            pic_num+=1
    elif pic_num == r:
        #중복존재?
        for j in range(pic_num):
            if pic[j][0] == i:
                pic[j][1] += 1
                flag = True
                break
        if not flag:
            pic.sort(key=lambda x:(x[1],-x[2]))
            pic[0] = [i,1,0]
    time_plus(pic)
    # print(pic)
print(*(sorted([x[0] for x in pic])))