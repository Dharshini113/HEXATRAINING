import pandas as pd

# data = {

#     "employee_id": [101,102,103],

#     "name": [
#         "Rahul",
#         "Priya",
#         "Amit"
#     ],

#     "salary": [
#         75000,
#         85000,
#         65000
#     ]
# }

# df = pd.DataFrame(data)
# print(df)

df = pd.read_csv(
    "file handling\\employees.csv"
)

# Prints all rows and columns
print(df)

# Shows the first 5 rows by default.
print(df.head())

# shoes the first 2 rows
print(df.head(2))

# Shows the last 5 rows by default
print(df.tail())
# shows the last 3 rows
print(df.tail(3))

# Displays the data type of each column
print(df.dtypes)

# Provides a summary
print(df.info())

# Generates statistical summary
print(df.describe()) # statistics

print(df["name"])

print( df[["name","salary"]] )