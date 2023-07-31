import pandas as pd
import os
from switch_m_abbreviation import switch_month_abbreviation



def extraction_path(location, year, month=""):
    global files
    if month:
        month_abbreviation = switch_month_abbreviation(int(month))
        path = location+"_"+year+"_"+month_abbreviation+".txt"
        folder = location
        files = [file for file in os.listdir(folder) if (
            str(year) in file and str(month_abbreviation) in file)]

    else:
        folder = location
        files = [file for file in os.listdir(folder) if (
            file.endswith(".txt") and str(year) in file)]


def process_file_data(location, year):
    data = []

    files_in_folder = os.listdir(location)
    for file in files_in_folder:
        if file in files:
            with open(str(location + "/" + file), "r") as file1:
                # Skip the header line
                if location == 'lahore_weather':
                    file1.readline()
                    file1.readline()
                else:
                    file1.readline()
                for line in file1:
                    tokens = line.strip().split(",")
                    if len(tokens) == 23:
                        source = tokens[0]  # Extract GST or PKT

                        # Convert 'Max TemperatureC', 'Min TemperatureC', and 'Max Humidity' columns to numeric
                        max_temp = pd.to_numeric(tokens[1], errors='coerce')  # Max TemperatureC
                        min_temp = pd.to_numeric(tokens[3], errors='coerce')  # Min TemperatureC
                        max_humidity = pd.to_numeric(tokens[7], errors='coerce')  # Max Humidity

                        data.append({
                            "Source": source,
                            "Max TemperatureC": max_temp,
                            "Min TemperatureC": min_temp,
                            "Max Humidity": max_humidity,
                        })
                    else:
                        pass
    return data
