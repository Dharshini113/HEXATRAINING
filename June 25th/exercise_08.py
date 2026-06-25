from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_bill_file():
    data = "Rahul,210\nPriya,180\nAmit,300\nSneha,150\nKiran,260"
    with open("/tmp/electricity.txt", "w") as f:
        f.write(data)
    print("electricity.txt created!")

def calculate_total_units():
    units_list = []
    with open("/tmp/electricity.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                name, units = line.split(",")
                units_list.append(int(units))
    total   = sum(units_list)
    count   = len(units_list)
    average = total / count
    with open("/tmp/bill_calc.txt", "w") as f:
        f.write(f"count={count}\ntotal={total}\naverage={average:.2f}\n")
    print(f"Customers   = {count}")
    print(f"Total Units = {total}")
    print(f"Average     = {average:.2f}")

def generate_bill_summary():
    r = {}
    with open("/tmp/bill_calc.txt", "r") as f:
        for line in f:
            k, v = line.strip().split("=")
            r[k] = v
    report = (
        "=" * 40 + "\n"
        "      ELECTRICITY BILL SUMMARY\n"
        "=" * 40 + "\n"
        f"  Customers   : {r['count']}\n"
        f"  Total Units : {r['total']} kWh\n"
        f"  Avg Units   : {r['average']} kWh\n"
        "=" * 40
    )
    with open("/tmp/bill_summary.txt", "w") as f:
        f.write(report)
    print("bill_summary.txt generated!")
    print(report)

with DAG(
    dag_id="exercise_08_electricity_bill",
    start_date=datetime(2024, 1, 1),
    schedule="@monthly",
    catchup=False,
    tags=["exercise"]
) as dag:
    task1 = PythonOperator(task_id="create_bill_file",      python_callable=create_bill_file)
    task2 = PythonOperator(task_id="calculate_total_units", python_callable=calculate_total_units)
    task3 = PythonOperator(task_id="generate_bill_summary", python_callable=generate_bill_summary)
    task1 >> task2 >> task3
