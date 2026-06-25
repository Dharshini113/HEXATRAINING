from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_attendance():
    data = "Rahul,Present\nPriya,Present\nAmit,Absent\nSneha,Present\nKiran,Absent"
    with open("/tmp/attendance.txt", "w") as f:
        f.write(data)
    print("attendance.txt created!")

def count_present():
    present = 0
    total = 0
    with open("/tmp/attendance.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                name, status = line.split(",")
                total += 1
                if status == "Present":
                    present += 1
    with open("/tmp/present_count.txt", "w") as f:
        f.write(f"present={present}\ntotal={total}\n")
    print(f"Present = {present}")

def count_absent():
    absent = 0
    with open("/tmp/attendance.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                name, status = line.split(",")
                if status == "Absent":
                    absent += 1
    with open("/tmp/absent_count.txt", "w") as f:
        f.write(f"absent={absent}\n")
    print(f"Absent = {absent}")

def generate_summary():
    present = 0
    total = 0
    with open("/tmp/present_count.txt", "r") as f:
        for line in f:
            k, v = line.strip().split("=")
            if k == "present":
                present = int(v)
            if k == "total":
                total = int(v)
    with open("/tmp/absent_count.txt", "r") as f:
        absent = int(f.read().strip().split("=")[1])
    report = f"Total Students = {total}\nPresent = {present}\nAbsent = {absent}"
    with open("/tmp/attendance_report.txt", "w") as f:
        f.write(report)
    print("attendance_report.txt generated!")
    print(report)

with DAG(
    dag_id="exercise_05_attendance_report",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["exercise"]
) as dag:
    task1 = PythonOperator(task_id="create_attendance", python_callable=create_attendance)
    task2 = PythonOperator(task_id="count_present",     python_callable=count_present)
    task3 = PythonOperator(task_id="count_absent",      python_callable=count_absent)
    task4 = PythonOperator(task_id="generate_summary",  python_callable=generate_summary)
    task1 >> [task2, task3] >> task4
