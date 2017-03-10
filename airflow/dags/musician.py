from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from src.src.loaders.global_loader import load_items

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2017, 3, 6),
    'email_on_failure': False,
    'email_on_retry': False,
    'email': ['airflow@airflow.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


dag = DAG('musician_load', default_args=default_args, schedule_interval="31 2 * * *")

t1 = PythonOperator(
    dag=dag,
    task_id='load_profile_information',
    provide_context=False,
    python_callable=load_items)
