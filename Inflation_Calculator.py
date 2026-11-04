#Start off by importing the relevant libaries for the project
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#Input CSV File
df = pd.read_csv("STATIC_INFLATIONCALC.csv", skiprows=8)
print (df)


def convert (From_Cost, From_Date, To_Date):
    from_index = df.loc[df["date"] == From_Date, "STATIC_INFLATIONCALC"].values[0]
    to_index = df.loc[df["date"] == To_Date, "STATIC_INFLATIONCALC"].values[0]
    To_Cost = float(From_Cost) * (to_index / from_index)
    return To_Cost  

result = convert(*input("Enter (Cost,From Date,To Date): ").split(","))


print(f"Converted Cost: ${result:.2f}")














#result = convert(100,4,5)
#print (result)




# Data Validation Sample
'''
user_input = input('Enter a number --->')

try:
    user_input = int(user_input)
    print( 2 + user_input)
except ValueError:
    print('Invalid: you need to enter a number !')
'''