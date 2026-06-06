import csv

# # created orders list and stored the data from csv file

# 1 - read
with open("orders.csv", "r") as file:
    reader = csv.reader(file)  
    header = next(reader) 
    orders = list(reader)  # storing the orders in list
    # print(header)
    # print(orders)

# 2 - display all orders
for ord in orders:
    print(ord)

# 3 - Total orders
count = len(orders) 
print("Total orders:", count)

# 4
tot_rev = sum(int(ord[5])*int(ord[6]) for ord in orders)
print("Total revenue:", tot_rev)

# 5
highest = 0
for ord in orders:
    if highest < (int(ord[5])*int(ord[6])):
        highest = int(ord[5])*int(ord[6])
print("Highest order value: ",highest)

# 6
lowest = int(orders[0][5]) * int(orders[0][6])
for ord in orders:
    if lowest > (int(ord[5])*int(ord[6])):
        lowest = int(ord[5])*int(ord[6])
print("lowest order value: ",lowest)

# 7
print("Average order value: ",tot_rev/len(orders))

# 8
customers = set()
for ord in orders:
    customers.add(ord[1])
print(customers)

# 9
print("Unique Customers:", len(customers))

# 10
customer_purchase = {}
for ord in orders:
    customer = ord[1]
    rev = int(ord[5]) * int(ord[6])
    if customer in customer_purchase:
        customer_purchase[customer] += rev
    else:
        customer_purchase[customer] = rev
top = max(customer_purchase, key=customer_purchase.get)
print("Customer with highest purchase:", top)

# 11
product_cnt = {}
for ord in orders:
    product = ord[3]
    if product in product_cnt:
        product_cnt[product] += 1
    else:
        product_cnt[product] = 1
print(product_cnt)

# 12
product_rev = {}
for ord in orders:
    product = ord[3]
    rev = int(ord[5]) * int(ord[6])
    if product in product_rev:
        product_rev[product] += rev
    else:
        product_rev[product] = rev
print(product_rev)

# 13
quantity = {}
for ord in orders:
    product = ord[3]
    qty = int(ord[5])
    if product in quantity:
        quantity[product] += qty
    else:
        quantity[product] = qty
most = max(quantity, key=quantity.get)
print("Most sold:", most)

# 14
least = min(quantity, key=quantity.get)
print("Least sold:", least)

# 15
category_rev = {}
for ord in orders:
    category = ord[4]
    rev = int(ord[5]) * int(ord[6])
    if category in category_rev:
        category_rev[category] += rev
    else:
        category_rev[category] = rev
print(category_rev)

# 16
city_orders = {}
for ord in orders:
    city = ord[2]
    if city in city_orders:
        city_orders[city] += 1
    else:
        city_orders[city] = 1
print(city_orders)

# 17 
city_rev = {}
for ord in orders:
    city = ord[2]
    rev = int(ord[5]) * int(ord[6])
    if city in city_rev:
        city_rev[city] += rev
    else:
        city_rev[city] = rev
print(city_rev)

# 18
city = max(city_rev, key=city_rev.get)
print("Highest revenue city:", city)

# 19
products = []
for ord in orders:
    products.append(ord[3])
products.sort()
print(products)

# 20
cities = set()
for ord in orders:
    cities.add(ord[2])
print(cities)

# 21 
print(city_rev)

# 22
quantity = {}
for ord in orders:
    product = ord[3]
    qty = int(ord[5])
    if product in quantity:
        quantity[product] += qty
    else:
        quantity[product] = qty
print(quantity)

# 23 
def total_rev():
    tot = 0
    for ord in orders:
        tot += int(ord[5]) * int(ord[6])
    return tot
print(total_rev())

# 24 
def top_product():
    return max(quantity, key=quantity.get)
print(top_product())

# 25 
def top_city():
    return max(city_rev, key=city_rev.get)
print(top_city())

# 26 
def average_value():
    return total_rev() / len(orders)
print(average_value())

# 27
try:
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        orders = list(reader)
        print(orders)
except FileNotFoundError:
    print("File not found!")

# 28
valid_ord = []
for ord in orders:
    try:
        qty = int(ord[5])
        valid_ord.append(ord)
    except ValueError:
        print("Invalid quantity:", ord)
# 29
valid_ord = []
for ord in orders:
    try:
        price = int(ord[6])
        valid_ord.append(ord)
    except ValueError:
        print("Invalid price:", ord)

import numpy as np

order_val = []
for ord in orders:
    rev = int(ord[5]) * int(ord[6])
    order_val.append(rev)
order_val = np.array(order_val)

# 30
print("Total Revenue:", np.sum(order_val))
print("Average Revenue:", np.mean(order_val))
print("Maximum Revenue:", np.max(order_val))
print("Minimum Revenue:", np.min(order_val))
print("Standard Deviation:", np.std(order_val))

import pandas as pd

# 31
df = pd.read_csv("orders.csv")
print(df)

# 32
df["Revenue"] = df["quantity"] * df["price"]
print(df)

# 33
top = df.sort_values(by="Revenue", ascending=False)
print(top.head())

# 34
city_rev_pd = df.groupby("city")["Revenue"].sum()
print(city_rev_pd)

# 35
product_rev = df.groupby("product")["Revenue"].sum()
print(product_rev)

# 36
top_products = df.groupby("product")["quantity"].sum()
top_products = top_products.sort_values(ascending=False)
print(top_products)

# 37
city_count = df.groupby("city")["order_id"].count()
print(city_count)

# Report
with open("sales_summary_report.txt", "w") as file:

    file.write("SALES SUMMARY REPORT\n\n")
    file.write(f"Total Orders: {len(orders)}\n")
    file.write(f"Total Revenue: {tot_rev}\n")
    file.write(f"Average Order Value: {tot_rev/len(orders)}\n")
    file.write(f"Highest Order Value: {highest}\n")
    file.write(f"Lowest Order Value: {lowest}\n")

    file.write("\nRevenue By City\n")
    file.write(str(city_rev))

    file.write("\n\nRevenue By Category\n")
    file.write(str(category_rev))

    file.write("\n\nTop Selling Product\n")
    file.write(str(top_product()))

    file.write("\n\nTop Revenue City\n")
    file.write(str(top_city()))
print("Report Generated")

# 38
high_value = df[df["Revenue"] > 50000]
high_value.to_csv("high_value_orders.csv", index=False)
print("high_value_orders.csv created")

# 39
electronics = df[df["category"] == "Electronics"]
electronics.to_csv("electronics_orders.csv", index=False)
print("electronics_orders.csv created")

# 40
while True:

    print("\n1. View Orders")
    print("2. Revenue Analysis")
    print("3. Product Analysis")
    print("4. City Analysis")
    print("5. Export Reports")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for ord in orders:
            print(ord)

    elif choice == "2":
        print("Total Revenue:", tot_rev)
        print("Highest Order:", highest)
        print("Lowest Order:", lowest)

    elif choice == "3":
        print("Most Sold:", most)
        print("Least Sold:", least)
        print(product_rev)

    elif choice == "4":
        # print(city_rev)
        print("Orders By City:", city_orders)
        print("Revenue By City:", city_rev)
        print("Top City:", top_city())

    elif choice == "5":
        high_value.to_csv("high_value_orders.csv", index=False)
        electronics.to_csv("electronics_orders.csv", index=False)
        print("Reports Exported")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")