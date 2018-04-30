import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def return_race(csvname):
    race1 = pd.read_csv(csvname)
    foo1 = lambda x: pd.Series([i for i in reversed(x.split(','))])
    rev1 = race1['GEO.display-label'].apply(foo1)
    rev1.rename(columns={0:'State',1:'County'},inplace=True)
    rev1 = rev1[['State','County']]
    race1 ['State'] = rev1.State
    race1 ['County'] = rev1.County
    temp1 = race1.loc[race1['Hisp.id'] == 'tothisp']
    temp1 = temp1.loc[temp1['Sex.id']=='totsex']
    temp1 = temp1.loc[temp1['Year.id']=='est72016']
    CA = pd.DataFrame()
    CA['county']=temp1['County']
    CA['totpop']=temp1['totpop']
    CA['asian']=temp1['aa']
    return CA

def return_asian_pop(CA,county_name):
    TOT = CA.totpop[CA['county']==county_name]
    AA = CA.asian[CA['county']==county_name]
    return (AA/TOT*100)

CA = return_race('CA-race.csv')
#TX = return_race('TX-race.csv')

#income = pd.read_csv('Income-US-counties.csv')
#foo1 = lambda x: pd.Series([i for i in reversed(x.split(','))])
#rev1 = income['Area_name'].apply(foo1)
#rev1.rename(columns={0:'State',1:'County'},inplace=True)
#rev1 = rev1[['State','County']]
#income['State'] = rev1.State
#income['County'] = rev1.County
CA['percent']=CA['asian']/CA['totpop']*100
CA = CA.set_index('county')
CA = CA.sort_values(by='percent')
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.barh(np.linspace(0,57,58),CA['percent'],tick_label=CA.index)
ax2 = plt.axes()
ax2.set_xlabel('Percentage of Asians')
plt.savefig('diversity.png')

income = pd.read_csv('Income-US-counties.csv')
income_CA = income[income['State']=='CA']
final = pd.DataFrame()
final['name'] = income_CA['Area_name']
final['income'] = income_CA['Median_Household_Income_2016']
final = final.set_index('name')
final['income'] = final['income'].str.replace(',', '')
final = final.astype(int)
final = final.sort_values(by='income')
final = final.drop('California')
plt.barh(np.linspace(0,57,58),final['income'],tick_label=final.index)
ax2.set_xlabel('Median Income in $')
plt.savefig('income.png')
#print(return_asian_pop(CA,'Riverside County'))
#print(return_asian_pop(CA,'Los Angeles County'))

#BR = pd.read_csv('BR-business.csv')
#counts = BR['NAICS Code'].value_counts().tolist()
#values = BR['NAICS Code'].value_counts().keys().tolist()
#values = [int(i) for i in values]
#data1 = pd.DataFrame(values,columns=['code'])
#data1['value']=pd.DataFrame(counts)
#temp = data1[:20]
#temp = temp.set_index('code')
#temp.plot(kind='bar')

#LA = pd.read_csv('LA-business.csv')
#counts = LA['NAICS'].value_counts().tolist()
#values = LA['NAICS'].value_counts().keys().tolist()
#values = [int(i) for i in values]
#data2 = pd.DataFrame(values,columns=['code'])
#data2['value']=pd.DataFrame(counts)
#temp = data2[:20]
#temp = temp.set_index('code')
#temp.plot(kind='bar')