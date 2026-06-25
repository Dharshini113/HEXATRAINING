from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_salary_file():
    data = "Rahul,45000\nPriya,52000\nAmit,61000\nSneha,48000"
    with open("/tmp/employees.txt", "w") as f:
        f.write(data)
    print("employees.txt created!")

def calculate_total_salary():
    total = 0
    count = 0
    with open("/tmp/employees.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                name, salary = line.split(",")
                total += int(salary)
                count += 1
    with open("/tmp/salary_calc.txt", "w") as f:
        f.write(f"count={count}\ntotal={total}\n")
    print(f"Employees    = {count}")
    print(f"Total Salary = {total}")

def generate_report():
    r = {}
    with open("/tmp/salary_calc.txt", "r") as f:
        for line in f:
            k, v = line.strip().split("=")
            r[k] = v
    report = f"Salary Report\nEmployees = {r['count']}\nTotal Salary = {r['total']}"
    with open("/tmp/report.txt", "w") as f:
        f.write(report)
    print("report.txt generated!")
    print(report)

with DAG(
    dag_id="exercise_02_salary_report",
    start_date=datetime(2024, 1, 1),
    schedule="@once",
    catchup=False,
    tags=["exercise"]
) as dag:
    task1 = PythonOperator(task_id="create_salary_file",     python_callable=create_salary_file)
    task2 = PythonOperator(task_id="calculate_total_salary", python_callable=calculate_total_salary)
    task3 = PythonOperator(task_id="generate_report",        python_callable=generate_report)
    task1 >> task2 >> task3
