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
        print("****Invalid: you need to enter a number for the cost!****")
        return None

    dates_np = df["date"].to_numpy()
    cpi_np = df["STATIC_INFLATIONCALC"].to_numpy()

    if From_Date not in dates_np:
        return None
    
    if To_Date not in dates_np:
            return None
    
    from_index = cpi_np[np.where(dates_np == From_Date)[0][0]]
    to_index = cpi_np[np.where(dates_np == To_Date)[0][0]]

    To_Cost = float(From_Cost) * (to_index / from_index)

    pct_change = ((to_index - from_index) / from_index) * 100

    return To_Cost, pct_change, from_index, to_index


print ("Enter in the Price of goods in the Starting date, the From Date, and the to Date to calculate the new cost")
print ("Dates must be in YYYY-MM-DD (Ex. 2000-04-01) format with 01 being the only day available")

result = convert(*input("Enter (Cost,From Date,To Date): ").split(","))

if result is not None:
     To_Cost, pct_change, from_index, to_index = result
     print(f"Converted Cost: ${To_Cost:.2f}")
     print(f"Percent change: {pct_change:.2f}%")
     print(f"CPI for first period: {from_index:.1f}")
     print(f"CPI for second period: {to_index:.1f}")

else:
     print ("Please restart and try again with valid entries.")
     print ("For Dates Valid Entries are between 1914-01-01, and 2026-09-01")
     print ("For Cost Values only integer/floats for cost please restart and try again")
















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