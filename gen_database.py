import pandas as pd
import json
import requests
from time import sleep
import numpy as np
import math

GOOGLE_API_KEY = 'AIzaSyBvpSqVuVoihLyhR0P-_Gf47PGngEQ_K3M'
R = 3961

# This will be the proposed business address
addr = 'Riverside, CA'

# We need to convert address to latitudes and longitudes
# So will we call the google geocoding API
geo_url = 'https://maps.googleapis.com/maps/api/geocode/json'
geo_params = {'sensor': 'false', 'address': addr}
r = requests.get(geo_url, params=geo_params)
results = r.json()['results']
location = results[0]['geometry']['location']
lat = location['lat']
lng = location['lng']

# We will now pass those latitudes and longitudes to goole places API
pg1_r = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(lat)+','+str(lng)+'&rankby=distance&type=restaurant&keyword=indian&hasNextPage=true&nextPage()=true&key='+str(GOOGLE_API_KEY))

r = pg1_r.json()['results']

f=open("loc_data.csv","w")

type1 = 'gym'

for i in range(len(r)):
    name = r[i]['name']
    #types = r[i]['types']
    #type_list = ','.join(types)
    lat = r[i]['geometry']['location']['lat']
    lng = r[i]['geometry']['location']['lng']
    #f.write("%s," % name)
    lat_r,lng_r = map(math.radians,[lat,lng])
    sleep(1)
    pg2_r = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(lat)+','+str(lng)+'&type='+type1+'&rankby=distance&hasNextPage=true&nextPage()=true&key='+str(GOOGLE_API_KEY))
    r2 = pg2_r.json()['results']
    for j in range(len(r2)):
        #types = r2[j]['types']
        #name1 = r2[j]['name']
        lat1 = r2[j]['geometry']['location']['lat']
        lng1 = r2[j]['geometry']['location']['lng']
        lat1,lng1 = map(math.radians,[lat1,lng1])
        dlat = lat_r-lat1
        dlng = lng_r-lng1
        a = (np.sin(dlat/2))**2+np.cos(lat_r)*np.cos(lat1)*(np.sin(dlng/2))**2
        c = 2*math.atan2(np.sqrt(a),np.sqrt(1-a))
        d = R*c
        #print(d)
        f.write("%s," % d)
        
    f.write("\n")    
    
f.close()
# Google Places API returns only 20 results at a time
# So if we want more results, we need to extract the next-page-token from results and
# pass it again as a new query
#pg2_token = pg1_r.json()['next_page_token']

# Storing results in a dataframe
#df1 = pd.DataFrame(pg1_r.json()['results'])

## If you send another request immediately, Google will not return anything
## You will get INVALID REQUEST ERROR
## So wait for one second

#sleep(1)

# Here we will pass the next_page_token. Notice last param in the request
#pg2_r = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(lat)+','+str(lng)+'&radius=1500&hasNextPage=true&nextPage()=true&key='+str(GOOGLE_API_KEY)+'&pagetoken='+str(pg2_token))

# Store results of this query in a different dataframe
#df2 = pd.DataFrame(pg2_r.json()['results'])


