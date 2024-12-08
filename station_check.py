from meteostat import Stations

# Search for stations near Kathmandu Valley
stations = Stations()
stations = stations.nearby(27.7172, 85.3240)  # Coordinates of Kathmandu
stations = stations.fetch(5)  # Fetch the top 5 stations

# Print available stations
print(stations)
