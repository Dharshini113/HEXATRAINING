import csv


# print()
# with open("employees.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# print()
# with open("employees.csv","r") as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         print(row)
#     for row in reader:
#         print(row[1])

# print()
# count = 0
# with open("employees.csv","r") as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         print(row)
#     for row in reader:
#         count+=1
# print(count)


# storing rows in a list
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader) 
    employees = list(reader) 
    print(header)
    # print(employees)

# We can use employees list as many times as you want

# display all employees
for emp in employees:
    print(emp)

# display only the names
for emp in employees:
    print(emp[1])

# Total employees
count = len(employees) 
print("Total Employees:", count)

# Exercise 4
# Find highest salary.
high_sal = max(int(emp[3]) for emp in employees)
print("Highest Salary:", high_sal)

# Exercise 5
# Find lowest salary.
low_sal = min(int(emp[3]) for emp in employees)
print("Lowest Salary:", low_sal)

# Exercise 6
# Find average salary.
avg_sal = sum(int(emp[3]) for emp in employees) / len(employees)
print("Average Salary:", avg_sal)

# Exercise 7
# Find total salary payout.
tot_sal = sum(int(emp[3]) for emp in employees)
print("Total Salary:", tot_sal)

# Exercise 8
# Display Hyderabad employees.
for emp in employees:
    if emp[4] == "Hyderabad":
        print(emp)

# Exercise 9
# Display AI Engineering employees.
for emp in employees:
    if emp[2] == "AI Engineering":
        print(emp)

# Exercise 10
# Display employees earning above ₹80,000.
for emp in employees:
    if int(emp[3]) > 80000:
        print(emp)