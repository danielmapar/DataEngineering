from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator, CreateTableOperator)
from airflow.operators.subdag_operator import SubDagOperator
from helpers import SqlQueries
from load_dimension_sub_dag import load_dimension_sub_dag

# AWS_KEY = os.environ.get('AWS_KEY')
# AWS_SECRET = os.environ.get('AWS_SECRET')

S3_BUCKET_NAME = "udacity-dend"
S3_LOG_KEY = "log_data"
S3_SONG_KEY = "song_data"
JSON_LOG_FILE = "log_json_path.json"
DAG_NAME = 'udac_example_dag'

default_args = {
    'owner': 'udacity',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 12),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup': False
}

dag = DAG('udac_example_dag',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow',
          schedule_interval='0 * * * *', # every hour
          max_active_runs=1
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

create_tables_redshift = CreateTableOperator(
    task_id='create_tables_redshift',
    redshift_conn_id='redshift',
    dag=dag
)

stage_events_to_redshift = StageToRedshiftOperator(
    task_id='Stage_events',
    table_name="staging_events",
    s3_bucket=S3_BUCKET_NAME,
    s3_key=S3_LOG_KEY,
    file_format="JSON",
    json_log_file=JSON_LOG_FILE,
    redshift_conn_id="redshift",
    aws_credential_id="aws_credentials",
    dag=dag,
    provide_context=True
)

stage_songs_to_redshift = StageToRedshiftOperator(
    task_id='Stage_songs',
    table_name="staging_songs",
    s3_bucket=S3_BUCKET_NAME,
    s3_key=S3_SONG_KEY,
    file_format="JSON",
    redshift_conn_id="redshift",
    aws_credential_id="aws_credentials",
    dag=dag,
    provide_context=True
)

load_songplays_table = LoadFactOperator(
    task_id='Load_songplays_fact_table',
    redshift_conn_id='redshift',
    sql_query=SqlQueries.songplay_table_insert, 
    dag=dag
)

load_user_dimension_table = SubDagOperator(
    subdag=load_dimension_sub_dag(
        parent_dag_name=DAG_NAME,
        task_id="Load_user_dim_table",
        redshift_conn_id="redshift",
        start_date=default_args['start_date'],
        sql_statement=SqlQueries.user_table_insert,
        delete_rows=True,
        table_name="users",
    ),
    task_id="Load_user_dim_table",
    dag=dag,
)

load_song_dimension_table = SubDagOperator(
    subdag=load_dimension_sub_dag(
        parent_dag_name=DAG_NAME,
        task_id="Load_song_dim_table",
        redshift_conn_id="redshift",
        start_date=default_args['start_date'],
        sql_statement=SqlQueries.song_table_insert,
        delete_rows=True,
        table_name="songs",
    ),
    task_id="Load_song_dim_table",
    dag=dag,
)

load_artist_dimension_table = SubDagOperator(
    subdag=load_dimension_sub_dag(
        parent_dag_name=DAG_NAME,
        task_id="Load_artist_dim_table",
        redshift_conn_id="redshift",
        start_date=default_args['start_date'],
        sql_statement=SqlQueries.artist_table_insert,
        delete_rows=True,
        table_name="artists",
    ),
    task_id="Load_artist_dim_table",
    dag=dag,
)

load_time_dimension_table = SubDagOperator(
    subdag=load_dimension_sub_dag(
        parent_dag_name=DAG_NAME,
        task_id="Load_time_dim_table",
        redshift_conn_id="redshift",
        start_date=default_args['start_date'],
        sql_statement=SqlQueries.time_table_insert,
        delete_rows=True,
        table_name="time",
    ),
    task_id="Load_time_dim_table",
    dag=dag,
)

has_rows_checker = lambda records: len(records) == 1 and len(records[0]) == 1 and records[0][0] > 0
has_no_rows_checker = lambda records: len(records) == 1 and len(records[0]) == 1 and records[0][0] == 0
sql_count_query = 'SELECT COUNT(*) FROM {}'

run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    redshift_conn_id='redshift',
    sql_statements=(
        sql_count_query.format('songplays'), 
        sql_count_query.format('users'),
        sql_count_query.format('artists'),
        sql_count_query.format('songs'), 
        sql_count_query.format('time'), 
        'SELECT COUNT(*) FROM users WHERE first_name IS NULL'
    ),
    checks=(
        has_rows_checker, 
        has_rows_checker,
        has_rows_checker, 
        has_rows_checker,
        has_rows_checker, 
        has_no_rows_checker
    ),
    dag=dag
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

start_operator >> create_tables_redshift
create_tables_redshift >> [stage_songs_to_redshift, stage_events_to_redshift] >> load_songplays_table

load_songplays_table >> [load_user_dimension_table, load_song_dimension_table, load_artist_dimension_table, load_time_dimension_table] >> run_quality_checks >> end_operator
