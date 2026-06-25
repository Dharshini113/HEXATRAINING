from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_result_file():
    data = "Rahul,Pass\nPriya,Fail\nAmit,Pass\nSneha,Pass\nKiran,Fail\nMegha,Pass"
    with open("/tmp/results.txt", "w") as f:
        f.write(data)
    print("results.txt created!")

def count_pass_fail():
    passed = 0
    failed = 0
    with open("/tmp/results.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                name, result = line.split(",")
                if result == "Pass":
                    passed += 1
                else:
                    failed += 1
    with open("/tmp/result_calc.txt", "w") as f:
        f.write(f"total={passed + failed}\npass={passed}\nfail={failed}\n")
    print(f"Total Pass = {passed}")
    print(f"Total Fail = {failed}")

def generate_result_summary():
    r = {}
    with open("/tmp/result_calc.txt", "r") as f:
        for line in f:
            k, v = line.strip().split("=")
            r[k] = int(v)
    report = (
        "=" * 40 + "\n"
        "        EXAM RESULT SUMMARY\n"
        "=" * 40 + "\n"
        f"  Total Students : {r['total']}\n"
        f"  Passed         : {r['pass']}\n"
        f"  Failed         : {r['fail']}\n"
        "=" * 40
    )
    with open("/tmp/result_summary.txt", "w") as f:
        f.write(report)
    print("result_summary.txt generated!")
    print(report)

with DAG(
    dag_id="exercise_09_exam_results",
    start_date=datetime(2024, 1, 1),
    schedule="@once",
    catchup=False,
    tags=["exercise"]
) as dag:
    task1 = PythonOperator(task_id="create_result_file",      python_callable=create_result_file)
    task2 = PythonOperator(task_id="count_pass_fail",         python_callable=count_pass_fail)
    task3 = PythonOperator(task_id="generate_result_summary", python_callable=generate_result_summary)
    task1 >> task2 >> task3
