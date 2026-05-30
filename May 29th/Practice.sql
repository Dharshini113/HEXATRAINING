-- create database retail_db
-- use reatail_db
-- create table customers(
-- 	id int,
--     cust_name varchar(50),
--     city varchar(50)
--    ) 
--     
-- insert into customers values
-- (1,'Rahul','Hyderabad'),
-- (2,'Priya','Bandalore'),
-- (3,'Amit','Mumbai')

-- set sql_safe_updates = 0;    no primary key is provided hence safe update is off

-- update customers 
-- set city = 'Chennai'
-- where id = 1;

-- set sql_safe_updates = 1;     safe update is on 

-- set sql_safe_updates = 0;    

-- delete from customers
-- where city = 'Bandalore';

-- set sql_safe_updates = 1;   

-- select * from customers;

-- create table  products(
-- 	product_id int primary key,
--     product_name varchar(100),
--     category varchar(50),
--     price decimal(10,2),
--     stock_quantity int,
--     supplier_city varchar(50)
-- );

-- insert into products
-- values
-- (1,'Laptop','Electronics',55000,10,'Hyderabad'),
-- (2,'Tablet','Electronics',45000,16,'Coimbatore'),
-- (3,'Mobile','Electronics',30000,6,'Chennai')

-- update products
-- set stock_quantity = 8
-- where product_id = 2;
-- select * from products

-- delete from products where product_name = 'Mobile';   here product_name  is not primary key hance if it necessaery  we can use set_safe_update
-- delete from products where product_id = 2;  

-- drop table products
-- drop table customers

-- use retail_db;

-- CREATE TABLE products
-- (
--     product_id INT PRIMARY KEY,
--     product_name VARCHAR(50),
--     category VARCHAR(30),
--     price DECIMAL(10,2),
--     stock_quantity INT,
--     supplier_city VARCHAR(30)
-- );

-- INSERT INTO products VALUES
-- (1,'Laptop','Electronics',55000,10,'Hyderabad'),
-- (2,'Mobile','Electronics',25000,25,'Bangalore'),
-- (3,'Printer','Electronics',18000,8,'Pune'),
-- (4,'Office Chair','Furniture',7500,15,'Mumbai'),
-- (5,'Desk','Furniture',12000,5,'Chennai'),
-- (6,'Notebook','Stationery',80,200,'Hyderabad'),
-- (7,'Pen','Stationery',20,500,'Delhi'),
-- (8,'Water Bottle','Accessories',500,50,'Bangalore');

-- select * from products;

-- select product_name, price from products;

-- select distinct category from products;
-- select * from products where category='Electronics';

-- select * from products where price>10000;
-- select * from products where stock_quantity < 20;

-- select * from products where category = 'Electronics'
-- and price > 20000;

-- select * from products where supplier_city='Hyderabad' or
-- supplier_city='Bangalore';

-- select * from products where not category = 'Electronics';

-- select * from products where supplier_city in ('Hyderabad','Delhi');

-- select * from products where price between 500 and 20000;

-- select * from products where product_name like 'P%';

-- select * from products where product_name like '%k';

-- select * from products where product_name like '%top%';

-- select product_name AS Product, price AS ProductPrice
-- from products;

-- select * from products order by price;

-- select * from products order by price desc;

-- select count(*) from products;

-- select count(*) from products where category='Electronics';

-- select sum(price) from products;

-- select count(*) as TotalProducts,
-- sum(price) as TotalPrice,
-- avg(price) as AveragePrice,
-- max(price) as HighestPrice,
-- min(price) as LowestPrice
-- from products;

-- select category, count(*) as ProductCount
-- from products group by category;

-- select category, sum(price) as TotalPrice
-- from products group by category;

-- drop table products;













