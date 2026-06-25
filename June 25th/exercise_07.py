from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_department_file():
    data = "IT,45000\nHR,35000\nFinance,50000\nIT,55000\nFinance,40000\nHR,30000"
    with open("/tmp/departments.txt", "w") as f:
        f.write(data)
    print("departments.txt created!")

def calculate_department_salary():
    totals = {}
    with open("/tmp/departments.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                dept, salary = line.split(",")
                totals[dept] = totals.get(dept, 0) + int(salary)
    with open("/tmp/dept_salary_result.txt", "w") as f:
        for dept, total in totals.items():
            f.write(f"{dept}={total}\n")
    for dept, total in totals.items():
        print(f"{dept} = {total}")

def generate_department_report():
    lines = ["=" * 40, "     DEPARTMENT SALARY REPORT", "=" * 40]
    with open("/tmp/dept_salary_result.txt", "r") as f:
        for line in f:
            dept, total = line.strip().split("=")
            lines.append(f"  {dept:<12} : Rs.{int(total):,}")
    lines.append("=" * 40)
    report = "\n".join(lines)
    with open("/tmp/department_report.txt", "w") as f:
        f.write(report)
    print("department_report.txt generated!")
    print(report)

with DAG(
    dag_id="exercise_07_department_salary",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["exercise"]
) as dag:
    task1 = PythonOperator(task_id="create_department_file",      python_callable=create_department_file)
    task2 = PythonOperator(task_id="calculate_department_salary", python_callable=calculate_department_salary)
    task3 = PythonOperator(task_id="generate_department_report",  python_callable=generate_department_report)
    task1 >> task2 >> task3
