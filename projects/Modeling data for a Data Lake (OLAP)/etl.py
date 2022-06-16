"""A etl pipeline to using Spark and Amazon S3."""
import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf


config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID'] = config['AWS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY'] = config['AWS']['AWS_SECRET_ACCESS_KEY']


def create_spark_session():
    """Create a Spark Session capable of interacting with S3 files."""
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    """
    Process song data.

    Read S3 files from "input_data" and converts it to song and artists
    parquet files.
    """
    # get filepath to song data file
    song_data = "{}song_data/*/*/*/*.json".format(input_data)

    # read song data file
    df = spark.read.json(song_data)

    # extract columns to create songs table
    songs_table = df.select(
        'song_id',
        'title',
        'artist_id',
        'year',
        'duration').dropDuplicates()

    # write songs table to parquet files partitioned by year and artist
    songs_table.write.mode("overwrite").partitionBy(
        "year", "artist_id").parquet(
        "{}songs/songs_table.parquet".format(output_data))

    # extract columns to create artists table
    artists_table = df.select(
        'artist_id',
        'artist_name',
        'artist_location',
        'artist_latitude',
        'artist_longitude').dropDuplicates()

    # write artists table to parquet files
    artists_table.write.mode("overwrite").parquet(
        "{}artists/artists_table.parquet".format(output_data))


def process_log_data(spark, input_data, output_data):
    """
    Process Log data.

    Read S3 files from "input_data" and converts it to a user,
    time and songplays parquet files.
    """
    # get filepath to log data file
    log_data = "{}log_data/*/*/*.json".format(input_data)

    # read log data file
    df = spark.read.json(log_data)

    # filter by actions for song plays
    df = df.filter(df.page == 'NextSong')

    # extract columns for users table
    users_table = df.select(
        'userId',
        'firstName',
        'lastName',
        'gender',
        'level').dropDuplicates()

    # write users table to parquet files
    users_table.write.mode("overwrite").parquet(
        '{}users/users_table.parquet'.format(output_data))

    # create timestamp column from original timestamp column
    get_timestamp = udf(lambda x: datetime.fromtimestamp((int(x) / 1000)))
    df = df.withColumn('timestamp', get_timestamp(df.ts))

    # create datetime column from original timestamp column
    get_datetime = udf(lambda x: datetime.fromtimestamp((int(x) / 1000)))
    df = df.withColumn('datetime', get_datetime(df.ts))

    # extract columns to create time table
    time_table = df.selectExpr("hour(timestamp) as hour",
                               "dayofmonth(timestamp) as day",
                               "weekofyear(timestamp) as week",
                               "month(timestamp) as month",
                               "year(timestamp) as year",
                               "dayofweek(timestamp) as weekday",
                               "timestamp as start_time",
                               ).dropDuplicates(["start_time"])

    # write time table to parquet files partitioned by year and month
    time_table.write.mode("overwrite").partitionBy(
        'year', 'month').parquet(
        '{}time/time_table.parquet'.format(output_data))

    # read in song data to use for songplays table
    song_df = spark.read.json('{}song_data/*/*/*/*.json'.format(input_data))

    # create table views for both song and log data
    song_df.createOrReplaceTempView("song_data_view")
    df.createOrReplaceTempView("log_data_view")

    # extract columns from joined song and log datasets to create songplays
    # table
    songplays_table = spark.sql("""
                    SELECT monotonically_increasing_id() as songplay_id,
                                       year(ldv.timestamp) as year,
                                       month(ldv.timestamp) as month,
                                       ldv.timestamp as start_time,
                                       ldv.userId as user_id,
                                       ldv.level as level,
                                       ldv.sessionId as session_id,
                                       ldv.userAgent as user_agent,
                                       ldv.location as location,
                                       sdv.song_id as song_id,
                                       sdv.artist_id as artist_id
                                FROM log_data_view ldv
                                JOIN song_data_view sdv ON (
                                    ldv.song = sdv.title AND
                                    ldv.artist = sdv.artist_name AND
                                    ldv.length = sdv.duration
                                )
                                """)

    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.mode("overwrite").partitionBy(
        "year", "month").parquet(
        "{}songplays/songplays_table.parquet".format(output_data))


def main():
    """
    Entrance method.

    Create a Spark Session and initializes functions to create
    parquet files for artists, songs, users, time and song_plays.
    """
    spark = create_spark_session()
    input_data = config['AWS']['BUCKET_INPUT_DATA']
    output_data = config['AWS']['BUCKET_OUTPUT_DATA']

    process_song_data(spark, input_data, output_data)
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
