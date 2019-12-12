import pymysql as ps
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#DB 접속
conn = ps.connect(host='localhost',
                  user='root',
                  password='',
                  db='bicycle',
                  charset='utf8')
curs = conn.cursor()

#SQL select 문 실행
def selectItem():
    sql = """
        select rentalDate,useNum from bicycle_users
    """
    curs.execute(sql)
    result = curs.fetchall()
    return result

#select 문으로 얻어낸 데이터를 df 로 만들기
def getDataFrame(result):
    df = pd.DataFrame(result,columns=['rentalDate','useNum'])
    df2 = df.groupby(['rentalDate'],as_index=False).mean()
    print(df2)
    return df2

#getDataFrame으로 얻어낸 dataFrame을 relplot형태로 시각화
def visualization(df):
    header_list= list(df.columns.values)
    print(header_list)
    sns.relplot(x=header_list[0],y=header_list[1], kind='line',data=df)
    plt.show()

if __name__ == '__main__':
    visualization(getDataFrame(selectItem()))

    curs.close()
    conn.close()