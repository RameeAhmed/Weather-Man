import sys
import os
import pandas as pd
import calendar
variable = sys.argv[1]


def check_year_month_argument(argument):
    if '/' in argument:
        year, month = argument.split('/')
        if not (len(year) == 4 and year.isdigit()):
            return False
        if month and not (month.isdigit()):
            return False
        return True
    return False


"""def convert_to_two_digit_month(month):
    return f"{int(month):02}"""


def switch_month_abbreviation(month_number):
    return calendar.month_abbr[month_number]


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 weatherman.py <a/e> <year/month> <location>")
        sys.exit(1)

    option = sys.argv[1]
    if option not in ['-a', '-e', '-c']:
        print("Invalid option. Use either '-a' or '-e'.")
        sys.exit(1)

    date_location = sys.argv[2]
    location = sys.argv[3]

    if check_year_month_argument(date_location):
        year, month = date_location.split('/')
        print(f"Option: {option}")
        print(f"Year: {year}")
        if month:
            """month = convert_to_two_digit_month(month)"""

            print(f"Month: {month}")
        print(f"Location: {location}")
    else:
        year = date_location
        print(f"Option: {option}")
        print(f"Year: {year}")
        print(f"Location: {location}")


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


data = []

if (variable == '-a'):
    x = extraction_path(location, year, month)
    fileswinfolder = os.listdir(location)
    for file in fileswinfolder:
        if (file in files):
            with open(str(location+"/"+file), "r") as file1:
                if (location == 'lahore_weather'):
                    file1.readline()
                    file1.readline()
                else:
                    file1.readline()
                for line in file1:
                    tokens = line.strip().split(",")
                    if (len(tokens) == 23):
                        source = tokens[0]  # Extract GST or PKT

                    # Convert 'Max TemperatureC', 'Min TemperatureC', and 'Max Humidity' columns to numeric
                        max_temp = pd.to_numeric(
                            tokens[1], errors='coerce')  # Max TemperatureC
                        min_temp = pd.to_numeric(
                            tokens[3], errors='coerce')  # Min TemperatureC
                        max_humidity = pd.to_numeric(
                            tokens[7], errors='coerce')  # Max Humidity

                        data.append({
                            "Source": source,
                            "Max TemperatureC": max_temp,
                            "Min TemperatureC": min_temp,
                            "Max Humidity": max_humidity,
                        })
                    else:
                        pass
    df = pd.DataFrame(data)
    average_value_hum = df['Max Humidity'].mean()
    average_value_max_tem = df['Max TemperatureC'].mean()
    average_value_min_temp = df['Min TemperatureC'].mean()
    print(f"Highest Average:{average_value_max_tem}")
    print(f"Highest Average:{average_value_min_temp}")
    print(f"Highest Average:{average_value_hum}%")

elif (variable == '-e'):

    x = extraction_path(location, year)
    fileswinfolder = os.listdir(location)
    for file in fileswinfolder:
        if file in files:
            with open(str(location + "/" + file), "r") as file1:
                # Skip the header line
                if (location == 'lahore_weather'):
                    file1.readline()
                    file1.readline()
                else:
                    file1.readline()
                for line in file1:
                    tokens = line.strip().split(",")
                    if (len(tokens) == 23):
                        source = tokens[0]  # Extract GST or PKT

                    # Convert 'Max TemperatureC', 'Min TemperatureC', and 'Max Humidity' columns to numeric
                        max_temp = pd.to_numeric(
                            tokens[1], errors='coerce')  # Max TemperatureC
                        min_temp = pd.to_numeric(
                            tokens[3], errors='coerce')  # Min TemperatureC
                        max_humidity = pd.to_numeric(
                            tokens[7], errors='coerce')  # Max Humidity

                        data.append({
                            "Source": source,
                            "Max TemperatureC": max_temp,
                            "Min TemperatureC": min_temp,
                            "Max Humidity": max_humidity,
                        })
                    else:
                        pass
    df = pd.DataFrame(data)

    # Your existing code for calculating max_temp, max_humidity, and other parts remains the same

    df = pd.DataFrame(data)
    max_temp = df['Max TemperatureC'].max()
    max_humidity = df['Max Humidity'].max()
    min_temp = df['Min TemperatureC'].min()

    # Assuming your DataFrame is named 'df' and it contains the required columns

    # Assuming your DataFrame is named 'df' and it contains the required columns

# Convert 'Max TemperatureC' column to numeric, ignoring errors and setting invalid parsing as NaN
    df['Max TemperatureC'] = pd.to_numeric(
        df['Max TemperatureC'], errors='coerce')

# Convert 'Max Humidity' column to numeric, ignoring errors and setting invalid parsing as NaN
    df['Max Humidity'] = pd.to_numeric(df['Max Humidity'], errors='coerce')

# Convert 'Min TemperatureC' column to numeric, ignoring errors and setting invalid parsing as NaN
    df['Min TemperatureC'] = pd.to_numeric(
        df['Min TemperatureC'], errors='coerce')

# Find the index of the row with the maximum temperature
    max_temp_index = df['Max TemperatureC'].idxmax()
    df.dropna(inplace=True)
# Get the date with the maximum temperature
    max_temp_date = df.loc[max_temp_index, 'Source']

# Find the index of the row with the maximum humidity
    max_humidity_index = df['Max Humidity'].idxmax()

# Get the date with the maximum humidity
    max_humidity_date = df.loc[max_humidity_index, 'Source']

# Find the index of the row with the minimum temperature
    min_temp_index = df['Min TemperatureC'].idxmin()

# Get the date with the minimum temperature
    min_temp_date = df.loc[min_temp_index, 'Source']

    max_temp_date_list = max_temp_date.split("-")
    min_temp_date_list = min_temp_date.split("-")
    max_humidity_date_list = max_humidity_date.split("-")

    # Get the full month name using the month number
    full_month_name1 = calendar.month_name[int(max_humidity_date_list[1])]
    full_month_name2 = calendar.month_name[int(min_temp_date_list[1])]
    full_month_name3 = calendar.month_name[int(max_temp_date_list[1])]

    print(
        f"Highest:{max_temp}C on {full_month_name3} {int(max_temp_date_list[2])}")
    print(
        f"lowest:{min_temp}C on {full_month_name2} {int(min_temp_date_list[2])} ")
    print(
        f"Humid:{max_humidity}% on {full_month_name1} {int(max_humidity_date_list[2])}")

elif (variable == '-c'):
    x = extraction_path(location, year, month)
    fileswinfolder = os.listdir(location)
    for file in fileswinfolder:
        if (file in files):
            with open(str(location+"/"+file), "r") as file1:
                if (location == 'lahore_weather'):
                    file1.readline()
                    file1.readline()
                else:
                    file1.readline()
                for line in file1:
                    tokens = line.strip().split(",")
                    if (len(tokens) == 23):
                        source = tokens[0]  # Extract GST or PKT

                    # Convert 'Max TemperatureC', 'Min TemperatureC', and 'Max Humidity' columns to numeric
                        max_temp = pd.to_numeric(
                            tokens[1], errors='coerce')  # Max TemperatureC
                        min_temp = pd.to_numeric(
                            tokens[3], errors='coerce')  # Min TemperatureC
                        max_humidity = pd.to_numeric(
                            tokens[7], errors='coerce')  # Max Humidity

                        data.append({
                            "Source": source,
                            "Max TemperatureC": max_temp,
                            "Min TemperatureC": min_temp,
                            "Max Humidity": max_humidity,
                        })
                    else:
                        pass
    df = pd.DataFrame(data)
    df.fillna(0, inplace=True)
    index_list = df.index.tolist()
    for x in index_list:
        max_temp_value = df.iloc[x, df.columns.get_loc('Max TemperatureC')]
        print(f"{x}"+"\033[31m*\033[0m" *
              int(max_temp_value)+(f"{max_temp_value}C"))
        min_temp_value = df.iloc[x, df.columns.get_loc('Min TemperatureC')]
        print(f"{x}"+"\033[94m*\033[0m" *
              int(min_temp_value)+(f"{min_temp_value}C"))

    for x in index_list:
        max_temp_value = df.iloc[x, df.columns.get_loc('Max TemperatureC')]
        min_temp_value = df.iloc[x, df.columns.get_loc('Min TemperatureC')]
        print(f"{x}"+"\033[94m*\033[0m"*int(min_temp_value)+"\033[31m*\033[0m" *
              int(max_temp_value)+f"{min_temp_value}C {max_temp_value}C")
