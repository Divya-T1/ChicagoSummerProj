from shapely.wkt import loads
import geopandas as gp
import pandas as p
from shapely.geometry import Point
import ReadingCoord
import matplotlib.pyplot as plt

df = p.read_csv('GroceryStore.csv') 

#points=df.apply(point, axis=1)
df['points'] = df['Location'].apply(loads)

mapPoints=gp.GeoDataFrame(df, geometry="points")

mapPoints.crs={'init' : 'epsg:4326'}
#print(mapPoints.head())
mapPoints.plot()
plt.show()

