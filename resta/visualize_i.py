import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt

R = 3961

def clean_data(db_name):
    db = pd.read_csv(db_name)
    #data = pd.read_csv('loc_data.csv',error_bad_lines=False)
    new_index = np.arange(0,21,1)
    #new_index = np.arange(0,18,1)
    db.columns = new_index
    db = db.drop(columns=20)
    db = db.drop(columns=0)
    #data = data.drop(columns=[12,14,15,16,17])
    df = db.mean(axis=1)
    return df
    #data = data.dropna()
    
def clean_rv(db_name):
    #db = pd.read_csv(db_name)
    db = pd.read_csv(db_name,error_bad_lines=False)
    new_index = np.arange(0,18,1)
    #new_index = np.arange(0,18,1)
    db.columns = new_index
    #db = db.drop(columns=20)
    db = db.drop(columns=0)
    db = db.drop(columns=[12,14,15,16,17])
    df = db.mean(axis=1)
    return df
    #data = data.dropna()


i_SF = clean_data('loc_data_SF.csv')
i_SD = clean_data('loc_data_SD.csv')
i_LA = clean_data('loc_data_LA.csv')
i_HOU = clean_data('loc_data_HOU.csv')
i_AUS = clean_data('loc_data_AUS.csv')
i_DAL = clean_data('loc_data_DAL.csv')
i_RV = clean_data('loc_data_RV.csv')

#data = data.drop_duplicates(subset=0)
sns.set(style="white",palette="muted",color_codes=True)
sns.distplot(i_SF,bins=20,label='SF')
sns.distplot(i_SD,bins=20,label='SD')
sns.distplot(i_LA,bins=20,label='LA')
sns.distplot(i_HOU,bins=20,label='HOU')
sns.distplot(i_DAL,bins=20,label='DAL')
sns.distplot(i_AUS,bins=20,label='AUS')
sns.distplot(i_RV,bins=20,label='RV')
plt.xlim([0,1])
plt.ylim([0,20])
plt.legend()
plt.xlabel('Distance (miles)')
plt.ylabel('Distribution')
plt.title('Proximity to other Restaurants')
#plt.savefig('resta.png',dpi=600)
plt.show()
#sns.distplot(i_RV,bins=20)
#f,axes = plt.subplots(4,4,sharex='col',sharey='row')
#sns.despine(left=True)

#d = np.empty((25,25))
#d = np.empty((16,20))
#k=0
#i=3
#m=-1
#n=-1
#for i in range(15):
#    k=0
#    for j in range(3,41,2):
#        lat1 = data.iloc[i][1]
#        lng1 = data.iloc[i][2]
#        lat1,lng1 = map(math.radians,[lat1,lng1])
#        lat2,lng2 = map(math.radians,[data.iloc[i][j],data.iloc[i][j+1]])
#        dlat = lat1-lat2
#        dlng = lng1-lng2
#        a = (np.sin(dlat/2))**2+np.cos(lat1)*np.cos(lat2)*(np.sin(dlng/2))**2
#        c = 2*math.atan2(np.sqrt(a),np.sqrt(1-a))
        #d[i][k] = R*c
        #k = k+
        #print(k)
#        d[i,k]=R*c
#        k=k+1
        
#i=0;
#for m in range(4):
#    for n in range(4):
#        sns.distplot(d[i,:],bins=20,ax=axes[m,n])
        #sns.distplot(d[i,:],bins=30)
        #axes[m,n].set_xlim([0,25])
#        i=i+1


