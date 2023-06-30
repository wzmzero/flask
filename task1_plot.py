import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine,text
import numpy as np
import pymysql
from datetime import datetime
pymysql.install_as_MySQLdb()
engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/db_test')
sql="select * from tb_test where id='PFM00059981' and DATEYM LIKE '%'"
df= pd.read_sql(text(sql), engine.connect())
df['DATEYM']=pd.to_datetime(df['DATEYM'])
years=[]
plt.figure(figsize=(20,10))
plt.xlabel('DATEYM')
plt.ylabel('VALUE')
plt.title('CHART1')
for i in list(set(df['LEVEL'])):
    years=list(set(df.loc[df['LEVEL']==i]['DATEYM'].dt.year))
    average=[]
    for year in years:
        average.append(df.loc[df['DATEYM'].dt.year == year].loc[df['LEVEL']==i]['VALUE'].mean())
    plt.plot(years, average,marker='o',markersize=5,label=str(i))
plt.legend(loc='upper right')
plt.show()