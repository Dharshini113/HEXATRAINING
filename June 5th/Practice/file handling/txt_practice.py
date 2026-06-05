
#File operations

# read file
file = open("employees.txt", "r")
data = file.read()
print(data)
file.close()

#read single line
file = open("employees.txt", "r")
print(file.readline())
file.close()

#multiple lines
file = open("employees.txt", "r")
lines = file.readlines()
print(lines)
file.close()

#Automatic closing
with open("employees.txt", "r") as file:
    data = file.read()
    print(data)

# #write to file - overwrites existing content
with open("employees1.txt","w")as file:
    file.write("John - Manager\n")
    file.write("Sara - Developer\n")
    file.write("Mike - Designer\n")


# #append to file - adds to existing content
with open("employees1.txt","a")as file:
    file.write("Emily - Analyst\n")
    file.write("David - Tester\n")