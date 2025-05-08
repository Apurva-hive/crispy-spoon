import os
import pandas as pd
from collections import defaultdict

# Folder with CSV files
data_folder = "temperature_data"

# Seasons mapping
seasons = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"]
}

# Data structures
seasonal_data = defaultdict(list)      # {season: [temps]}
station_temps = defaultdict(list)      # {station: [monthly temps across all years]}

# Process each CSV file
for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        filepath = os.path.join(data_folder, filename)
        df = pd.read_csv(filepath)

        # Clean column names
        df.columns = df.columns.str.strip()
        for _, row in df.iterrows():
            station = row.get("STATION_NAME", "Unknown Station")
            monthly_avgs = []
            for month in ["January", "February", "March", "April", "May", "June",
                          "July", "August", "September", "October", "November", "December"]:
                temp = row.get(month)
                if pd.notna(temp):
                    monthly_avgs.append(temp)

            # Add temps for the station
            station_temps[station].extend(monthly_avgs)

            # Group temps by season
            for season, months in seasons.items():
                season_values = [row.get(month) for month in months if pd.notna(row.get(month))]
                seasonal_data[season].extend(season_values)

# 1. Average temperature per season
seasonal_averages = {
    season: round(sum(temps) / len(temps), 2)
    for season, temps in seasonal_data.items() if temps
}

with open("average_temp.txt", "w") as f:
    for season, avg in seasonal_averages.items():
        f.write(f"{season}: {avg}°C\n")

# 2. Largest temperature range per station
temp_ranges = {
    station: max(temps) - min(temps)
    for station, temps in station_temps.items() if temps
}

if temp_ranges:
    max_range = max(temp_ranges.values())
    stations_with_max_range = [s for s, r in temp_ranges.items() if r == max_range]

    with open("largest_temp_range_station.txt", "w") as f:
        f.write(f"Largest range: {max_range:.2f}°C\n")
        f.write("Station(s):\n")
        for station in stations_with_max_range:
            f.write(f"{station}\n")

# 3. Warmest and coolest stations by individual temperature readings
max_temp = float('-inf')
min_temp = float('inf')
warmest_stations = set()
coolest_stations = set()

for station, temps in station_temps.items():
    if not temps:
        continue
    station_max = max(temps)
    station_min = min(temps)

    if station_max > max_temp:
        max_temp = station_max
        warmest_stations = {station}
    elif station_max == max_temp:
        warmest_stations.add(station)

    if station_min < min_temp:
        min_temp = station_min
        coolest_stations = {station}
    elif station_min == min_temp:
        coolest_stations.add(station)

with open("warmest_and_coolest_station.txt", "w") as f:
    f.write(f"Warmest Station(s) (based on highest recorded temp {max_temp:.2f}°C):\n")
    for s in warmest_stations:
        f.write(f"{s}\n")

    f.write(f"\nCoolest Station(s) (based on lowest recorded temp {min_temp:.2f}°C):\n")
    for s in coolest_stations:
        f.write(f"{s}\n")