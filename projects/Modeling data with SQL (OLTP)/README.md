# Sparkify

## Introduction

* This project aims to `ETL` data from a fictitious music app called **Sparkify**, this applications is similar to Spotify / Apple Music. The extracted data from this app enables us to query informations about `users`, `artists`, `songs` related to those `artists` and `listened songs`. On that note, this dataset could be utilized by data scientists to understand `users` listening `patterns`, `users` preferred `songs`, `users` preferred `artists` and much more. Potentially we could use this data to train a Machine Learning model to suggest `songs` to `users`.

## How to run the project

* Make sure to first install [Anaconda](https://www.anaconda.com/) and [PostgreSQL](https://www.postgresql.org/)

* After installing `Anaconda`, please run: `pip install pandas psycopg2`. 

* After installing `PostgreSQL`, make sure to create a database called `studentdb` owned by a `user` called `student` with a `password` = `student`

* Run `python3 create_tables.py` to create the necessary database tables and `python etl.py` to populate those tables with data.
    * **IMPORTANT**: Be mindful that for both scripts you need to update `psycopg2.connect` with the appopriate `host`.

* After running the scripts, you should be able to run `jupyter notebook` on your terminal and open `test.ipynb`.
    * This file contains some example queries that can be done over the database.

## Database design details

* This database contains the following tables:
    * `songplays`
        * A table dedicate to store which songs a specific user played at a given date / time.
    * `users`
        * A table that stores users information for easy identification.
    * `songs`
        * A table that stores `songs` details including a reference to their designated `artist`.
    * `artists`
        * A table that stores `artists` details.
    * `time`
        * A table that stores detailed information about the time when a user listened to a song.

* This database was designed to support `JOIN` queries and flexible reporting on `songs`, `song consumption`, `users` and `artists`.
