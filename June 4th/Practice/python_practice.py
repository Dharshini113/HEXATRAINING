# print("Hello Hexaware")
# print("Python Training Started")

# customer_name="Riya sharma"
# age=28
# salary=50000
# is_active=True

# print(customer_name)
# print(age)
# print(salary)
# print(is_active)

# print(type(customer_name))
# print(type(age))
# print(type(salary))
# print(type(is_active))

# salary=35000
# if salary>50000:
#     print("High Income")
# else:
#     print("Normal Income")

# experience=5
# if salary > 50000  and experience>=3:
#     print("Eligible")
# else:
#     print("Not Eligible")


# marks=85
# if marks>=90:
#     print("Grade A")
# elif marks>=75:
#     print("Grade B")
# elif marks>=60:
#     print("Grade C")
# else:
#     print("Grade D")

# not operator
# is_blocked=False
# if not is_blocked:
#     print("Login Allowed")

# for loop
# for i in range(1,6):
#     print(i)
## whileloop
# count=1
# while count <=5:
#     print(count)
#     count+=1


# cities=["Hyderabad","Mumbai","Delhi"]
# print(cities[0])
# print(cities[1])
# print(cities[2])

# print(cities[-1])
# print(cities[-2])

# #update
# cities[1]="Bangalore"
# print(cities)

# #insert
# cities.insert(1,"pune")
# print(cities)

# #append
# cities.append("chennai")
# print(cities)

# #extend
# cities.extend(["kochi","pondichery"])
# print(cities)

# #remove
# cities.remove("pondichery")
# print(cities)

# #pop
# cities.pop()
# print(cities)

# #del
# del cities[0]
# print(cities)

# cities.clear()
# print(cities)
# print(len(cities))
 
# cities=["Hyderabad","Mumbai","Delhi","Pune"]
# print("Mumbai" in cities)
# print("Pune" in cities)

# print(cities.index("Hyderabad"))
# cities.sort()
# print(cities)

# #tuple
# cities=("Hyderabad","Mumbai","Delhi","Pune")
# print(cities)
# print(cities[0])
# print(cities[1])

# print(cities[-1])
# print(cities[-2])

# print(len(cities))
# print(cities[1:4])
# print(cities)

# cities[1]="Bangalore"
# error

# employee=(101,"Rahul",7500)
# print(employee)

# #Unpacking
# emp_id,emp_name,salary=employee
# print(emp_id)
# print(emp_name)
# print(salary)

# #multiple values
# def get_employee():
#     return 101,"Rahul",7500
# result=get_employee()
# print(result)

# #Each Row is represented as tuple
# record=(
#     101,
#     "Rahul",
#     7500
# )
# print(record)

# SET

# cities={"Hyderabad","Mumbai","Delhi","Mumbai"}
# print(cities)

# #remove duplicates from list
# # unique_cities = set(cities)
# # print(unique_cities)

# cities.add("Chennai")
# print(cities)

# cities.update(["Chennai","Delhi"])
# print(cities)

# cities.remove("Chennai")
# print(cities)

# cities.discard("Delhi") #no error when data is not present
# cities.discard("tamilnadu")
# print(cities)

# set1={1,2,3,4,5,6,7,8,9,10}
# set2={3,4,5,6,7,8,9,10,11,12}

# result=set1.union(set2)
# print(result)

# result=set1.intersection(set2)
# print(result)

# result=set1.symmetric_difference(set2)
# print(result)

# result=set1.difference(set2)
# print(result)

#dictionary 

customer={
    "customer_id":101,
    "name":"Rahul",
    "city":"hyderabad"
}
print(customer)

print(customer["name"])
print(customer["city"])

#safe
print(customer.get("name"))
print(customer.get("salary"))

#add New key value pair
customer["salary"]=75000
print(customer)

#update
customer["name"]="Rahul"
print(customer)

customer.pop("customer_id")
print(customer)

del customer["salary"]
print(customer)
