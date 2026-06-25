from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_temperature_file():
    data = "Monday,34\nTuesday,36\nWednesday,31\nThursday,38\nFriday,35\nSaturday,33\nSunday,32"
    with open("/tmp/temperature.txt", "w") as f:
        f.write(data)
    print("temperature.txt created!")

def find_highest_temperature():
    readings = {}
    with open("/tmp/temperature.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                day, temp = line.split(",")
                readings[day] = int(temp)
    highest = max(readings.values())
    hot_day = max(readings, key=readings.get)
    average = sum(readings.values()) / len(readings)
    with open("/tmp/temp_calc.txt", "w") as f:
        f.write(f"highest={highest}\nhot_day={hot_day}\naverage={average:.1f}\n")
    print(f"Highest Temperature = {highest} C ({hot_day})")
    print(f"Average Temperature = {average:.1f} C")

def generate_weather_report():
    r = {}
    with open("/tmp/temp_calc.txt", "r") as f:
        for line in f:
            k, v = line.strip().split("=")
            r[k] = v
    report = (
        "=" * 40 + "\n"
        "      WEEKLY WEATHER REPORT\n"
        "=" * 40 + "\n"
        f"  Highest Temp : {r['highest']} C ({r['hot_day']})\n"
        f"  Average Temp : {r['average']} C\n"
        "=" * 40
    )
    with open("/tmp/weather_report.txt", "w") as f:
        f.write(report)
    print("weather_report.txt generated!")
    print(report)

with DAG(
    dag_id="exercise_11_temperature_analysis",
    start_date=datetime(2024, 1, 1),
    schedule="@weekly",
    catchup=False,
    tags=["exercise"]
) as dag:
    task1 = PythonOperator(task_id="create_temperature_file",  python_callable=create_temperature_file)
    task2 = PythonOperator(task_id="find_highest_temperature", python_callable=find_highest_temperature)
    task3 = PythonOperator(task_id="generate_weather_report",  python_callable=generate_weather_report)
    task1 >> task2 >> task3
