import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv("AllDataFile.csv")

features = df.drop(columns = ["Community Area Number", "COMMUNITY AREA NAME", "HARDSHIP INDEX"], axis=1)

target = df["HARDSHIP INDEX"]

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state = 4)

LinearReg = LinearRegression().fit(x_train, y_train)

predictions = LinearReg.predict(x_test)

for x in range(len(y_test)):
    print(y_test[x:x+1], predictions[x:x+1])

'''
49 #this is the index of the rows selected     51 #the correlating Hardship Index
Name: HARDSHIP INDEX, dtype: int64 [51.1445944] #the prediction
'''

print("Coefficients: ", LinearReg.coef_)
print("Accuracy Score: ", LinearReg.score(x_test, y_test))
print("MSE: ", np.mean((predictions - y_test)**2))





