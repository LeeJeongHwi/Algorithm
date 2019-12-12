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
                       names=["rentalOffice", "rentalNumber",
                              "rentalName", "rentalAdd",
                              "latitude","longitude","startDay","bicycleNum"]
                       )
    del cs['startDay'],cs["rentalName"]

    return cs
# csv Data들을 DB에 저장
def insertData():
    # cs = loadcsv(r"../data/csv/Bicycle_RentalOffice_data.csv")
    #load된 csv 파일은 DataFrame으로 저장되있는 상태
    engine = create_engine("mysql+pymysql://root:"+""+
                           "@localhost:3306/bicycle?charset=utf8",
                           encoding='utf-8')
    encon = engine.connect()
    cs.to_sql(name='bicycle',con=engine,if_exists='append',index=False)
    encon.close()



"""
create table bicycle_users(
    rentalDate int NOT NULL,
    rentalNumber int NOT NULL,
    rentalOffice varchar(255) NOT NULL,
    rentalCode varchar(20) NOT NULL,
    gender varchar(4) NOT NULL,
    ageCode varchar(20) NOT NULL,
    useNum int NOT NULL,
    movement float(10,2) NOT NULL,
    carbon float(10,2) NOT NULL,
    distance int NOT NULL,
    travelTime int NOT NULL,
    foreign key (rentalNumber) references bicycle(rentalNumber)
)
"""