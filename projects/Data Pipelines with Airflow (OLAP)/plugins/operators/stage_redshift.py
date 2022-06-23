from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 aws_credential_id="",
                 table_name="",
                 s3_bucket="",
                 s3_key="",
                 file_format="",
                 json_log_file="",
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.aws_credential_id = aws_credential_id
        self.table_name = table_name
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.file_format = file_format
        self.json_log_file = json_log_file
        self.execution_date = kwargs.get("execution_date")    
        self.copy_query = "COPY {} FROM '{}' ACCESS_KEY_ID '{}' SECRET_ACCESS_KEY '{}' FORMAT AS json '{}';"

    def execute(self, context):
        aws_hook = AwsHook(self.aws_credential_id)
        credentials = aws_hook.get_credentials()

        s3_path = "s3://{}/{}".format(self.s3_bucket, self.s3_key)
        copy_query = ""

        if self.json_log_file != "":
            self.json_log_file = "s3://{}/{}".format(self.s3_bucket, self.json_log_file)
            copy_query = self.copy_query.format(self.table_name, s3_path, credentials.access_key, credentials.secret_key, self.log_json_file)
        else:
            copy_query = self.copy_query.format(self.table_name, s3_path, credentials.access_key, credentials.secret_key, "auto")

        redshift_hook = PostgresHook(postgres_conn_id = self.redshift_conn_id)

        self.log.info(f"Running copy query: {copy_query}")
        redshift_hook.run(copy_query)
        self.log.info(f"Table {self.table_name} successfully staged!")