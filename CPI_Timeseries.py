# Start off by importing the relevant libaries for the project
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# reads CSV File using pandas and assigns it to a data frame variable along with skipping into the data rows
df = pd.read_csv("STATIC_INFLATIONCALC.csv", skiprows=8)

dates_np = df["date"].to_numpy()
cpi_np = df["STATIC_INFLATIONCALC"].to_numpy()

print(df)

ax.set_xlabel('Date')
ax.set_ylabel('CPI')
ax.set_title('CPI Over Time', fontsize=16)