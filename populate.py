# Fetches entries from RSS subscriptions and populates database

# Import necessary libs...
import sys
import sqlite3
import feedparser as fp

# Import necessary files...
from helper import get_current_date


def push_to_db(db_file):
    """ Checks for RSS subscriptions file. Throw error and exit if none are found """
    try:
        with open(".rmotd_feeds", "r", encoding="utf-8") as f:
            feeds = f.readlines()
    except FileNotFoundError:
        print("[ERROR] - No feeds file found!\n"\
              "Try running `rmotd --setup` to create a feeds file..."
        )
        sys.exit()

    entry_grabber(feeds, db_file)


def entry_grabber(feeds, db_file):
    """ Pulls entries down from RSS feeds
        and inserts them into rmotd db """
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    current_time = get_current_date()

    # Could probably make this faster
    for url in feeds:
        d = fp.parse(url.strip("\n"))
        for entry in d.entries:
            cur.execute("""
            INSERT INTO rmotdEntries (title, desc, link, read, day, year)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (entry.title, sanitize(entry.description), entry.link,
             False, current_time[0], current_time[1]))

    # Add this in ONLY to verify the queries added successfully
    cur.execute("SELECT title, desc, link FROM rmotdEntries")
    rows = cur.fetchone()

    # For testing purposes. Prints out all contents in table
    for _ in rows:
        print(_)

    conn.commit()
    conn.close()


def sanitize(entry_desc):
    """ Cleans up entry descriptions.
        Looks for extra <p> and </p> """
    return entry_desc[:entry_desc.find("<p>")]
