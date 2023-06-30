import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine,text
import numpy as np
import pymysql

class plot():
    pymysql.install_as_MySQLdb()
    engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/db_test')
    sql="select * from tb_qt"
    df= pd.read_sql(text(sql), engine.connect())
    df['DATEYM']=pd.to_datetime(df['DATEYM'])
    plt.figure(figsize=(20,10))
    plt.xlabel('DATEYM')
    plt.ylabel('VALUE')
    plt.title('CHART1')
    years=list(set(df['DATEYM'].dt.year))
    average=[]
    for year in years:
        average.append(df.loc[df['DATEYM'].dt.year == year]['VALUE'].mean())
    plt.plot(years, average,marker='o',markersize=5,label="year-avg")
    plt.legend(loc='upper right')
    plt.show()

# if __name__ == '__main__':
#     plot()