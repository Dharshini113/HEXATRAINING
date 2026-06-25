import csv
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_csv():
    rows = [
        ["product",  "quantity", "price"],
        ["Laptop",   "2",        "70000"],
        ["Mouse",    "5",        "500"  ],
        ["Keyboard", "3",        "1200" ],
    ]
    with open("/tmp/sales.csv", "w", newline="") as f:
        csv.writer(f).writerows(rows)
    print("sales.csv created!")

def read_csv():
    with open("/tmp/sales.csv", "r") as f:
        reader = csv.DictReader(f)
        print("CSV Contents:")
        for row in reader:
            print(f"  {row['product']} | qty: {row['quantity']} | price: {row['price']}")

def calculate_revenue():
    revenues = {}
    with open("/tmp/sales.csv", "r") as f:
        for row in csv.DictReader(f):
            revenue = int(row["quantity"]) * int(row["price"])
            revenues[row["product"]] = revenue
            print(f"{row['product']} = {revenue}")
    total = sum(revenues.values())
    print(f"Total Revenue = {total}")
    with open("/tmp/revenue_calc.txt", "w") as f:
        for product, rev in revenues.items():
            f.write(f"{product}={rev}\n")
        f.write(f"TOTAL={total}\n")

def create_summary():
    revenues = {}
    total = 0
    with open("/tmp/revenue_calc.txt", "r") as f:
        for line in f:
            k, v = line.strip().split("=", 1)
            if k == "TOTAL":
                total = int(v)
            else:
                revenues[k] = int(v)
    lines = ["=" * 38, "        CSV SALES SUMMARY", "=" * 38]
    for product, rev in revenues.items():
        lines.append(f"  {product:<12} = {rev:,}")
    lines += ["-" * 38, f"  Total Revenue = {total:,}", "=" * 38]
    report = "\n".join(lines)
    with open("/tmp/summary.txt", "w") as f:
        f.write(report)
    print("summary.txt generated!")
    print(report)

with DAG(
    dag_id="exercise_06_csv_processing",
    start_date=datetime(2024, 1, 1),
    schedule="@once",
    catchup=False,
    tags=["exercise"]
) as dag:
    task1 = PythonOperator(task_id="create_csv",        python_callable=create_csv)
    task2 = PythonOperator(task_id="read_csv",          python_callable=read_csv)
    task3 = PythonOperator(task_id="calculate_revenue", python_callable=calculate_revenue)
    task4 = PythonOperator(task_id="create_summary",    python_callable=create_summary)
    task1 >> task2 >> task3 >> task4
