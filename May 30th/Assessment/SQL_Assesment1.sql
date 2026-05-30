CREATE DATABASE training_sql_db;

USE training_sql_db;

CREATE TABLE books
(
book_id INT PRIMARY KEY,
book_title VARCHAR(100),
category VARCHAR(50),
author VARCHAR(50),
price DECIMAL(10,2),
stock INT,
published_year INT
);

INSERT INTO books VALUES
(1, 'Python Basics', 'Programming', 'Ravi Kumar', 550, 30, 2021),
(2, 'Advanced SQL', 'Database', 'Priya Sharma', 750, 15, 2020),
(3, 'Data Engineering Guide', 'Data', 'Amit Verma', 1200, 10, 2023),
(4, 'Machine Learning Start', 'AI', 'Neha Reddy', 950, 8, 2022),
(5, 'Excel for Business', 'Business', 'Kiran Rao', 400, 50, 2019),
(6, 'Power BI Reports', 'Data', 'Sneha Patel', 850, 12, 2021),
(7, 'Java Fundamentals', 'Programming', 'Arjun Mehta', 600, 20, 2018),
(8, 'Cloud Basics', 'Cloud', 'Rahul Nair', 700, 18, 2022),
(9, 'SQL Interview Prep', 'Database', 'Farhan Ali', 500, 25, 2024),
(10, 'AI for Beginners', 'AI', 'Meera Singh', 650, 5, 2023);

-- Exercise 1
select * from books;

-- Exercise 2
select book_title , category,price from books;

-- Exercise 3
select distinct category from books;

-- Exercise 4
select * from books where category = 'Programming';

-- Exercise 5
select * from books where price>700;

-- Exercise 6
select * from books where stock < 15;

-- Exercise 7
select * from books where category in ('Programming','Database','AI');

-- Exercise 8
select * from books where price > 500 and price < 800;
select * from books where price between 500 and 900;

-- Exercise 9
select * from books where book_title like '%SQL%' ;

-- Exercise 10
select * from books where book_title like 'Data%';

-- Exercise 11
select * from books order by price desc;

-- Exercise 12
select * from books order by category asc, price desc;

-- Exercise 13
select count(*) as total_books from books;

-- Exercise 14
select max(price) as highest_price from books;

-- Exercise 15
select min(price) as lowest_price from books;

-- Exercise 16
select avg(price) as avg_price from books;

-- Exercise 17
select sum(stock) as total_stock from books;

-- Exercise 18
select category ,count(*) as count from books group by category;

-- Exercise 19
select category ,avg(price) from books group by category;

-- Exercise 20
select category ,sum(stock) as tot_stock from books group by category;

-- Exercise 21
select category , count(*) as count from books group by category having count(*)>1;

-- Exercise 22
select category , avg(price) as avg_price from books group by category having avg(price) > 700;

CREATE TABLE departments
(
department_id INT PRIMARY KEY,
department_name VARCHAR(50),
location VARCHAR(50)
);

CREATE TABLE employees
(
employee_id INT PRIMARY KEY,
employee_name VARCHAR(50),
department_id INT,
salary DECIMAL(10,2),
city VARCHAR(50),
manager_id INT
);

INSERT INTO departments VALUES
(10, 'IT', 'Hyderabad'),
(20, 'HR', 'Bangalore'),
(30, 'Finance', 'Mumbai'),
(40, 'Sales', 'Delhi'),
(50, 'Marketing', NULL);

INSERT INTO employees VALUES
(101, 'Rahul Sharma', 10, 75000, 'Hyderabad', 201),
(102, 'Priya Reddy', 10, 85000, 'Bangalore', 201),
(103, 'Amit Kumar', 20, 55000, NULL, 202),
(104, 'Sneha Patel', 30, 65000, 'Mumbai', 203),
(105, 'Arjun Verma', NULL, 60000, 'Chennai', 204),
(106, 'Neha Singh', 60, 50000, 'Delhi', NULL),
(107, 'Farhan Ali', 40, NULL, 'Hyderabad', 205),
(108, 'Meera Nair', 10, 90000, 'Pune', 201);

-- Exercise 23
select 
	e.employee_name,
    e.salary,
    d.department_name,
    d.location
from employees e 
inner join departments d
on e.department_id = d.department_id;
    
-- Exercise 24
select * from employees e 
left join departments d
on e.department_id = d.department_id;

-- Exercise 25
select e.employee_name from employees e
left join departments d
on e.department_id = d.department_id
where d.department_id is null;

-- Exercise 26
select * from employees e 
right join departments d
on e.department_id = d.department_id;

-- Exercise 27
select d.department_name
from employees e 
right join departments d
on d.department_id = e.department_id
WHERE e.employee_id IS NULL;

-- Exercise 28
select employee_name from employees
where salary is null;

-- Exercise 29
select employee_name from employees
where city is null;

-- Exercise 30
select department_name from departments
where location is null;

-- Exercise 31
select d.department_name , count(e.employee_id) as count
from employees e
right join departments d 
on d.department_id = e.department_id
group by d.department_id;

-- Exercise 32
select d.department_name , avg(e.salary) as average
from employees e
right join departments d 
on d.department_id = e.department_id
group by d.department_name;

-- Exercise 33
select d.department_name , count(e.employee_id) as count
from employees e
right join departments d 
on d.department_id = e.department_id
group by d.department_name
having count(e.employee_id) > 2;

-- Exercise 34
select d.department_name , max(e.salary) as highest_salary
from employees e
right join departments d 
on d.department_id = e.department_id
group by d.department_name;

CREATE TABLE customers_new
(
customer_id INT PRIMARY KEY,
customer_name VARCHAR(50),
city VARCHAR(50),
membership_type VARCHAR(30)
);

CREATE TABLE payments
(
payment_id INT PRIMARY KEY,
customer_id INT,
amount DECIMAL(10,2),
payment_mode VARCHAR(30),
payment_status VARCHAR(30)
);

INSERT INTO customers_new VALUES
(1, 'Ramesh Gupta', 'Hyderabad', 'Gold'),
(2, 'Sana Khan', 'Bangalore', 'Silver'),
(3, 'John Mathew', 'Mumbai', 'Gold'),
(4, 'Ayesha Begum', 'Chennai', 'Bronze'),
(5, 'Vikram Rao', 'Delhi', 'Silver'),
(6, 'Divya Sharma', 'Pune', NULL);

INSERT INTO payments VALUES
(1001, 1, 15000, 'UPI', 'Success'),
(1002, 1, 8000, 'Card', 'Success'),
(1003, 2, 5000, 'Cash', 'Pending'),
(1004, 3, 22000, 'UPI', 'Success'),
(1005, 7, 12000, 'Card', 'Failed'),
(1006, NULL, 3000, 'Cash', 'Pending'),
(1007, 4, NULL, 'UPI', 'Success'),
(1008, 5, 7000, NULL, 'Success');

-- Exercise 35
select customer_name from customers_new
where customer_id in
(select customer_id from payments 
where customer_id is not null);

-- Exercise 36
select customer_name from customers_new
where customer_id not in
(	select customer_id from payments 
	where customer_id is not null);
    
-- Exercise 37
select * from payments 
where amount > (select avg(amount) from payments);

-- Exercise 38
select customer_name from customers_new
where customer_id =(
	select customer_id from payments 
	where amount =
		(select max(amount) from payments 
        )
	);

-- Exercise 39
select customer_name from customers_new
where membership_type = 'Gold' and customer_id in (
	select customer_id from payments 
	where customer_id is not null
	);
    
-- Exercise 40
select customer_name from customers_new
where customer_id in
(	select customer_id from payments 
	group by customer_id 
    having sum(amount) > 10000
    );

-- Exercise 41
select payment_id 
from payments
where customer_id is null
or customer_id not in (
	select customer_id from customers_new);
    
-- Exercise 42
select customer_name from customers_new c
where exists(
	select 1 from payments p where p.customer_id = c.customer_id
);

-- Exercise 43
select customer_name from customers_new c
where not exists(
	select 1 from payments p where p.customer_id = c.customer_id
);

-- Exercise 44
select distinct c.customer_name from customers_new c
join payments p 
on c.customer_id = p.customer_id
where p.amount > ( 
	select avg(amount) from payments p
);