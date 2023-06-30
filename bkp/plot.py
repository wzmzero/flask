import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_table('.\WLG.txt',sep='\s+')
months = pd.date_range('2000-01', '2021-01', freq='BM')
y = data.iloc[:,2]
plt.figure(figsize=(10,6))
plt.xlabel('Year')
plt.ylabel('CO2')
plt.title('CHART')
average=[]
year=[]
for i in list(set(data['年度'])):
    average.append(data.loc[data['年度']==i]['CO2'].mean())
    year.append(i)
plt.plot(months, y,marker='o',markersize=4)
plt.show()
plt.figure(figsize=(12,6))
plt.xticks(year)
plt.xlabel('Year')
plt.ylabel('CO2-average')
plt.plot(year, average,marker='o',markersize=4)
plt.show()