from airflow import DAG
from airflow.operators import LoadDimensionOperator

def load_dimension_sub_dag(
    parent_dag_name,
    task_id,
    redshift_conn_id,
    sql_statement,
    delete_rows,
    table_name,
    *args, **kwargs):

    dag = DAG(f"{parent_dag_name}.{task_id}", **kwargs)

    load_dimension_table = LoadDimensionOperator(
        task_id=task_id,
        dag=dag,
        redshift_conn_id=redshift_conn_id,
        sql_query=sql_statement,
        delete_rows=delete_rows,
        table_name=table_name,
    )

    return dag