from shapely.wkt import loads
import geopandas as gp
import pandas as p
from shapely.geometry import Point
import ReadingCoord
import matplotlib.pyplot as plt

df = p.read_csv('GroceryStore.csv') 
df2= p.read_csv("C:\\Users\\venki\\VSCode\\Python\\ChicagoSummerProject\\ChicagoSummerProj\\database\\Business_License.csv")

#points=df.apply(point, axis=1)
#hello
df['points'] = df['Location'].apply(loads)
df2["points2"]=df2.apply(lambda col: Point(col.LONGITUDE, col.LATITUDE), axis=1)
#axis=0 allows us to iterate by each row, but axis=1 allows us to iterate by each column (so decides whether to treat given x and y as seperate rows or cols, and since we want them seen as 2 columns, axis=1)


mapPoints=gp.GeoDataFrame(df, geometry="points")
mapPoints2=gp.GeoDataFrame(df2, geometry="points2")

shapefile="C:\\Users\\venki\\VSCode\\Python\\ChicagoSummerProject\\ChicagoSummerProj"

base=gp.read_file(shapefile)

fig, ax = plt.subplots(figsize=(10, 10))
base.plot(ax=ax, color='grey')

mapPoints.crs={'init' : 'epsg:4326'}
#print(mapPoints.head())

mapPoints2.crs={'init' : 'epsg:4326'}
#print(mapPoints.head())
mapPoints2.plot(ax=ax, color="RED", markersize=3)
mapPoints.plot(ax=ax, color="Blue", markersize=3)

plt.show()