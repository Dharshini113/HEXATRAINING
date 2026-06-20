import pandas as pd
import numpy as np

df = pd.read_csv("expenses.csv")
print(df)

df['amount'] = df['amount'].replace('[\$,]', '', regex=True).astype(float)

df['date'] = pd.to_datetime(df['date'])

df = df.dropna(subset=['date', 'amount'])

df['month'] = df['date'].dt.to_period('M')

print(df)

monthlyexpense = df.groupby(['month', 'category'])['amount'].sum().unstack().fillna(0)
print(monthlyexpense)

print("Expenses per month based on category:")
print(df.groupby(['month', 'category'])['amount'].sum())

print("\nSummary Report:")

print("\nCount: \n",df.count())
print("\n")

print("Highest Expense:", np.max(df['amount']))
print("\nLowest Expense:", np.min(df['amount']))
print("\nAverage Expense:", np.mean(df['amount']))
print("\nTotal Expense:", np.sum(df['amount']))

print("\nmonthly_averages: \n",df.groupby('month')['amount'].mean())
print("\nmonthly_totals: \n",df.groupby('month')['amount'].sum())

print("\nExpenses per month based on category: \n",monthlyexpense)