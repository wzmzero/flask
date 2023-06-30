import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine,text

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/txt')
#engine = create_engine('mysql+pymysql://用户名:密码@localhost:3306/数据库')

sql="select * from wlg2"
data= pd.read_sql_query(text(sql), engine.connect())


year=data['年度']
months=[]
average=[]
y=[]
for i in range(data.shape[0]):
    for k in range(1,data.shape[1]):
        months.append(str(year[i]) + '-' + str(k))
        y.append(data.iloc[i,k])
    average.append(data.iloc[i,1:].mean())
##月
plt.figure(figsize=(10,6))
plt.xlabel('Year')
plt.ylabel('CO2')
plt.title('CHART')
plt.xticks(np.arange(0, len(months), step=12),rotation = 30)
plt.plot(months, y,marker='o',markersize=4)
plt.show()

##年平均
plt.figure(figsize=(12,6))
plt.xticks(year)
plt.xlabel('Year')
plt.ylabel('CO2-average')
plt.plot(year, average,marker='o',markersize=4)
plt.show()