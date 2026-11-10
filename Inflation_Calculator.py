# Start off by importing the relevant libaries for the project
import pandas as pd
import numpy as np
from datetime import datetime

# reads CSV File using pandas and assigns it to a data frame variable along with skipping into the data rows
df = pd.read_csv("STATIC_INFLATIONCALC.csv", skiprows=8)

# Creation of the conversion function which defines that user inputs needed for calculation
def convert (From_Cost, From_Date, To_Date):
    # Checks if the From_Cost inputted by user is a float
    try:
        cost_float = float(From_Cost)

    # Returns an Error if it is not a float
    except ValueError:
        # Tells user the correct input method
        print("****Invalid: you need to enter a number for the cost!****")
        # Ensures the function is terminated and assigns the return value to None If it fails the float test
        return None
   
    # Goes into the data frame and converts the "date" column to a numpy array
    dates_np = df["date"].to_numpy()
    # Goes into the data frame and converts "STATIC_INFLATIONCALC" column into an array
    cpi_np = df["STATIC_INFLATIONCALC"].to_numpy()

    # Checks if the user input "From_Date" within date range contained in the date column from data
    if From_Date not in dates_np:
        return None
    # Checks if the user input "To_Date" is within date range contained in the date column from data
    if To_Date not in dates_np:
            return None

    # Assigns a row number to a matching date by the user for the "From_Date" input
    from_pos = np.where(dates_np == From_Date)[0][0]   
    # Assigns a row number to a matching date by the user for the "To_Date" input
    to_pos = np.where(dates_np == To_Date)[0][0]

    # Gets the cpi value at the user's inputted From_Date using established variables
    from_cpi = cpi_np[from_pos]
    # Converts the From_Cpi's date into a string 
    from_cpi_string = datetime.strptime(From_Date, "%Y-%m-%d").strftime("%B %Y")
    # Gets the cpi value at the user's inputted To_Date using established variables
    to_cpi = cpi_np[to_pos]
    # Converts the To_Cpi's date into a string 
    to_cpi_string = datetime.strptime(To_Date, "%Y-%m-%d").strftime("%B %Y")    

    # Calculates the cost at the user inputted To_Date using the cpi's 
    to_cost = float(From_Cost) * (to_cpi / from_cpi)
    # Calculates the Percentage change between the dates the user inputs 
    pct_change = ((to_cpi - from_cpi) / from_cpi) * 100
    # Calculates the number of years between the dates the user inputs 
    num_of_years = ((to_pos - from_pos)/12)

    # Ensures there is no multipication error if a user inputs the same From_Date and To_Date
    if num_of_years == 0:
            # Returns the result of the average inflation if "Num_Of_Years == 0"
            Avg_Rate_Inflation = 0.0
    else:
            # Calculates the Average inflation within the user set date range using the dates cpi's and "num_of_years"
            Avg_Rate_Inflation = (((to_cpi / from_cpi) ** (1 / num_of_years)) - 1) * 100
    # Returns all of the outputs of the conversion 
    return to_cost, pct_change, from_cpi, to_cpi, Avg_Rate_Inflation, num_of_years, from_cpi_string, to_cpi_string

# Prompts the user to enter in the desired dates and cost in the correct formatting
print ("Enter in the Price of goods in the Starting date, the From Date")
print("and the to Date to calculate the new cost")
print ("Dates must be in YYYY-MM-DD (Ex. 2000-04-01) format with 01 being the only day available")

# applies the convert function to the user inputted data and splits data with ","
result = convert(*input("Enter (Cost,From Date,To Date): ").split(","))

# Gives all of the final output values to the user if the user input "result" is valid
if result is not None:
     # Defines Result and relates it to all of the variables within the conversion function
     to_cost, pct_change, from_cpi, to_cpi, Avg_Rate_Inflation, num_of_years, from_cpi_string, to_cpi_string = result
     print(f"Converted Cost: ${to_cost:.2f}")
     print(f"Percent change: {pct_change:.2f}%")
     print(f"CPI for first year: ({from_cpi_string}) {from_cpi:.1f}")
     print(f"CPI for second year:({to_cpi_string}) {to_cpi:.1f}")
     print(f"Average annual rate of inflation (%) / Decline in the value of money: {Avg_Rate_Inflation:.2f}%")
     print(f"Number of years are: {num_of_years:.2f}")
     print("2002 CPI = 100.0")
     
# Gives users guidance on possible mistakes that make the "result" invalid
else:
     print ("Please restart and try again with valid entries.")
     print ("For Dates Valid Entries are between 1914-01-01, and 2026-09-01")
     print ("For Cost Values only integer/floats are valid please restart and try again")