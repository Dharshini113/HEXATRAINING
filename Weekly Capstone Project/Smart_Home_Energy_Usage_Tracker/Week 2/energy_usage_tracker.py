import pandas as pd
import numpy as np

df = pd.read_csv("energy_usage.csv")
print(df)

df['energy_kwh'] = pd.to_numeric(df['energy_kwh'], errors='coerce')

df['timestamp'] = pd.to_datetime(df['timestamp'])

df = df.dropna(subset=['timestamp', 'energy_kwh'])

df['month'] = df['timestamp'].dt.to_period('M')

print(df)

monthlydevice = df.groupby(['month', 'device_name'])['energy_kwh'].sum().unstack().fillna(0)
print(monthlydevice)

print("Energy usage per month based on device:")
print(df.groupby(['month', 'device_name'])['energy_kwh'].sum())

print("\nSummary Report:")

print("\nCount: \n", df.count())
print("\n")

print("Highest Energy Reading:", np.max(df['energy_kwh']))
print("\nLowest Energy Reading:", np.min(df['energy_kwh']))
print("\nAverage Energy Reading:", np.mean(df['energy_kwh']))
print("\nTotal Energy Consumed:", np.sum(df['energy_kwh']))

print("\nmonthly_averages: \n", df.groupby('month')['energy_kwh'].mean())
print("\nmonthly_totals: \n", df.groupby('month')['energy_kwh'].sum())

print("\nroom_totals: \n", df.groupby('room_id')['energy_kwh'].sum())

room_summary = df.groupby('room_id')['energy_kwh'].agg(
    total_kwh='sum',
    avg_kwh='mean',
    reading_count='count'
).reset_index()

print("\nRoom-Level Summary (Pandas):\n", room_summary)

print("\nEnergy usage per month based on device: \n", monthlydevice)

room_summary.to_csv("room_summary.csv", index=False)