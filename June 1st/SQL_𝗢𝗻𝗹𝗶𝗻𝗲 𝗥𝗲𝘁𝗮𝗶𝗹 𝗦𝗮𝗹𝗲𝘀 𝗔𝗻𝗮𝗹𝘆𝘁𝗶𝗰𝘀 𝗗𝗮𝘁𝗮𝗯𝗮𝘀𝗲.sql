-- Part 1 
CREATE DATABASE retail_capstone_db;

USE retail_capstone_db;

CREATE TABLE customers
(
customer_id INT PRIMARY KEY,
customer_name VARCHAR(100),
city VARCHAR(50),
state VARCHAR(50),
gender VARCHAR(10),
membership_type VARCHAR(30)
);

CREATE TABLE products
(
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2)
);

CREATE TABLE orders
(
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
order_status VARCHAR(30),
foreign key (customer_id) references customers(customer_id)
);

CREATE TABLE order_items
(
item_id INT PRIMARY KEY,
order_id INT,
product_id INT,
quantity INT,
foreign key (order_id) references orders(order_id),
foreign key(product_id) references products(product_id)
);

CREATE TABLE payments
(
payment_id INT PRIMARY KEY,
order_id INT,
payment_mode VARCHAR(30),
payment_status VARCHAR(30),
amount DECIMAL(10,2),
foreign key (order_id) references orders(order_id)
);

CREATE TABLE deliveries
(
delivery_id INT PRIMARY KEY,
order_id INT,
delivery_partner VARCHAR(50),
delivery_status VARCHAR(30),
delivery_city VARCHAR(50),
foreign key (order_id) references orders(order_id)
);

-- Part 2 
INSERT INTO customers VALUES
(1,'Arun Kumar','Chennai','Tamil Nadu','Male','Gold'),
(2,'Priya Sharma','Chennai','Tamil Nadu','Female','Silver'),
(3,'Rahul Verma','Bangalore','Karnataka','Male','Gold'),
(4,'Sneha Reddy','Hyderabad','Telangana','Female','Platinum'),
(5,'Vikram Singh','Mumbai','Maharashtra','Male','Silver'),
(6,'Anjali Mehta','Mumbai','Maharashtra','Female','Gold'),
(7,'Karthik Raj','Coimbatore','Tamil Nadu','Male','Silver'),
(8,'Divya Nair','Kochi','Kerala','Female','Gold'),
(9,'Rohit Gupta','Delhi','Delhi','Male','Platinum'),
(10,'Meera Iyer','Chennai','Tamil Nadu','Female','Gold');

INSERT INTO products VALUES
(101,'Wireless Mouse','Electronics',799.00),
(102,'Bluetooth Speaker','Electronics',2499.00),
(103,'Laptop Backpack','Accessories',1299.00),
(104,'Water Bottle','Home',499.00),
(105,'Office Chair','Furniture',5999.00),
(106,'USB Keyboard','Electronics',899.00),
(107,'Notebook Pack','Stationery',299.00),
(108,'Desk Lamp','Home',999.00),
(109,'Smart Watch','Electronics',4999.00),
(110,'Coffee Mug','Home',349.00);

INSERT INTO products VALUES
(111,'Men T-Shirt','Fashion',799.00),
(112,'Women Jeans','Fashion',1499.00);

INSERT INTO orders VALUES
(1001,1,'2025-01-05','Delivered'),
(1002,2,'2025-01-08','Delivered'),
(1003,3,'2025-01-10','Cancelled'),
(1004,4,'2025-01-12','Delivered'),
(1005,5,'2025-01-15','Pending'),
(1006,6,'2025-01-18','Delivered'),
(1007,1,'2025-01-20','Delivered'),
(1008,7,'2025-01-22','Pending'),
(1009,8,'2025-01-24','Delivered'),
(1010,9,'2025-01-25','Cancelled'),
(1011,10,'2025-01-27','Delivered'),
(1012,2,'2025-01-29','Pending'),
(1013,3,'2025-02-01','Delivered'),
(1014,5,'2025-02-03','Delivered'),
(1015,1,'2025-02-05','Pending');

INSERT INTO orders VALUES
(1016,4,'2026-02-10','Delivered');

INSERT INTO order_items VALUES
(1,1001,101,2),
(2,1001,103,1),
(3,1002,102,1),
(4,1002,104,2),
(5,1003,105,1),
(6,1004,109,1),
(7,1004,110,2),
(8,1005,106,1),
(9,1006,107,5),
(10,1006,108,1),
(11,1007,101,1),
(12,1007,109,1),
(13,1008,103,2),
(14,1009,104,3),
(15,1009,110,2),
(16,1010,102,1),
(17,1011,105,1),
(18,1012,108,2),
(19,1013,101,1),
(20,1014,106,2);

INSERT INTO payments VALUES
(501,1001,'UPI','Success',2897.00),
(502,1002,'Credit Card','Success',3497.00),
(503,1003,'Net Banking','Failed',5999.00),
(504,1004,'UPI','Success',5697.00),
(505,1005,'Debit Card','Pending',899.00),
(506,1006,'UPI','Success',2494.00),
(507,1007,'Credit Card','Success',5798.00),
(508,1008,'UPI','Pending',2598.00),
(509,1009,'Cash on Delivery','Success',2195.00),
(510,1010,'Credit Card','Failed',2499.00),
(511,1011,'Net Banking','Success',5999.00),
(512,1012,'UPI','Pending',1998.00),
(513,1013,'Debit Card','Success',799.00),
(514,1014,'UPI','Success',1798.00),
(515,1015,'Cash on Delivery','Pending',4999.00);

INSERT INTO deliveries VALUES
(701,1001,'Delhivery','Delivered','Chennai'),
(702,1002,'Blue Dart','Delivered','Chennai'),
(703,1003,'Ecom Express','Cancelled','Bangalore'),
(704,1004,'Delhivery','Delivered','Hyderabad'),
(705,1005,'Blue Dart','Pending','Mumbai'),
(706,1006,'Ecom Express','Delivered','Mumbai'),
(707,1007,'Delhivery','Delivered','Chennai'),
(708,1008,'Blue Dart','Pending','Coimbatore'),
(709,1009,'Ecom Express','Delivered','Kochi'),
(710,1010,'Delhivery','Cancelled','Delhi'),
(711,1011,'Blue Dart','Delivered','Chennai'),
(712,1012,'Ecom Express','Pending','Chennai'),
(713,1013,'Delhivery','Delivered','Bangalore'),
(714,1014,'Blue Dart','Delivered','Mumbai'),
(715,1015,'Ecom Express','Pending','Chennai');

-- Part 3
-- 1
select * from customers;

-- 2
select customer_name, city, membership_type from customers;

-- 3
select * from products order by price desc;

-- 4
select * from customers where city = 'Hyderabad';

-- 5
select * from customers where membership_type = 'Gold';

-- 6
select * from products where price between 500 and 5000;

-- 7
select * from products where category in ('Electronics' , 'Fashion');

-- 8
select * from orders where order_date > '2026-01-01';

-- 9
select * from payments where payment_mode = 'UPI';

-- 10
select * from deliveries where delivery_status = 'Pending';

-- Part 4
-- 11
select count(*) as tot_customers from customers;

-- 12
select count(*) as tot_orders from orders;

-- 13
select count(*) as tot_products from products;

-- 14
select sum(amount) as revenue from payments 
where payment_status = 'Success';

-- 15
select avg(amount) as average_payment from payments;

-- 16
select max(amount) from payments;

-- 17
select min(amount) from payments;

-- 18
select city, count(*) as count from customers group by city;

-- 19
select category , count(*) as count from products group by category;

-- 20
select order_status , count(*) as count from orders group by order_status;

-- Part 5
-- 21
select c.customer_name , o.order_id , o.order_date
from customers c
join orders o  
on c.customer_id = o.customer_id;

-- 22
select oi.order_id, p.product_name, oi.quantity, p.price
from order_items oi
join products p 
on oi.product_id = p.product_id;

-- 23
SELECT c.customer_name, p.product_name, oi.quantity, o.order_date
from customers c
join orders o on c.customer_id = o.customer_id
join order_items oi on o.order_id = oi.order_id
join products p on oi.product_id = p.product_id;

-- 24
select o.order_id, p.payment_mode, p.payment_status, p.amount
from orders o
join payments p on o.order_id = p.order_id;

-- 25
select o.order_id, d.delivery_partner, d.delivery_status
from orders o
join deliveries d on o.order_id = d.order_id;

-- 26
select c.customer_name, c.city, o.order_id, o.order_date, p.product_name, p.category,
	oi.quantity, p.price, pay.payment_status, d.delivery_status
from customers c
join orders o on c.customer_id = o.customer_id
join order_items oi on o.order_id = oi.order_id
join products p on oi.product_id = p.product_id
join payments pay on o.order_id = pay.order_id
join deliveries d on o.order_id = d.order_id;

-- Part 6
-- 27
select c.city, sum(pay.amount) as tot_revenue
from customers c
join orders o on c.customer_id = o.customer_id
join payments pay on o.order_id = pay.order_id
where pay.payment_status = 'Success'
group by c.city;

-- 28
select c.customer_name, sum(pay.amount) as tot_revenue
from customers c
join orders o on c.customer_id = o.customer_id
join payments pay on o.order_id = pay.order_id
where pay.payment_status = 'Success'
group by c.customer_name;

-- 29
select p.product_name, sum(oi.quantity) as tot_quantity
from products p
join order_items oi on p.product_id = oi.product_id
group by p.product_name;

-- 30
select p.category, sum(oi.quantity * p.price) AS revenue
from products p
join order_items oi on p.product_id = oi.product_id
group by p.category;

-- 31
select c.customer_name, count(o.order_id) AS tot_orders
from customers c
join orders o on c.customer_id = o.customer_id
group by c.customer_name;

-- 32
select c.customer_name, count(o.order_id) AS total_orders
from customers c
join orders o on c.customer_id = o.customer_id
group by c.customer_name 
having count(o.order_id) > 1;

-- 33
select p.category, sum(oi.quantity * p.price) AS revenue
from products p
join order_items oi on p.product_id = oi.product_id
group by p.category 
having sum(oi.quantity * p.price) > 10000;

-- 34
select city, count(*) as total_customers
from customers
group by city 
having count(*) > 2;

-- 35
select p.product_name, sum(oi.quantity) AS total_sold
from products p
join order_items oi on p.product_id = oi.product_id
group by p.product_name 
having sum(oi.quantity) > 3;

-- Part 7

-- 36
SELECT * from customers
where customer_id in (
    select customer_id from orders 
    );

-- 37
SELECT * from customers
where customer_id not in 
(	select customer_id from orders );

-- 38
select * from products
where product_id not in 
(	select product_id from order_items );

-- 39
select * from payments
where amount >
(    select avg(amount) from payments );

-- 40
select c.customer_name, p.amount
from customers c
join orders o on c.customer_id = o.customer_id
join payments p on o.order_id = p.order_id
where p.amount =
(	select max(amount) from payments );

-- 41
select * from products
where price >
(	select avg(price) from products );

-- 42
select distinct c.customer_name
from customers c
join orders o on c.customer_id = o.customer_id
join order_items oi on o.order_id = oi.order_id
join products p on oi.product_id = p.product_id
where p.category = 'Electronics';
-- 43
select * from orders
where order_id in
(	select order_id from payments
    where payment_status = 'Success' );

-- 44
select * from orders
where order_id in 
(	select order_id from deliveries
    where delivery_status <> 'Delivered' );

-- 45
select c.customer_name, sum(p.amount) AS tot_spending
from customers c
join orders o on c.customer_id = o.customer_id
join payments p on o.order_id = p.order_id
where p.payment_status = 'Success'
group by c.customer_id, c.customer_name 
having sum(p.amount) >
(	select avg(customer_spending) from
    (	select sum(amount) as customer_spending
        from customers c
        join orders o on c.customer_id = o.customer_id
        join payments p on o.order_id = p.order_id
        where p.payment_status = 'Success'
        group by c.customer_id
    ) avg_spend
);

-- Part 8
-- 46
select o.* 
from orders o
left join payments p 
on o.order_id = p.order_id
where p.order_id is null;

-- 47
select o.*
from orders o
left join deliveries d 
on o.order_id = d.order_id
where d.order_id is null;

-- 48
select * from payments
where amount is null or amount = 0;

-- 49
select o.order_id, o.order_status, p.payment_status, p.amount
from orders o
join payments p on o.order_id = p.order_id
where o.order_status = 'Cancelled' and p.payment_status = 'Success';

-- 50
select o.order_id, o.order_status, d.delivery_status, p.payment_status
from orders o
join deliveries d on o.order_id = d.order_id
join payments p on o.order_id = p.order_id
where d.delivery_status = 'Delivered' and p.payment_status = 'Failed';

-- 51
select oi.*
from order_items oi
left join products p on oi.product_id = p.product_id
where p.product_id is NULL;

-- 52
select o.*
from orders o
left join customers c
on o.customer_id = c.customer_id
where c.customer_id is NULL;
