# An assortment of helper functions to use
# throughout the program

# Import necessary libs...
from datetime import datetime, date


def get_current_date():
    """ Returns [current day, year] """
    return [datetime.now().timetuple().tm_yday, date.today().year]
