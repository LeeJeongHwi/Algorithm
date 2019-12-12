import pymysql as ps
import pandas as pd
from sqlalchemy import create_engine

#DB 접속
conn = ps.connect(host='localhost',
                  user='root',
                  password='',
                  db='bicycle',
                  charset='utf8')
curs = conn.cursor()
#CSV 파일 로드, 안 쓸 columns 삭제
def loadcsv(fileName):
    cs = pd.read_csv(fileName,header=None, skiprows=1,
                       names=["Number",'Code',"rentalOffice","OfficeEname",
                              "esripk",'latitude','longitude']
                       )
    del cs['esripk']

    return cs
# csv Data들을 DB에 저장
def insertData():
    cs = loadcsv(r"../data/csv/seouldata.csv")
    print(cs.head())
    #load된 csv 파일은 DataFrame으로 저장되있는 상태
    engine = create_engine("mysql+pymysql://root:"+""+
                           "@localhost:3306/bicycle?charset=utf8",
                           encoding='utf-8')
    encon = engine.connect()
    cs.to_sql(name='seoulData',con=engine,if_exists='append',index=False)
    encon.close()

insertData()