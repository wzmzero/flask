import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import VARCHAR, Float, Integer, Date, Numeric
import pymysql
pymysql.install_as_MySQLdb()
engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/db_test')
df = pd.read_table('./vapr_12z-mly.txt',sep='\s+',names=['ID','DATEYM','DATE','LEVEL','VALUE','NUM'])
df['DATEYM'] = df['DATEYM'].map(str)+"-"+df['DATE'].map(str)+'-1'
df.drop(labels='DATE',axis=1,inplace=True)
df.to_sql('tb_test',con = engine,if_exists='replace',index=False,
                      dtype={'ID':VARCHAR(11),'DATEYM':Date,'LEVEL':Integer,'VALUE':Float,'NUM':Numeric})

