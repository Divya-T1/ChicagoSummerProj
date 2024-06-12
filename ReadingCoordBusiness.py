import pandas as p
#80 and 217
#Long=x Lat=y
#Hi
class Map:
    def __init__(self):
        global x_list
        global y_list
        x_list=[]
        y_list=[]
        self.points()
    def points(self):
        index=0
        read=p.read_csv("C:\\Users\\venki\\VSCode\\Python\\ChicagoSummerProject\\ChicagoSummerProj\\database\\Business_License.csv", header=0, usecols=["LOCATION"])
        for y in range(len(read)):
            row=str(read.loc[y])
            if("(" in row != False):
                y_list.append(row[row.index("(")+1:row.index(" ",row.index("("))])
            else:
                print(y)
        for x in range(len(read)):
            row=str(read.loc[x])
            if("(" in row != False):
                x_list.append(row[row.index(" ",row.index("("))+1:row.index(")")])
        
Map()




