employees = [
{ "id": 101, "name": "Rahul", "department": "IT", "salary": 50000 },
{ "id": 102, "name": "Priya", "department": "HR", "salary": 70000 },
{ "id": 103, "name": "Amit", "department": "IT", "salary": 60000 },
{ "id": 104, "name": "Sneha", "department": "Finance", "salary": 80000 },
{ "id": 105, "name": "Farhan", "department": "IT", "salary": 90000 } ]

# 29
for emp in employees:
    print(emp["name"])

# 30
for emp in employees:
    if emp["department"] == "IT":
        print(emp)

# 31
highest = max(employees, key=lambda emp: emp["salary"])
print(highest)

# 32
lowest = min(employees, key=lambda emp: emp["salary"])
print(lowest)

# 33
total = sum(emp["salary"] for emp in employees)
average = total / len(employees)
print("Average Salary:", average)

# 34
total = sum(emp["salary"] for emp in employees)
print("Total Salary Payout:", total)

# 35
for emp in employees:
    if emp["salary"] > 70000:
        print(emp)

# 36
count = 0

for emp in employees:
    if emp["department"] == "IT":
        count += 1
print("IT Employees:", count)

# 37
sorted_employees = sorted(
    employees,
    key=lambda emp: emp["salary"],
    reverse=True
)
for emp in sorted_employees:
    print(emp["name"], emp["salary"])

 # 38
sorted_employees = sorted(
    employees,
    key=lambda emp: emp["salary"],
    reverse=True
)
print("Second Highest Salary Employee:")
print(sorted_employees[1])

# 39
print(set(emp["department"] for emp in employees))