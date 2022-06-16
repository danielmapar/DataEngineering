import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

"""
Runs SQL drop commands specified at sql_queries.py
"""
def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

"""
Runs SQL create commands specified at sql_queries.py
"""
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


"""
This function loads config parameters from dwg.cfg, 
connects to Amazon Redshift cluster, drops database 
tables and creates database tables.
"""
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    print("connecting to redshift...")
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    print("connected to redshift!")

    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()