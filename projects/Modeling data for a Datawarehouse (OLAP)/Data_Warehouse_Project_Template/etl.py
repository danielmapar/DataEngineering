import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

"""
Runs SQL copy commands specified at sql_queries.py
"""
def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

"""
Runs SQL insert commands specified at sql_queries.py
"""
def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

"""
This function loads config parameters from dwg.cfg, 
connects to Amazon Redshift cluster, loads data from S3
to staging tables and inserts data from staging tables
to facts and dimensions tables.
"""
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    print("connecting to redshift...")
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    print("connected to redshift!")
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()