from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_file():
    content = "Welcome to Apache Airflow\nLearning DAGs\nLearning Task Dependencies"
    with open("/tmp/message.txt", "w") as f:
        f.write(content)
    print("File created: /tmp/message.txt")

def read_file():
    with open("/tmp/message.txt", "r") as f:
        content = f.read()
    print("File contents:")
    print(content)

with DAG(
    dag_id="exercise_01_create_read_file",
    start_date=datetime(2024, 1, 1),
    schedule="@once",
    catchup=False,
    tags=["exercise"]
) as dag:
    task1 = PythonOperator(task_id="create_file", python_callable=create_file)
    task2 = PythonOperator(task_id="read_file",   python_callable=read_file)
    task1 >> task2
