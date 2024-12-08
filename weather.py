from datetime import datetime
from meteostat import Hourly
import pandas as pd

# Define time period
start = datetime(2017, 1, 1)
end = datetime(2024, 12, 31, 23, 59)

# Fetch hourly data for Kathmandu's station (replace 'STATION_ID' with the chosen station)
station_id = '44454'  # Replace with the ID from Step 1; here station id is of kathmandu airport
data = Hourly(station_id, start, end)
data = data.fetch()

# Include time as a column and save to CSV
data.reset_index(inplace=True)
data.to_csv("kathmandu_valley_weather.csv", index=False)

print("Weather data saved to 'kathmandu_valley_weather.csv'")
