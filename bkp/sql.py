import pymysql
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine,text
import numpy as np
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/txt')
#engine = create_engine('mysql+pymysql://用户名:密码@localhost:3306/数据库')


sql="select * from wlg"
data= pd.read_sql_query(text(sql), engine.connect())
print(data)
y = data.iloc[:,3]
average=[]
year=[]
months = []
for i in list(set(data['年度'])):
    average.append(data.loc[data['年度']==i]['CO2'].mean())
    year.append(i)
    for k in list(set(data['月'])):
        months.append(str(i) + '-' + str(k))
plt.figure(figsize=(10,6))
plt.xlabel('Year')
plt.ylabel('CO2')
plt.title('CHART')
plt.xticks(np.arange(0, len(months), step=12),rotation = 30)
plt.plot(months, y,marker='o',markersize=4)
plt.show()

plt.figure(figsize=(12,6))
plt.xticks(year)
plt.xlabel('Year')
plt.ylabel('CO2-average')
plt.plot(year, average,marker='o',markersize=4)
plt.show()