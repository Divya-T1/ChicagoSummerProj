from shapely.wkt import loads
import geopandas as gp
import pandas as p
from shapely.geometry import Point
import ReadingCoord
import matplotlib.pyplot as plt
import geodatasets

df = p.read_csv('GroceryStore.csv') 
#put an r in front of the filepath so you don't have to do double backslashes
#Ex: df2=p.read_csv(r'C:\Users\venki\VSCode\Python\ChicagoSummerProject\ChicagoSummerProj\database\Business_License.csv')
df2 = p.read_csv(r"C:\Users\venki\VSCode\Python\ChicagoSummerProject\ChicagoSummerProj")
#use nrows to limit number of rows

#chicago=p.read_csv("ChicagoMap.csv", usecols=["the_geom", "COMMUNITY"], nrows=1)

sample=p.read_csv(r"database\Business_License.csv", nrows=15)


#points=df.apply(point, axis=1)
#hello
df['points'] = df['Location'].apply(loads)
df2["points2"]=df2.apply(lambda col: Point(col.LONGITUDE, col.LATITUDE), axis=1)
#axis=0 allows us to iterate by each row, but axis=1 allows us to iterate by each column (so decides whether to treat given x and y as seperate rows or cols, and since we want them seen as 2 columns, axis=1)


#Code below counts the number of businesses in each area

count=0
'''for x in range(len(df2["points2"])):
    chi=chicago["the_geom"].apply(loads)
    print(type(chi.loc[0]))
    if(chi.loc[0].contains(df2.loc[x, "points2"])):
        count+=1
print(count)
'''

mapPoints=gp.GeoDataFrame(df, geometry="points")
mapPoints2=gp.GeoDataFrame(df2, geometry="points2")

shapefile=r"geo_export_2de1f329-0bd0-4922-a95b-6cc4d6a6d59e.shp"

base=gp.read_file(shapefile)
#sampleBase=base["the_geom"]


fig, ax = plt.subplots(figsize=(10, 10))
base.plot(ax=ax, color='grey')

mapPoints.crs={'init' : 'epsg:4326'}
#print(mapPoints.head())

mapPoints2.crs={'init' : 'epsg:4326'}
#print(mapPoints.head())
mapPoints2.plot(ax=ax, color="RED", markersize=1)
mapPoints.plot(ax=ax, color="Blue", markersize=10)

plt.show()