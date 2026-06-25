from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_enrollment_file():
    data = "Python,Rahul\nPython,Priya\nSQL,Amit\nPython,Sneha\nPower BI,Kiran\nSQL,Megha\nPower BI,Arjun"
    with open("/tmp/enrollments.txt", "w") as f:
        f.write(data)
    print("enrollments.txt created!")

def count_students():
    course_count = {}
    with open("/tmp/enrollments.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                course, student = line.split(",")
                course_count[course] = course_count.get(course, 0) + 1
    with open("/tmp/enrollment_calc.txt", "w") as f:
        for course, count in course_count.items():
            f.write(f"{course}={count}\n")
    for course, count in course_count.items():
        print(f"{course} = {count}")

def generate_course_report():
    course_count = {}
    with open("/tmp/enrollment_calc.txt", "r") as f:
        for line in f:
            course, count = line.strip().split("=")
            course_count[course] = int(count)
    total      = sum(course_count.values())
    top_course = max(course_count, key=course_count.get)
    lines = [
        "=" * 42,
        "      COURSE ENROLLMENT REPORT",
        "=" * 42,
        f"  {'Course':<15}  {'Students':>8}",
        "-" * 42,
    ]
    for course, count in course_count.items():
        lines.append(f"  {course:<15}  {count:>8}")
    lines += [
        "-" * 42,
        f"  Total Students : {total}",
        f"  Most Popular   : {top_course}",
        "=" * 42,
    ]
    report = "\n".join(lines)
    with open("/tmp/course_report.txt", "w") as f:
        f.write(report)
    print("course_report.txt generated!")
    print(report)

with DAG(
    dag_id="exercise_14_course_enrollment",
    start_date=datetime(2024, 1, 1),
    schedule="@weekly",
    catchup=False,
    tags=["exercise"]
) as dag:
    task1 = PythonOperator(task_id="create_enrollment_file", python_callable=create_enrollment_file)
    task2 = PythonOperator(task_id="count_students",         python_callable=count_students)
    task3 = PythonOperator(task_id="generate_course_report", python_callable=generate_course_report)
    task1 >> task2 >> task3
