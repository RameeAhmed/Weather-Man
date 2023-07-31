import pandas as pd
import calendar
def printa(df):
    average_value_hum = df['Max Humidity'].mean()
    average_value_max_tem = df['Max TemperatureC'].mean()
    average_value_min_temp = df['Min TemperatureC'].mean()
    print(f"Highest Average:{average_value_max_tem}")
    print(f"Highest Average:{average_value_min_temp}")
    print(f"Highest Average:{average_value_hum}%")


def printe(df):
    max_temp = df['Max TemperatureC'].max()
    max_humidity = df['Max Humidity'].max()
    min_temp = df['Min TemperatureC'].min()

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


def printc(df):
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

