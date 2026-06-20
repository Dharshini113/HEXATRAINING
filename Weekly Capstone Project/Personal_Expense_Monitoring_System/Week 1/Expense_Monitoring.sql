-- Week 1: MySQL Schema for Personal Expense Monitoring System

CREATE DATABASE expense_monitoring;
USE expense_monitoring;

-- Table: users
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    city VARCHAR(50),
    monthly_budget DECIMAL(10, 2) NOT NULL DEFAULT 0.00
);

-- Table: categories
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(60) NOT NULL UNIQUE
);

-- Table: expenses
CREATE TABLE expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    category_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    expense_date DATE NOT NULL,
    description VARCHAR(255),
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

INSERT INTO categories (category_name)
VALUES
('Food'),
('Transport'),
('Utilities'),
('Shopping'),
('Entertainment'),
('Healthcare'),
('Education');

INSERT INTO users
(full_name, email, city, monthly_budget)
VALUES
('Arun Kumar', 'arun@gmail.com', 'Chennai', 25000.00),
('Priya Sharma', 'priya@gmail.com', 'Coimbatore', 30000.00),
('Rajesh Kumar', 'rajesh@gmail.com', 'Madurai', 20000.00);

INSERT INTO expenses
(user_id, category_id, amount, expense_date, description)
VALUES
(1, 1, 250.00, '2026-01-05', 'Lunch'),
(1, 2, 120.00, '2026-01-06', 'Bus Fare'),
(1, 4, 1500.00, '2026-01-08', 'Clothes Purchase'),
(1, 3, 950.00, '2026-01-15', 'Internet Bill'),
(2, 1, 300.00, '2026-01-05', 'Dinner'),
(2, 3, 800.00, '2026-01-10', 'Electricity Bill'),
(2, 4, 2200.00, '2026-01-20', 'Mobile Accessories'),
(3, 5, 500.00, '2026-01-12', 'Movie Ticket'),
(3, 2, 200.00, '2026-01-13', 'Auto Fare'),
(3, 6, 1200.00, '2026-01-18', 'Medical Checkup');

SELECT * FROM expenses;

SELECT * FROM expenses WHERE expense_id = 1;

SELECT * FROM expenses WHERE user_id = 1;

DELETE FROM expenses WHERE expense_id = 10;

select count(*) from expenses;

UPDATE expenses SET amount = 1800 
WHERE expense_id = 3;

select * from expenses;

SELECT
	c.category_name,
	SUM(amount) AS total_expense
FROM expenses e
JOIN categories c ON e.category_id = c.category_id
GROUP BY
	c.category_name
ORDER BY c.category_name;

-- Stored procedure
DELIMITER $$

CREATE PROCEDURE GetMonthlyCategoryExpenses()
BEGIN
    SELECT
        c.category_name,
        SUM(amount) AS total_expense
    FROM expenses e
    JOIN categories c ON e.category_id = c.category_id
    GROUP BY c.category_name
    ORDER BY c.category_name;
END$$

DELIMITER ;

CALL GetMonthlyCategoryExpenses();

