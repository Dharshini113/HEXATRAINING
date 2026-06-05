import json

# employees = [

#     {
#         "employee_id": 101,
#         "name": "Rahul Sharma",
#         "department": "Data Engineering",
#         "salary": 75000,
#         "city": "Hyderabad"
#     },

#     {
#         "employee_id": 102,
#         "name": "Priya Reddy",
#         "department": "AI Engineering",
#         "salary": 85000,
#         "city": "Bangalore"
#     },

#     {
#         "employee_id": 103,
#         "name": "Amit Kumar",
#         "department": "Data Engineering",
#         "salary": 65000,
#         "city": "Mumbai"
#     },

#     {
#         "employee_id": 104,
#         "name": "Sneha Patel",
#         "department": "Data Science",
#         "salary": 95000,
#         "city": "Chennai"
#     },

#     {
#         "employee_id": 105,
#         "name": "Farhan Ali",
#         "department": "Cloud Engineering",
#         "salary": 80000,
#         "city": "Delhi"
#     }

# ]

# with open("employees.json","w") as file:
#     json.dump(employees,file,indent=4)

# print("JSON file created successsfully")

with open("employees.json","r") as file:
    employees = json.load(file)

# print all the employees
print(employees) 

for emp in employees:
    print(emp)

# print only the names
for emp in employees:
    print(emp["name"]) 

# to finf the length of employees
print(len(employees))

# to find highest salary
# highest = 0
# for emp in employees:
#     if emp["salary"] > highest:
#         highest = emp["salary"]
# print("Highest Salary:", highest)

highest = max(emp["salary"] for emp in employees)
print("Highest Salary:", highest)

# to find average salary

# avg = 0
# for emp in employees:
#     avg+= emp["salary"]
# print("Average Salary:", avg/len(employees))

average = sum(emp["salary"] for emp in employees) / len(employees)
print("Average Salary:", average)

# Display Data Engineering Employees
for emp in employees:
    if emp["department"] == "Data Engineering":
        print(emp)

# Display Employees Earning More Than 80000
for emp in employees:
    if emp["salary"] > 80000:
        print(emp["name"])

# Update Salary of one of employees
for emp in employees:
    if emp["employee_id"] == 103:
        emp["salary"] = 70000
        break
print("Salary updated successfully")

# Add New Employee
new_employee = {
    "employee_id": 106,
    "name": "Kiran Kumar",
    "department": "Data Science",
    "salary": 90000,
    "city": "Pune"
}

employees.append(new_employee)
print("Employee added successfully")

# Delete an Employee
for emp in employees:
    if emp["employee_id"] == 104:
        employees.remove(emp)
        break

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)
print("Changes saved successfully")