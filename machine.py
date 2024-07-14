from shapely.wkt import loads
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import NearestNeighbors
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import sklearn

df = pd.read_csv('GroceryStore.csv') 
df2 = pd.read_csv("database\\Business_License.csv")
df2.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
# ^ Might be an issue here, with the drop line the len of df2 is 49555, without the line its 54025
# I think theres some problems with the business data coords, idk

#breaks the grocery store into just the lat and long numbers (we need numbers to make the model)
df['points'] = df['Location'].apply(loads)
df['grocery_long'] = df['points'].apply(lambda point: point.x if point else None)
df['grocery_lat'] = df['points'].apply(lambda point: point.y if point else None)

#df2.dropna(subset=['LONGITUDE'], inplace=True)
#df2["points2"]=df2.apply(lambda col: Point(col.LONGITUDE, col.LATITUDE), axis=1)
#df['business_long'] = df['points2'].apply(lambda point: point.x if point else None)
#sf['business_lat'] = df['points2'].apply(lambda point: point.y if point else None)

df2 = df2.rename(columns={'LATITUDE': 'business_lat', 'LONGITUDE': 'business_long'})
columns_to_drop = ['Store Name','Address','Zip','New status','Last updated','Location', 'points']
df = df.drop(columns=columns_to_drop)

columns_to_drop = ['ID','LICENSE ID','ACCOUNT NUMBER','SITE NUMBER','LEGAL NAME','DOING BUSINESS AS NAME',
                   'ADDRESS','CITY','STATE','ZIP CODE','WARD','PRECINCT','WARD PRECINCT','POLICE DISTRICT','LICENSE CODE','LICENSE DESCRIPTION',
                   'BUSINESS ACTIVITY ID','BUSINESS ACTIVITY','LICENSE NUMBER','APPLICATION TYPE','APPLICATION CREATED DATE',
                   'APPLICATION REQUIREMENTS COMPLETE','PAYMENT DATE','CONDITIONAL APPROVAL','LICENSE TERM START DATE',
                   'LICENSE TERM EXPIRATION DATE','LICENSE APPROVED FOR ISSUANCE','DATE ISSUED','LICENSE STATUS',
                   'LICENSE STATUS CHANGE DATE','SSA','LOCATION']
df2 = df2.drop(columns=columns_to_drop)

#print(df2['business_long'].dtype)
# print(len(df2['business_lat']))
# print(len(df2['business_long']))

# X is predictor, Y is predicted
# tr = training, dev = developer ie. validation
Xtr = df2.sample(frac=0.8, random_state=200)
Xdev = df2.drop(Xtr.index)

Ytr = df.sample(frac=0.8, random_state=200)
Ydev = df.drop(Ytr.index)

model = NearestNeighbors() 
model.fit(Xtr, Ytr)
# this does not work, WIP ^^^
predictions = model.predict(Xdev)

print(predictions)

