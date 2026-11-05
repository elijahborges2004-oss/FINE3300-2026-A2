#Start off by importing the relevant libaries for the project
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#Input CSV File
df = pd.read_csv("STATIC_INFLATIONCALC.csv", skiprows=8)
print (df)

def convert (From_Cost, From_Date, To_Date):
    try:
        cost_float = float(From_Cost)
    except ValueError:
        print("Invalid: you need to enter a number for the cost!")
        return None


    # Data Validation for the From_Date
    if From_Date not in df["date"].values:
        return None
    
    # Data Validation for the To_Date
    if To_Date not in df["date"].values:
            return None

    # Indexs the file Static_Infalationcalc.csv dates to return the related CPI value. 
    from_index = df.loc[df["date"] == From_Date, "STATIC_INFLATIONCALC"].values[0]
    to_index = df.loc[df["date"] == To_Date, "STATIC_INFLATIONCALC"].values[0]
    # Calculate the cost conversion 
    To_Cost = float(From_Cost) * (to_index / from_index)
    return To_Cost
    


print ("Enter in the Price of goods in the Starting date, the From Date, and the to Date to calculate the new cost")
print ("Dates must be in YYYY-MM-DD (Ex. 2000-04-01) format with 01 being the only day available")

result = convert(*input("Enter (Cost,From Date,To Date): ").split(","))

if result is not None:
     print(f"Converted Cost: ${result:.2f}")

else:
     print ("Please restart and try again with valid entries.")
     print ("Valid Entries are between 1914-01-01, and 2026-09-01 for dates and only integer/floats for cost please restart and try again")
















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