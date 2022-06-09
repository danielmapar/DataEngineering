# Sparkify

## Introduction

* This project aims to ETL data from a fictitious music app called Sparkify, this applications is similar to Spotify / Apple Music. The extracted data from this app enables us to query informations about users, artists, songs related to those artists and listened songs. On that note, this dataset could be utilized by data scientists to understand users listening patterns, users preferred songs, users preferred artists and much more. Potentially we could use this data to train a Machine Learning model to suggest songs to users.

## How to run the project

* Make sure to first install [Python](https://www.python.org/downloads/) and the  [PostgreSQL client](https://www.timescale.com/blog/how-to-install-psql-on-mac-ubuntu-debian-windows/)

* After installing Python, please run: `pip install pandas psycopg2`. 

* After installing the PostgreSQL client, make sure to test your connection with the [Amazon Redshift](https://aws.amazon.com/pm/redshift/?trk=9afe6d50-880f-4406-b73d-581c81995108&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Analytics|Redshift|CA|EN|Text|xx|SEM&s_kwcid=AL!4422!3!525873052690!e!!g!!amazon%20redshift&ef_id=CjwKCAjwtIaVBhBkEiwAsr7-c0Rx5pboUf28ubAU8R2344wJUciwE0X-xlIlxZgLF34tYGenzBA0WBoCuQcQAvD_BwE:G:s&s_kwcid=AL!4422!3!525873052690!e!!g!!amazon%20redshift) cluster by running: `psql -h redshift-cluster-3.cjd6tlx48795.us-east-1.redshift.amazonaws.com -U sampleuser -d dev -p 5439`

* Run `python create_tables.py` to create the necessary database tables and `python etl.py` to populate those tables with data.

* After running the scripts, you should be able to query data within `Amazon Redshift`.

## Project files

* **create_tables.py**
    * Creates `Staging`, `Facts` and `Dimensions` tables

* **etl.py**
    * ELT pipeline that loads `S3` data to Redshift `Staging` tables and subsequentially loads the data from the `Staging` tables to the appropriate `Facts` and `Dimensions` tables.

* **sql_queries.py**
    * Groups the necessary SQL query statements for `create_tables.py` and `etl.py`

* **dwh.cfg**
    * A config file that specifies details about database connection and `S3` file paths.

* **terraform**
    * A folder containing the necessary `IaC` to provision the `Amazon Redshift` cluster.