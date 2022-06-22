# Airflow Data Pipeline - Sparkfy

## Local Setup

* Install [Python](https://www.python.org/)

* Install [Airflow](https://airflow.apache.org/) locally
    * `pip install "apache-airflow[celery]==2.3.2" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.7.txt" --ignore-installed PyYAML`

* Setup Airflow db:
    * `airflow db upgrade`

* Install `AWS` and `Postgres` Airflow provider packages:
    * `pip install apache-airflow-providers-amazon`
    * `pip install apache-airflow-providers-postgres`
    
* Create Airflow root user:
    * `airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin`

* Start Airflow scheduler and web server:
    * `./start.sh`
    * To turn it off check port `3000`
        * `lsof -i tcp:3000`
        * `kill <pid>`