import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

"""
This function takes a song file path and extracts the file data
to both "songs" and "artists" tables in the database.

The song file contains informations about songs and its associated artists.
"""
def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = list(df[["song_id", "title", "artist_id", "year", "duration"]].values[0])
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"]]
    artist_data = artist_data.where(pd.notnull(artist_data), None)
    artist_data = list(artist_data.values[0])
    cur.execute(artist_table_insert, artist_data)

"""
This function takes a log file path and extracts the file data
to both "time", "users" and "songplay" tables in the database.

The log file contains information about which songs are users listening to and when.
"""
def process_log_file(cur, filepath):
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page']=="NextSong"]

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    df['ts'] = t
    
    # insert time data records
    time_data =  [list(t.dt.date.values), list(t.dt.hour.values), list(t.dt.day.values), list(t.dt.weekofyear.values), list(t.dt.month.values), list(t.dt.year.values), list(t.dt.weekday.values)]
    column_labels = ("timestamp", "hour", "day", "week of year", "month", "year", "weekday")

    dict = {}
    for index in range(len(column_labels)):
        dict[column_labels[index]] = time_data[index]

    time_df = pd.DataFrame(dict)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[["userId", "firstName", "lastName", "gender", "level"]]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)

"""
This function reads all JSON files from a given directory
and it executes a lambda function passing each file path to it.
"""
def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


"""
This is the entrance of this program. It will connect to the database
and process both song_data files and log_data files.
"""
def main():
    conn = psycopg2.connect("host=172.30.176.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()