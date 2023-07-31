def check_year_month_argument(argument):
    if '/' in argument:
        year, month = argument.split('/')
        if not (len(year) == 4 and year.isdigit()):
            return False
        if month and not (month.isdigit()):
            return False
        return True
    return False
