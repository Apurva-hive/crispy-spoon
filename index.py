import os
import pandas as pd

# Function to calculate the average temperature for each season
def calculate_seasonal_avg_temperature(temperature_data):
    # Define seasons with corresponding months
    seasons = ['summer', 'autumn', 'winter', 'spring']
    season_months = {
        'summer': [12, 1, 2],    # Dec, Jan, Feb
        'autumn': [3, 4, 5],     # Mar, Apr, May
        'winter': [6, 7, 8],     # Jun, Jul, Aug
        'spring': [9, 10, 11]    # Sep, Oct, Nov
    }

    seasonal_avg_temps = {season: [] for season in seasons}

    # Loop over each CSV file (each year of data)
    for filename in os.listdir(temperature_data):
        if filename.endswith(".csv"):
            year_data = pd.read_csv(os.path.join(temperature_data, filename))

            for season, months in season_months.items():
                # Filter data for the specific season
                season_data = year_data[year_data.columns[4:]].iloc[:, months].mean(axis=1)
                seasonal_avg_temps[season].append(season_data.mean())

    # Calculate the overall average for each season
    seasonal_avg_temps = {season: sum(temps) / len(temps) for season, temps in seasonal_avg_temps.items()}

    # Save results to file
    with open("average_temp.txt", "w") as file:
        for season, avg_temp in seasonal_avg_temps.items():
            file.write(f"{season.capitalize()}: {avg_temp:.2f} °C\n")

    print("Average temperatures for each season saved to 'average_temp.txt'.")
    return seasonal_avg_temps

# Function to find the station(s) with the largest temperature range
def find_largest_temp_range_station(temperature_data):
    station_temp_ranges = {}

    # Loop over each CSV file (each year of data)
    for filename in os.listdir(temperature_data):
        if filename.endswith(".csv"):
            year_data = pd.read_csv(os.path.join(temperature_data, filename))

            for station in year_data['STATION_NAME'].unique():
                station_data = year_data[year_data['STATION_NAME'] == station]
                temp_range = station_data.iloc[:, 4:].max().max() - station_data.iloc[:, 4:].min().min()

                # Store the range for each station
                if station not in station_temp_ranges:
                    station_temp_ranges[station] = []

                station_temp_ranges[station].append(temp_range)

    # Find the station(s) with the largest range
    largest_range = max([max(ranges) for ranges in station_temp_ranges.values()])
    largest_range_stations = [
        station for station, ranges in station_temp_ranges.items() if max(ranges) == largest_range
    ]

    # Save results to file
    with open("largest_temp_range_station.txt", "w") as file:
        for station in largest_range_stations:
            file.write(f"Station: {station} with largest temperature range: {largest_range} °C\n")

    print("Stations with the largest temperature range saved to 'largest_temp_range_station.txt'.")
    return largest_range_stations

# Function to find the warmest and coolest station(s)
def find_warmest_and_coolest_station(temperature_data):
    station_avg_temps = {}

    # Loop over each CSV file (each year of data)
    for filename in os.listdir(temperature_data):
        if filename.endswith(".csv"):
            year_data = pd.read_csv(os.path.join(temperature_data, filename))

            for station in year_data['STATION_NAME'].unique():
                station_data = year_data[year_data['STATION_NAME'] == station]
                avg_temp = station_data.iloc[:, 4:].mean(axis=1).mean()

                # Store the average temperature for each station
                if station not in station_avg_temps:
                    station_avg_temps[station] = []

                station_avg_temps[station].append(avg_temp)

    # Find the warmest and coolest station(s)
    warmest_station = max(station_avg_temps, key=lambda station: sum(station_avg_temps[station]) / len(station_avg_temps[station]))
    coolest_station = min(station_avg_temps, key=lambda station: sum(station_avg_temps[station]) / len(station_avg_temps[station]))

    # Save results to file
    with open("warmest_and_coolest_station.txt", "w") as file:
        file.write(f"Warmest Station: {warmest_station}\n")
        file.write(f"Coolest Station: {coolest_station}\n")

    print("Warmest and coolest stations saved to 'warmest_and_coolest_station.txt'.")
    return warmest_station, coolest_station

# Main function to run the program
def main():
    temperature_data = "temperatures"  # Folder containing the CSV files

    # Calculate seasonal average temperatures
    calculate_seasonal_avg_temperature(temperature_data)

    # Find station(s) with the largest temperature range
    find_largest_temp_range_station(temperature_data)

    # Find the warmest and coolest station(s)
    find_warmest_and_coolest_station(temperature_data)

if __name__ == "__main__":
    main()
