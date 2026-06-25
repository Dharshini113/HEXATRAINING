from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_transactions():
    data = "Deposit,10000\nWithdraw,2500\nDeposit,4000\nWithdraw,1500\nDeposit,2000"
    with open("/tmp/transactions.txt", "w") as f:
        f.write(data)
    print("transactions.txt created!")

def calculate_balance():
    deposit  = 0
    withdraw = 0
    with open("/tmp/transactions.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                txn_type, amount = line.split(",")
                if txn_type == "Deposit":
                    deposit += int(amount)
                elif txn_type == "Withdraw":
                    withdraw += int(amount)
    balance = deposit - withdraw
    with open("/tmp/balance_calc.txt", "w") as f:
        f.write(f"deposit={deposit}\nwithdrawal={withdraw}\nbalance={balance}\n")
    print(f"Total Deposit    = Rs.{deposit:,}")
    print(f"Total Withdrawal = Rs.{withdraw:,}")
    print(f"Final Balance    = Rs.{balance:,}")

def generate_account_report():
    r = {}
    with open("/tmp/balance_calc.txt", "r") as f:
        for line in f:
            k, v = line.strip().split("=")
            r[k] = int(v)
    report = (
        "=" * 40 + "\n"
        "    BANK ACCOUNT SUMMARY REPORT\n"
        "=" * 40 + "\n"
        f"  Total Deposit    : Rs.{r['deposit']:,}\n"
        f"  Total Withdrawal : Rs.{r['withdrawal']:,}\n"
        "  " + "-" * 36 + "\n"
        f"  Final Balance    : Rs.{r['balance']:,}\n"
        "=" * 40
    )
    with open("/tmp/account_report.txt", "w") as f:
        f.write(report)
    print("account_report.txt generated!")
    print(report)

with DAG(
    dag_id="exercise_12_bank_transactions",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["exercise"]
) as dag:
    task1 = PythonOperator(task_id="create_transactions",     python_callable=create_transactions)
    task2 = PythonOperator(task_id="calculate_balance",       python_callable=calculate_balance)
    task3 = PythonOperator(task_id="generate_account_report", python_callable=generate_account_report)
    task1 >> task2 >> task3
