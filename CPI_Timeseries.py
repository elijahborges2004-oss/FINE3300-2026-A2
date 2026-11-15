# Start off by importing the relevant libraries for the project
import pandas as pd
import matplotlib.pyplot as plt

# Defines the base level of CPI and the number of rows to go back to calculate the annual change
base = 100
lag = 12

# reads CSV File using pandas and assigns it to a data frame variable along with skipping into the data rows
df = pd.read_csv("STATIC_INFLATIONCALC.csv", skiprows=8)
# Converts the "date" column from text into real dates so the graph has a proper time axis
df["date"] = pd.to_datetime(df["date"])
# Calculates the percentage change in CPI compared to 12 rows (one year) back and stores it in a new column
df["pct_change"] = df["STATIC_INFLATIONCALC"].pct_change(lag) * 100

# Creates the figure and the main (left hand) axis, constrained layout stops the labels from overlapping
fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
# Plots the CPI against the dates on the left axis
ax.plot(df["date"], df["STATIC_INFLATIONCALC"], color='blue', lw=2, label='CPI')
# Draws the dotted horizontal line through the base level of 100
ax.axhline(base, ls=':', color='black', label='Base Level (2002 = 100)')

# Creates a second y axis on the right hand side that shares the same x axis (the dates)
ax2 = ax.twinx()
# Plots the annual percentage change on the right axis
ax2.plot(df["date"], df["pct_change"], color='red', lw=2, label='Annual Inflation Rate (%)')

# Labels the x axis and the left y axis, the colour matches the CPI line
ax.set_xlabel('Date')
ax.set_ylabel('CPI [Index]', color='blue')
# Labels the right y axis, the colour matches the inflation line
ax2.set_ylabel('Annual Change [%]', color='red')
# Gives the graph its title
ax.set_title('Canadian CPI and Annual Inflation Rate', fontsize=16)

# Gets the legend entries from both axes since each axis only knows about its own lines
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
# Combines the entries from both axes into one legend in the lower right corner
ax.legend(h1 + h2, l1 + l2, loc='lower right')

# Saves the figure in a PNG format with a resolution of 300 dpi
plt.savefig('CPI_Graph.png', dpi=300)
# Returns the graph in a window for the user to view
plt.show()