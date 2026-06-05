#Generic Exceptions
try:
    a = 10
    b = 0
    res = a/b
    print(res)
   
except:
    print("Exception occured")
   
#Specific Exceptions

try:
    a = 10
    b = 0
    ans = a/b
    print(ans)
except ZeroDivisionError:
    print("Cannot divide by zero")
 
try:
    age = int(input("Enter Age: "))
    print(age)
except ValueError:
    print("Only numeric values")
 

# Multiple Exceptions
try:
    age = int(input("Enter Age: "))
    print(100 / age)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Age cannot be zero")


# Exception Object
try:
    num = int("abc")
except Exception as e:
    print(e)


# Else Block
try:
    num = 10
    print(num)
except:
    print("Error")
else:
    print("Success")
   
   
#finally - anything that is mandatory and can't be skipped. Eg: Closing a connection
try:
    print(10 /0)
except:
    print("Error")
finally:
    print("Connection Closed")
 

# Raise Error - manually raise an error
salary = -1000
if salary < 0:
    raise ValueError("Salary cannot be negative")
