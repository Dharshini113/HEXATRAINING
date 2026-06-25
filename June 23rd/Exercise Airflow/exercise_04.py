from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_inventory():
    data = "Rice,50\nOil,7\nSoap,35\nSugar,10\nTea,5"
    with open("/tmp/inventory.txt", "w") as f:
        f.write(data)
    print("inventory.txt created!")

def find_low_stock():
    low_stock = []
    with open("/tmp/inventory.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                product, stock = line.split(",")
                if int(stock) < 15:
                    low_stock.append(product)
                    print(f"LOW STOCK: {product} = {stock}")
    with open("/tmp/low_stock.txt", "w") as f:
        f.write("\n".join(low_stock))
    print(f"Total low stock items = {len(low_stock)}")

def generate_alert():
    with open("/tmp/low_stock.txt", "r") as f:
        items = f.read().strip()
    with open("/tmp/alerts.txt", "w") as f:
        f.write(items)
    print("alerts.txt generated!")
    print(items)

with DAG(
    dag_id="exercise_04_stock_alert",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["exercise"]
) as dag:
    task1 = PythonOperator(task_id="create_inventory", python_callable=create_inventory)
    task2 = PythonOperator(task_id="find_low_stock",   python_callable=find_low_stock)
    task3 = PythonOperator(task_id="generate_alert",   python_callable=generate_alert)
    task1 >> task2 >> task3
