salaries = [45000, 55000, 65000, 75000, 85000]

# 1
print(salaries)

# 2
print("Maximum Salary: ",max(salaries))

print("Minimum salary: ",min(salaries))

# 3
print("Total salary: ",sum(salaries))

# 4
print("Average salary: ",sum(salaries)/len(salaries))

# 5
salaries.append(95000)
salaries.append(105000)

print(salaries)

# 6
salaries.remove(55000)
print(salaries)

# 7
salaries.sort()
print(salaries)

# 8
salaries.sort(reverse=True)
print(salaries)

# 9
print(salaries[1])

# 10
# result = [num for num in salaries if num > 70000]
# print(result)
print([num for num in salaries if num > 70000])
