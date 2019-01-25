# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:53:32 2019

@author: kdandebo
"""
#Importing libraries
import matplotlib.pyplot as plt
import pandas as pd

#importing the data file
xl = pd.ExcelFile("C:/Users/kdandebo/Desktop/Models/Python excercise/Data3.xlsx")
#Parsing the data
df=xl.parse("Data")

#checking the info of the date file
print(df.columns)
df.info()
    
#information of the scatter plot
plt.xlabel('Country Name')
plt.ylabel('Percapita Income(in millions)')
plt.title('GDP per capita income of Argentina')

x = df[df['Country Name']=="Argentina"]
plt.scatter(x['Country Name'],x['Value'], marker='x', color='red')
plt.show()
#print(df.head(5))
