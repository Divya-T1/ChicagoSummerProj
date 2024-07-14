import string
from shapely.wkt import loads
import geopandas as gp
import pandas as p
from shapely.geometry import Point
from sklearn import tree
import ReadingCoord
import matplotlib.pyplot as plt
import geodatasets
import numpy as np
from shapely import wkt
from shapely.errors import WKTReadingError
from lxml import etree
import xml.etree.ElementTree as ET

df = p.read_csv('GroceryStore.csv') 
#put an r in front of the filepath so you don't have to do double backslashes
#Ex: df2=p.read_csv(r'C:\Users\venki\VSCode\Python\ChicagoSummerProject\ChicagoSummerProj\database\Business_License.csv')
df2 = p.read_csv("database\\Business_License.csv")
#use nrows to limit number of rows

chicago = ET.parse("ChicagoMap.xml")
root = chicago.getroot()

allData=p.read_csv(r"C:\Users\venki\VSCode\Python\ChicagoSummerProject\ChicagoSummerProj\AllDataFile.csv")

census=p.read_csv(r"C:\Users\venki\VSCode\Python\ChicagoSummerProject\ChicagoSummerProj\database\Census_Data_-_Selected_socioeconomic_indicators_in_Chicago__2008___2012_20240529.csv")

x=(root[0][1].find("the_geom"))
print(type(wkt.loads(x)))

for community in root.iter("community"):
    x=(census[census["COMMUNITY AREA NAME"] == string.capwords(community.text)].index.tolist())
    if(x==[]):
        print(community.text)

'''print(census.loc[4, "COMMUNITY AREA NAME"].upper())
print(chicago.iloc[4])
print(type(census.loc[6, "COMMUNITY AREA NAME"]))
value=chicago[chicago["COMMUNITY"] == census.loc[8, "COMMUNITY AREA NAME"].upper()].index.tolist() #use .loc directly for any content value, but use .apply(loads) and then .loc[] for points
'''

df['points'] = df['Location'].apply(loads)
df2["points2"]=df2.apply(lambda col: Point(col.LONGITUDE, col.LATITUDE), axis=1)
#print(wkt.loads(chicago.loc[8, "the_geom"]))
'''try:
    for x in range(len(chicago["the_geom"])):
        wkt.loads(chicago.loc[x, "the_geom"])

except WKTReadingError as e:
    print(x)'''


listVal = []
for x in range(len(census["COMMUNITY AREA NAME"])):
    listVal.append(0)


for community in root.iter("community"):
    index=(census[census["COMMUNITY AREA NAME"] == string.capwords(community.text)].index.tolist())
    geom=root[0][index[0]].find("the_geom").text
    count=0
    if(index==[]):
        listVal.append(0)
    else:
        for y in range(len(df2["points2"])):
            if(wkt.loads(geom).contains(df2.loc[y, "points2"])):
                count+=1
        listVal[index[0]]=count
    print(count)

allData["Business Count"]=listVal
allData.to_csv(r"C:\Users\venki\VSCode\Python\ChicagoSummerProject\ChicagoSummerProj\AllDataFile.csv", index=False)






