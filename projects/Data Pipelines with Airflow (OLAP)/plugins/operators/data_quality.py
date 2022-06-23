from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 sql_statements=(),
                 checks=(),
                 *args, **kwargs):

        if len(sql_statements) != len(checks):
            raise Exception('sql_statements and checks must have the same number of elements.')

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.sql_statements = sql_statements
        self.checks = checks

    def execute(self, context):
        redshift_hook = PostgresHook(postgres_conn_id = self.redshift_conn_id)

        for sql_statements, checks in zip(self.sql_statements, self.checks):
            self.log.info(f"Running data quality validation: {sql_statements}")
            records = redshift_hook.get_records(sql_statements)
            if not checks(records):
                raise ValueError('Data quality check failed: {}'.format(sql_statements))
            self.log.info(f"The data quality validation was successful: {sql_statements}")