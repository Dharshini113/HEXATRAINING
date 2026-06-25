from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_marks_file():
    data = "Math,80\nScience,75\nEnglish,90\nPython,95"
    with open("/tmp/marks.txt", "w") as f:
        f.write(data)
    print("marks.txt created!")

def calculate_average():
    marks = []
    with open("/tmp/marks.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                subject, mark = line.split(",")
                marks.append(int(mark))
    average = sum(marks) / len(marks)
    with open("/tmp/marks_calc.txt", "w") as f:
        f.write(f"average={average:.0f}\n")
    print(f"Average = {average:.0f}")

def generate_result():
    with open("/tmp/marks_calc.txt", "r") as f:
        average = int(f.read().strip().split("=")[1])
    result = "PASS" if average >= 50 else "FAIL"
    report = f"Average Marks = {average}\nResult = {result}"
    with open("/tmp/result.txt", "w") as f:
        f.write(report)
    print("result.txt generated!")
    print(report)

with DAG(
    dag_id="exercise_03_student_marks",
    start_date=datetime(2024, 1, 1),
    schedule="@once",
    catchup=False,
    tags=["exercise"]
) as dag:
    task1 = PythonOperator(task_id="create_marks_file", python_callable=create_marks_file)
    task2 = PythonOperator(task_id="calculate_average", python_callable=calculate_average)
    task3 = PythonOperator(task_id="generate_result",   python_callable=generate_result)
    task1 >> task2 >> task3
