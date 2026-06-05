
# 1
with open("employees.txt", "r") as file:
    print(file.read())

# 2
with open("employees.txt", "r") as file:
    for line in file:
        print(line.strip())

# storing employee as list to access through out the file
with open("employees.txt", "r") as file:
    employees = [line.strip().split(",") for line in file]

# 3
print("Total Employees:", len(employees))

# 4
for emp in employees:
    print(emp[1])

# 5
for emp in employees:
    if emp[4] == "Hyderabad":
        print(emp)

# 6
for emp in employees:
    if emp[4] == "Bangalore":
        print(emp)

# 7
for emp in employees:
    if int(emp[3]) > 80000:
        print(emp)

# 8

# highest = 0
# for emp in employees:
#     if int(emp[3]) > highest:
#         highest = int(emp[3])
# print("Highest Salary:", highest)

high_sal = max(int(emp[3]) for emp in employees)
print("Highest Salary:", high_sal)

# 9

# lowest = int(employees[0][3])
# for emp in employees:
#     if int(emp[3]) < lowest:
#         lowest = int(emp[3])
# print("Lowest Salary:", lowest)

low_sal = min(int(emp[3]) for emp in employees)
print("Lowest Salary:", low_sal)

# 10

# avg = 0
# for emp in employees:
#     avg+= int(emp[3])
# print("Average Salary:", avg/len(employees))

avg_sal = sum(int(emp[3]) for emp in employees) / len(employees)
print("Average Salary:", avg_sal)

# 11

# tot_sum = 0
# for emp in employees:
#     tot_sum+= int(emp[3])
# print("Total Salary:", tot_sum)

tot_sal = sum(int(emp[3]) for emp in employees)
print("Total Salary:", tot_sal)

# 12
cnt = 0
for emp in employees:
    if emp[2] == "AI Engineering":
        cnt+=1
print("AI Engineering:", cnt)

# using sum()
# count = sum(1 for emp in employees if emp[2] == "AI Engineering")
# print("AI Engineering:", count)

# 13
cnt = 0

for emp in employees:
    if emp[2] == "Data Engineering":
        cnt+=1
print("Data Engineering:", cnt)

# using sum()
# count = sum(1 for emp in employees if emp[2] == "Data Engineering")
# print("Data Engineering:", count)

# count = sum(emp[2] == "Data Engineering" for emp in employees)  # emp[2] == "Data Engineering"  true = 1 , false  0
# print(count)

# 14
for emp in employees:
    if emp[2] == "AI Engineering":
        print(emp)

# 15
with open("high_salary_employees.txt", "w") as file:
    for emp in employees:
        if int(emp[3]) > 80000:
            file.write(",".join(emp) + "\n")

# 16
with open("hyderabad_employees.txt", "w") as file:
    for emp in employees:
        if emp[4] == "Hyderabad":
            file.write(",".join(emp) + "\n")

# 17
cities = set(emp[4] for emp in employees)
for city in cities:
    print(city)
print("Count:", len(cities))

# 18
ai=0
de=0
ds=0
ce = 0
for emp in employees:
    if emp[2] == "AI Engineering":
        ai+=1
    elif emp[2] == "Data Engineering":
        de+=1
    elif emp[2] == "Data Science":
        ds+=1
    elif emp[2] == "Cloud Engineering":
        ce+=1
print("AI Engineering =", ai)
print("Data Engineering =", de)
print("Data Science =", ds)
print("Cloud Engineering =", ce)

# 19
highest = 0
employee =''
for emp in employees:
    if int(emp[3]) > highest:
        highest = int(emp[3])
        employee = emp[1]

print("Employee with Highest Salary:")
print(employee)
print(highest)

# 20

with open("employee_report.txt", "w") as file:
    file.write(f"Total Employees: {len(employees)}\n")
    file.write(f"Highest Salary: {high_sal}\n")
    file.write(f"Lowest Salary: {low_sal}\n")
    file.write(f"Average Salary: {avg_sal}\n")
    file.write(f"Total Salary: {tot_sal}\n")
