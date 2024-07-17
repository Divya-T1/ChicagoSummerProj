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

housing = p.read_csv(r"database\Affordable_Rental_Housing_Developments_20240529.csv")

hospitals = p.read_csv(r"database\Public_Health_Services-_Chicago_Primary_Care_Community_Health_Centers.csv")

schools=p.read_csv(r"database\CPS_School_Locations_SY1415_20240717.csv")

chicago = ET.parse("ChicagoMap.xml")
root = chicago.getroot()

allData=p.read_csv(r"AllDataFile.csv")

census=p.read_csv(r"database\Census_Data_-_Selected_socioeconomic_indicators_in_Chicago__2008___2012_20240529.csv")

crime=p.read_csv(r"database\Crime.csv")

x=(root[0][1].find("the_geom"))
print(type(wkt.loads(x)))

'''for community in root.iter("community"):
    x=(census[census["COMMUNITY AREA NAME"] == string.capwords(community.text)].index.tolist())
    if(x==[]):
        print(community.text)'''

'''print(census.loc[4, "COMMUNITY AREA NAME"].upper())
print(chicago.iloc[4])
print(type(census.loc[6, "COMMUNITY AREA NAME"]))
value=chicago[chicago["COMMUNITY"] == census.loc[8, "COMMUNITY AREA NAME"].upper()].index.tolist() #use .loc directly for any content value, but use .apply(loads) and then .loc[] for points
'''

df['points'] = df['Location'].apply(loads)
df2["points2"] = df2.apply(lambda col: Point(col.LONGITUDE, col.LATITUDE), axis=1)
housing["points"] = housing.apply(lambda col: Point(col.Longitude, col.Latitude), axis=1)
schools["points"] = schools["the_geom"].apply(loads)
crime["points"] = crime.apply(lambda col: Point(col.LONGITUDE, col.LATITUDE), axis=1)
#print(wkt.loads(chicago.loc[8, "the_geom"]))
'''try:
    for x in range(len(chicago["the_geom"])):
        wkt.loads(chicago.loc[x, "the_geom"])

except WKTReadingError as e:
    print(x)'''

listVal = []
for x in range(len(census["COMMUNITY AREA NAME"])):
    listVal.append(0)

listCE = []
for x in range(len(census["COMMUNITY AREA NAME"])):
    listCE.append(0)

listCH = []
for x in range(len(census["COMMUNITY AREA NAME"])):
    listCH.append(0)

listDE = []
for x in range(len(census["COMMUNITY AREA NAME"])):
    listDE.append(0)

listDH = []
for x in range(len(census["COMMUNITY AREA NAME"])):
    listDH.append(0)

listOE = []
for x in range(len(census["COMMUNITY AREA NAME"])):
    listOE.append(0)

listOH = []
for x in range(len(census["COMMUNITY AREA NAME"])):
    listOH.append(0)

#Businesses

'''for community in root.iter("community"):
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

allData["Business Count"]=listVal'''
#allData.to_csv(r"C:\Users\venki\VSCode\Python\ChicagoSummerProject\ChicagoSummerProj\AllDataFile.csv", index=False)




#Housing

'''for community in root.iter("community"):
    index=(census[census["COMMUNITY AREA NAME"] == string.capwords(community.text)].index.tolist())
    geom=root[0][index[0]].find("the_geom").text
    count=0
    countU=0
    if(index==[]):
        listVal.append(0)
    else:
        for y in range(len(housing["points"])):
            if(wkt.loads(geom).contains(housing.loc[y, "points"])):
                count+=1
                try:
                    countU+=int(housing.loc[y,"Units"])
                except:
                    print(y)
        listVal[index[0]]=count
        listVal2[index[0]]=countU
    print(count, countU)

allData["Housing Count"]=listVal
allData["Housing Count Units"]=listVal2'''
#allData.to_csv(r"C:\Users\venki\VSCode\Python\ChicagoSummerProject\ChicagoSummerProj\AllDataFile.csv", index=False)


#Hospitals

'''pointsHos=hospitals["Address"]
lats=[]
longs=[]

for x in range(len(pointsHos)):
    add=hospitals.loc[x, "Address"]
    lat=add[add.index("(")+1 : add.index(",", add.index("("))]
    lats.append(float(lat))

    long=add[add.index(" ", add.index("("))+1 : add.index(")")]
    longs.append(float(long))

hospitals["lat"]=lats
hospitals["long"]=longs

hospitals["points"]=hospitals.apply(lambda col: Point(col.long, col.lat), axis=1)

for community in root.iter("community"):
    index=(census[census["COMMUNITY AREA NAME"] == string.capwords(community.text)].index.tolist())
    geom=root[0][index[0]].find("the_geom").text
    count=0
    if(index==[]):
        listVal.append(0)
    else:
        for y in range(len(hospitals["points"])):
            if(wkt.loads(geom).contains(hospitals.loc[y, "points"])):
                count+=1
        listVal[index[0]]=count
    print(count)

allData["Hospital Count"]=listVal'''
#allData.to_csv(r"C:\Users\venki\VSCode\Python\ChicagoSummerProject\ChicagoSummerProj\AllDataFile.csv", index=False)


#Schools
'''print(schools.loc[1, "SCH_TYPE"]=="Charter")
for community in root.iter("community"):
    index=(census[census["COMMUNITY AREA NAME"] == string.capwords(community.text)].index.tolist())
    geom=root[0][index[0]].find("the_geom").text
    chartE=0
    chartH=0
    distE=0
    distH=0
    otherE=0
    otherH=0
    for y in range(len(schools["points"])):
        if(wkt.loads(geom).contains(schools.loc[y, "points"])):
            if(schools.loc[y, "SCH_TYPE"]=="Charter"):
                if(schools.loc[y, "GRADE_CAT"]=="ES"):
                    chartE+=1
                else:
                    chartH+=1

            elif(schools.loc[y, "SCH_TYPE"]=="District"):
                if(schools.loc[y, "GRADE_CAT"]=="ES"):
                    distE+=1
                else:
                    distH+=1
            else:
                if(schools.loc[y, "GRADE_CAT"]=="ES"):
                    otherE+=1
                else:
                    otherH+=1
    listCE[index[0]]=chartE
    listCH[index[0]]=chartH
    listDE[index[0]]=distE
    listDH[index[0]]=distH
    listOE[index[0]]=otherE
    listOH[index[0]]=otherH

allData["Charter School Elementary Count"]=listCE
allData["Charter School High School Count"]=listCH
allData["District School Elementary Count"]=listDE
allData["District School High School Count"]=listDH
allData["ALOP/Safe School Elementary Count"]=listOE
allData["ALOP/Safe School High School Count"]=listOH'''
#allData.to_csv(r"AllDataFile.csv", index=False)

#Crime

for community in root.iter("community"):
    index=(census[census["COMMUNITY AREA NAME"] == string.capwords(community.text)].index.tolist())
    geom=root[0][index[0]].find("the_geom").text
    count=0
    if(index==[]):
        listVal.append(0)
    else:
        for y in range(len(crime["points"])):
            if(wkt.loads(geom).contains(crime.loc[y, "points"])):
                count+=1
        listVal[index[0]]=count
    print(count)

allData["Crime Count"]=listVal
allData.to_csv(r"AllDataFile.csv", index=False)



