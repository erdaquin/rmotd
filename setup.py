# Creates database and RSS subscriptions file

import sqlite3

def init_db(db_file):
    """ Creates database """
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE rmotdEntries (
        title TEXT,
        desc TEXT,
        link TEXT,
        read BOOLEAN,
        day NUMERIC,
        year NUMERIC
    )
    """)

    conn.commit()
    conn.close()

def store_subs():
    """ Prompt user to store RSS subscriptions """
    feeds_file = ".rmotd_feeds"
    subs = []
    while True:
        enter_sub = input("Please enter an RSS feed. When done, press [ENTER|RETURN] to submit or quit: ") + "\n"
        if enter_sub.strip("\n") == "":
            confirm_done = input("Press [ENTER|RETURN] again to quit...")
            if confirm_done.lower() == "":
                break
            continue
        # Check if valid RSS feed. Make function for better parsing?
        if "rss" not in enter_sub.lower():
            print("Please enter a valid RSS feed.")
            continue
        else:
            subs.append(enter_sub)

    # Check if user input anything 
    if len(subs) == 0:
        print("[WARNING] No input from user!")
    else:
        with open(feeds_file, "w", encoding="utf-8") as f:
            f.writelines(subs)
        print("RSS feeds file `{}` created successfully...".format(feeds_file))
            
    
    
