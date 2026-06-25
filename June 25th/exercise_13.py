from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_employee_file():
    data = "Rahul,28\nPriya,31\nAmit,42\nSneha,26\nKiran,38"
    with open("/tmp/employees.txt", "w") as f:
        f.write(data)
    print("employees.txt created!")

def calculate_average_age():
    employees = {}
    with open("/tmp/employees.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                name, age = line.split(",")
                employees[name] = int(age)
    youngest = min(employees, key=employees.get)
    oldest   = max(employees, key=employees.get)
    average  = sum(employees.values()) / len(employees)
    with open("/tmp/age_calc.txt", "w") as f:
        f.write(f"youngest={youngest},{employees[youngest]}\n")
        f.write(f"oldest={oldest},{employees[oldest]}\n")
        f.write(f"average={average:.1f}\n")
    print(f"Youngest Employee = {youngest} (Age {employees[youngest]})")
    print(f"Oldest Employee   = {oldest} (Age {employees[oldest]})")
    print(f"Average Age       = {average:.1f}")

def generate_age_report():
    r = {}
    with open("/tmp/age_calc.txt", "r") as f:
        for line in f:
            k, v = line.strip().split("=", 1)
            r[k] = v
    y_name, y_age = r["youngest"].split(",")
    o_name, o_age = r["oldest"].split(",")
    report = (
        "=" * 40 + "\n"
        "       EMPLOYEE AGE REPORT\n"
        "=" * 40 + "\n"
        f"  Youngest : {y_name} (Age {y_age})\n"
        f"  Oldest   : {o_name} (Age {o_age})\n"
        f"  Average  : {r['average']} years\n"
        "=" * 40
    )
    with open("/tmp/age_report.txt", "w") as f:
        f.write(report)
    print("age_report.txt generated!")
    print(report)

with DAG(
    dag_id="exercise_13_employee_age",
    start_date=datetime(2024, 1, 1),
    schedule="@monthly",
    catchup=False,
    tags=["exercise"]
) as dag:
    task1 = PythonOperator(task_id="create_employee_file",  python_callable=create_employee_file)
    task2 = PythonOperator(task_id="calculate_average_age", python_callable=calculate_average_age)
    task3 = PythonOperator(task_id="generate_age_report",   python_callable=generate_age_report)
    task1 >> task2 >> task3
