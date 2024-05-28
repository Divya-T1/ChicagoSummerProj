import pandas as p
#80 and 217
#Long=x Lat=y
#Hi
print("Yay")
class Map:
    def __init__(self):
        global x_list
        global y_list
        x_list=[]
        y_list=[]
        self.points()
    def points(self):
        index=0
        read=p.read_csv("GroceryStore.csv", header=0, usecols=["Location"])
        for x in range(len(read)):
            row=str(read.loc[x])
            if("(" in row != False):
                x_list.append(row[row.index("(")+1:row.index(" ",25)])
            else:
                print(x)
        for y in range(len(read)):
            row=str(read.loc[y])
            if("(" in row != False):
                y_list.append(row[row.index(" ",25)+1:row.index(")")])
        
Map()




