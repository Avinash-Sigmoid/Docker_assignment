# from datetime import datetime, timedelta
#
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from current_wheather_data import write_csv
# from weather_table import create_weather_table
# from from_csv_into_table import read_and_load_csv
#
# default_args = {
#     "owner": "Airflow",
#     "depends_on_past": False,
#     "start_date": datetime(2022, 3, 14),
#     "email": ["airflow@airflow.com"],
#     "email_on_failure": False,
#     "email_on_retry": False,
#     "retries": 1,
#     "retry_delay": timedelta(minutes=1),
#     # 'queue': 'bash_queue',
#     # 'pool': 'backfill',
#     # 'priority_weight': 10,
#     # 'end_date': datetime(2016, 1, 1),
# }
#
# dag = DAG("Assignment", default_args=default_args, schedule_interval="0 6 * * *")
#
# t1 = PythonOperator(task_id='Write_into_csv', python_callable=write_csv, dag=dag)
#
# t2 = PythonOperator(task_id="create_table", python_callable=create_weather_table, dag=dag)
#
# t3 = PythonOperator(task_id="read_csv_load_data", python_callable=read_and_load_csv, dag=dag)
#
# t1 >> t2 >> t3
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from postgres_connection import check_connection
from airflow.providers.postgres.hooks.postgres import PostgresHook
from fetch_data import fetch_info

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2022, 3, 19),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG("Docker_assignment", default_args=default_args, schedule_interval=timedelta(1))

t1 = BashOperator(task_id="Welcome", bash_command="echo Hi This is Satyaprakash From Sigmoid", dag=dag)

t2 = PythonOperator(task_id='Adding_info_to_DB_table', python_callable=check_connection, dag=dag)

t3 = PythonOperator(task_id='fetching_info_from_PostgresDB', python_callable=fetch_info, dag=dag)

t1 >> t2 >> t3