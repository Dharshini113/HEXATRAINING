import csv
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_orders():
    rows = [
        ["product",  "quantity", "price"],
        ["Laptop",   "1",        "70000"],
        ["Mouse",    "4",        "500"  ],
        ["Monitor",  "2",        "12000"],
        ["Keyboard", "3",        "1500" ],
    ]
    with open("/tmp/orders.csv", "w", newline="") as f:
        csv.writer(f).writerows(rows)
    print("orders.csv created!")

def calculate_order_value():
    revenues = {}
    with open("/tmp/orders.csv", "r") as f:
        for row in csv.DictReader(f):
            revenues[row["product"]] = int(row["quantity"]) * int(row["price"])
    total       = sum(revenues.values())
    top_product = max(revenues, key=revenues.get)
    with open("/tmp/order_calc.txt", "w") as f:
        for product, rev in revenues.items():
            f.write(f"{product}={rev}\n")
        f.write(f"TOTAL={total}\nTOP={top_product}\n")
    for product, rev in revenues.items():
        print(f"{product} = Rs.{rev:,}")
    print(f"Highest Selling Product = {top_product}")

def generate_sales_report():
    revenues = {}
    meta = {}
    with open("/tmp/order_calc.txt", "r") as f:
        for line in f:
            k, v = line.strip().split("=", 1)
            if k in ("TOTAL", "TOP"):
                meta[k] = v
            else:
                revenues[k] = int(v)
    lines = [
        "=" * 42,
        "         ONLINE SALES REPORT",
        "=" * 42,
        f"  {'Product':<15}  {'Revenue':>12}",
        "-" * 42,
    ]
    for product, rev in revenues.items():
        lines.append(f"  {product:<15}  Rs.{rev:>9,}")
    lines += [
        "-" * 42,
        f"  {'TOTAL REVENUE':<15}  Rs.{int(meta['TOTAL']):>9,}",
        f"  Top Product     : {meta['TOP']}",
        "=" * 42,
    ]
    report = "\n".join(lines)
    with open("/tmp/sales_report.txt", "w") as f:
        f.write(report)
    print("sales_report.txt generated!")
    print(report)

with DAG(
    dag_id="exercise_10_online_orders",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["exercise"]
) as dag:
    task1 = PythonOperator(task_id="create_orders",         python_callable=create_orders)
    task2 = PythonOperator(task_id="calculate_order_value", python_callable=calculate_order_value)
    task3 = PythonOperator(task_id="generate_sales_report", python_callable=generate_sales_report)
    task1 >> task2 >> task3
