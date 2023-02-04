# Import necessary libs...
import os
import argparse

# Import necessary files...
import setup
import populate
import cleanup_entries


def main():
    """ Main function... (duh) """
    db_file = "rmotd_feeds.db"
    if not os.path.exists(db_file):
        print("Running setup script...")
        setup.init_db(db_file)
        setup.store_subs()
        print("Database now exists!")

    populate.push_to_db(db_file)
    # Add exception here after some testing

    # Add check for no entries in database

    # Add function to append entries to rss feeds file

    # Add a check for if no input from user, maybe don't create a db file

    # Actually, move the feed adding to another separate function for
    # when user runs --add to add another RSS subscription

    # Nevermind, that already happens lol. Just call store_subs() when
    # user runs --add to accomplish above

    # Add in here somewhere cleanup_entries to clean the database!

    
if __name__ == '__main__':
    main()
