import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine,text
import pymysql
pymysql.install_as_MySQLdb()
engine = create_engine('mysql+mysqldb://YJS2022:YJS2022YJS@47.111.6.160:3306/mod_t20')
sql="select dateYM,Tem_Mean from a06 where lon=1 and lat=1 "
df= pd.read_sql(text(sql), engine.connect())
df['dateYM']=pd.to_datetime(df['dateYM'])
plt.figure(figsize=(10,6))
plt.xlabel('dateYM')
plt.ylabel('Q_average')
plt.title('CHART2')
quarter=list(set(df['dateYM'].dt.quarter))
for i in quarter:
    years = list(set(df['dateYM'].dt.year))
    average = []
    for year in years:
        average.append(df.loc[df['dateYM'].dt.year==year].loc[df['dateYM'].dt.quarter == i]['Tem_Mean'].mean())
    plt.plot(years, average, marker='o', markersize=6,label='Quarter'+str(i))
plt.xticks(years,rotation = 30)
plt.legend(loc='upper right')
plt.show()