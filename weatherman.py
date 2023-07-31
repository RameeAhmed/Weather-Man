import sys
import os
import pandas as pd
import calendar
from switch_m_abbreviation import switch_month_abbreviation
from year_month import check_year_month_argument
from data_processing import process_file_data,extraction_path
from print_functions_a_e_c import printa,printe,printc


variable = sys.argv[1]


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python weatherman.py <a/e> <year/month> <location>")
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
            print(f"Month: {month} \n Location: {location} ")

    else:
        year = date_location
        print(f"Option: {option} \n Year: {year} \n Location: {location}")


x = extraction_path(location, year)
data = process_file_data(location, year)
df = pd.DataFrame(data)
print(df)
files=extraction_path(location, year, month="")

if (variable == '-a'):
    printa(df)


elif (variable == '-e'):
    printe(df)


elif (variable == '-c'):
    c(df)
