import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('GroceryStore.csv')

locations = list(df['Location'])
#print (locations)
#print('done')

xs = []
ys = []
for point in locations:
    if isinstance(point, str):  # Check if the point is a string
        clean_point = point.replace('POINT (', '').replace(')', '')
        coordinate = clean_point.split()
        #print(coordinate)
        xs.append(float(coordinate[0]))
        ys.append(float(coordinate[1]))
    else:
        print('error: invalid point at ' + str(len(xs)))

#print(xs)
#print(ys)

plt.plot(xs, ys, 'o')
#plt.xlim(min(xs), max(xs)) 
#plt.ylim(min(ys), max(ys))
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True, which="both", ls="--")
plt.show()

