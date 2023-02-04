# Used to clean up old entries in rmotd_feed.db

# Import necessary files...
from helper import get_current_date


def get_age_of_entry(day, year):
    """ Returns age of entry (in days) """
    curr = get_current_date()
    if year < curr[1]:
        return abs(day - (365 * (curr[1] - year))) + curr[0]
    else:
        return abs(day - curr[0])

def rem_entry_from_db(entry, entry_age):
    """ Checks age of read entries and removes `old` entries from db """
    if age >= 3:
        # Do stuff with entry
        pass
    
