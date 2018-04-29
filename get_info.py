#AIzaSyBvpSqVuVoihLyhR0P-_Gf47PGngEQ_K3M

from googleplaces import GooglePlaces, types, lang
import pandas as pd

YOUR_API_KEY = 'AIzaSyBvpSqVuVoihLyhR0P-_Gf47PGngEQ_K3M'

google_places = GooglePlaces(YOUR_API_KEY)

query_result = google_places.nearby_search(location='3460 Kentucky St. Riverside,CA',radius=500)

if query_result.has_attributions:
    print(query_result.html_attributions)
i=0
df = pd.DataFrame(columns=['name','type','geo_location'])
    
for place in query_result.places:
    #print(place.name)
    #print(place.types)
    #print(place.geo_location)
    #print(place.place_id)
    df_temp=pd.DataFrame({'name':place.name,
                          'type':place.types,
                          'geo_location':place.geo_location})
    df.append(df_temp)
    
#data = pd.read_json(query_result)

#print(data)