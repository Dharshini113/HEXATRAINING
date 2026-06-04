employee_info = {
    "employee_id": 101,
    "name": "Rahul Sharma",
    "department": "Data Engineering",
    "salary": 75000,
    "city": "Hyderabad"
}

# 21
print("name:", employee_info["name"])

# 22
print("Department:", employee_info["department"])
print("City:", employee_info["city"])

# 23
employee_info["experience"] = 5
print(employee_info)

# 24
employee_info["salary"] = 85000
print(employee_info)

# 25
employee_info.pop("city")
print(employee_info)

# 26
print(employee_info.keys())

# 27
print(employee_info.values())

# 28
print(employee_info.items())