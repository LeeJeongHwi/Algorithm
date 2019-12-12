"""
1. MySQL에는 데이터가 다 insert 되어 있다.
Data : Bicycle_Data / Bicycle_RentalOffice_Data / SeoulData(시군구)
2. SEOUL DISTRICT.SVG 파일에는 각 구별 ID가 있다.
3. Foreign key, Primary Key 설정은 MySQL 내에서 진행함-

참고자료 : https://github.com/Kim-Taesu/seoulMap
"""
import pymysql as ps
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import re

#DB 접속
conn = ps.connect(host='localhost',
                  user='root',
                  password='rjdnf88as',
                  db='bicycle',
                  charset='utf8')
curs = conn.cursor()

#data 가져오기
def selectItem():
    sql = """
        select s.OfficeEname,s.Code,bs.useNumber from 
        (select b.rentalOffice,sum(bu.useNum) as useNumber 
        from bicycle b inner join bicycle_users bu on b.rentalNumber 
        = bu.rentalNumber group by b.rentalOffice) bs inner join seouldata s 
        on s.rentalOffice = bs.rentalOffice group by s.rentalOffice;
    """
    curs.execute(sql)
    result = curs.fetchall()
    return result

itemDf = pd.DataFrame(list(selectItem()),columns=['Country','Code','Number'])

itemDf['Number'] = itemDf['Number'].astype('int')

itemDf['index']=0
# RelPlot
# sns.relplot(x='Code',y='Number',kind='line',data=itemDf)
#HeatMap DF 재생성
tmp= itemDf.pivot("Code",'index','Number')

#HeatMap 설정
plt.figure(figsize=(12,12))
ax = sns.heatmap(tmp,cmap='RdYlGn_r',annot=True,fmt='d') #HeatMap 생성
plt.title("Using Public Bicycle of Each District - HeatMap",fontsize=10)
#HeatMap을 svg 파일로 저장
plt.savefig('../data/result/test.svg')

svgFile = open("../data/result/test.svg",'r')


#각 구역별 data 마다 color 색출
    #Code순으로 sort
itemDf.sort_values(by=['Code'],axis=0,inplace=True)


soup = BeautifulSoup(svgFile,'html.parser')
colorList = soup.select("#QuadMesh_1 > path")

colors = []
    #Code의 목록을 인덱스로 접근하게 만듬
for i,k in enumerate(list(itemDf['Country'])):
    colors.append([k,i])
i=0
    #color를 색출해서 각 "Ename"에 맞게 colors에 저장
for color in colorList:
    colors[i][1] = str(re.search(r"fill:(.+);",colorList[i]['style']).group(1))
    i+=1

    #dict로 변환
coldict = {}
for c in colors:
    if c[0] not in coldict:
        coldict[c[0]] = c[1]
print(coldict)
#Seoul Map에 Mapping 시키기
    #svg 불러오기
seouldist = open("../data/svg/Seoul_districts.svg",'rt',encoding='UTF8').read()
    #parser 설정
mapSoup = BeautifulSoup(seouldist,'html.parser')
    #path 탐색
paths = mapSoup.find_all("path")
    #path Style 구조
# path_style = 'font-size:12px;fill-rule:nonzero;stroke:#000000;stroke-opacity:1;stroke-width:1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
path_style = 'fill:'

    #Data Set 생성
sample = itemDf.set_index("Country").T.to_dict('list')

    #(이해 필요) 각 구별 색을 path 데이터에 저장
index = 0

for p in paths:
    if p['id']:
        # if p['id'] == 'Yeongdeungpo-gu_1_':
        #     col = coldict['Yeongdeungpo-gu']
        #     # print(col)
        # else:
        col = coldict[p['id']]
        # print(col)
        p['style'] = path_style + col
        # if p['id'] == "Yeongdeungpo-gu_1_":
        #     p['id'] = p["id"] + " : " + str(sample['Yeongdeungpo-gu'][0])
        # else:
        p['id'] = p["id"] + " : " + str(sample[p['id']][0])
    else:
        p['id'] = p['id'] + " : 0"
    #변경된 seoul map svg 파일 seaborn 결과 svg 파일에 추가
pathtag = mapSoup.find_all('path')

soup.find('g',{'id':'axes_1'})['style']='visibility:hidden'
gtag = mapSoup.find_all('g')

tmp = soup.svg.g
tmp.append(gtag[0])
#결과 파일 저장
output_svg = '../data/svg/seoul_district(RESULT)2.svg'
newSeoulMap = open(output_svg, "w+" , encoding='UTF8')
newSeoulMap.write(str(soup))
newSeoulMap.close()

# plt.show()
curs.close()
conn.close()
