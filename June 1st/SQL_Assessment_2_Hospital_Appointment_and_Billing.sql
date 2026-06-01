CREATE DATABASE hospital_capstone_db;

USE hospital_capstone_db;

CREATE TABLE patients
(
    patient_id INT PRIMARY KEY,
    patient_name VARCHAR(100),
    gender VARCHAR(10),
    age INT,
    city VARCHAR(50),
    phone VARCHAR(15)
);

CREATE TABLE departments
(
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

CREATE TABLE doctors
(
    doctor_id INT PRIMARY KEY,
    doctor_name VARCHAR(100),
    specialization VARCHAR(100),
    department_id INT,
    consultation_fee DECIMAL(10,2),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE appointments
(
    appointment_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    appointment_status VARCHAR(30),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE treatments
(
    treatment_id INT PRIMARY KEY,
    appointment_id INT,
    treatment_name VARCHAR(100),
    treatment_cost DECIMAL(10,2),
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
);

CREATE TABLE bills
(
    bill_id INT PRIMARY KEY,
    patient_id INT,
    appointment_id INT,
    bill_date DATE,
    total_amount DECIMAL(10,2),
    bill_status VARCHAR(30),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
);

CREATE TABLE payments
(
    payment_id INT PRIMARY KEY,
    bill_id INT,
    payment_mode VARCHAR(30),
    paid_amount DECIMAL(10,2),
    payment_status VARCHAR(30),
    FOREIGN KEY (bill_id) REFERENCES bills(bill_id)
);

INSERT INTO departments VALUES
(1,'Cardiology'),
(2,'Neurology'),
(3,'Orthopedics'),
(4,'Pediatrics'),
(5,'Dermatology');

INSERT INTO patients VALUES
(1,'Arun Kumar','Male',35,'Chennai','9876543210'),
(2,'Priya Sharma','Female',42,'Hyderabad','9876543211'),
(3,'Rahul Verma','Male',29,'Bangalore','9876543212'),
(4,'Sneha Reddy','Female',38,'Hyderabad','9876543213'),
(5,'Vikram Singh','Male',50,'Mumbai','9876543214'),
(6,'Anjali Mehta','Female',45,'Delhi','9876543215'),
(7,'Karthik Raj','Male',31,'Chennai','9876543216'),
(8,'Divya Nair','Female',27,'Kochi','9876543217'),
(9,'Rohit Gupta','Male',55,'Delhi','9876543218'),
(10,'Meera Iyer','Female',33,'Chennai','9876543219'),
(11,'Sanjay Patel','Male',48,'Ahmedabad','9876543220'),
(12,'Pooja Das','Female',36,'Hyderabad','9876543221');

INSERT INTO doctors VALUES
(101,'Dr. Rajesh Kumar','Cardiologist',1,1200),
(102,'Dr. Priya Menon','Neurologist',2,1500),
(103,'Dr. Arjun Singh','Orthopedic Surgeon',3,1000),
(104,'Dr. Kavya Reddy','Pediatrician',4,800),
(105,'Dr. Vivek Sharma','Dermatologist',5,900),
(106,'Dr. Nitin Rao','Cardiologist',1,1300),
(107,'Dr. Meena Patel','Neurologist',2,1400),
(108,'Dr. Suresh Iyer','Orthopedic Surgeon',3,1100);

INSERT INTO appointments VALUES
(1001,1,101,'2025-12-20','Completed'),
(1002,2,102,'2026-01-05','Completed'),
(1003,3,103,'2026-01-08','Cancelled'),
(1004,4,101,'2026-01-10','Completed'),
(1005,5,104,'2026-01-12','Scheduled'),
(1006,6,105,'2026-01-15','Completed'),
(1007,7,106,'2026-01-18','Completed'),
(1008,8,107,'2026-01-20','Scheduled'),
(1009,9,108,'2026-01-22','Completed'),
(1010,10,101,'2026-01-25','Cancelled'),
(1011,11,102,'2026-01-27','Completed'),
(1012,12,103,'2026-01-29','Scheduled'),
(1013,1,104,'2026-02-01','Completed'),
(1014,2,105,'2026-02-03','Completed'),
(1015,3,106,'2026-02-05','Scheduled'),
(1016,4,107,'2026-02-08','Completed'),
(1017,5,108,'2026-02-10','Completed'),
(1018,6,101,'2026-02-12','Scheduled'),
(1019,7,102,'2026-02-15','Completed'),
(1020,8,103,'2026-02-18','Completed');

INSERT INTO treatments VALUES
(201,1001,'ECG',2500),
(202,1002,'Brain Scan',6000),
(203,1004,'Heart Checkup',7000),
(204,1006,'Skin Therapy',3500),
(205,1007,'ECG',2500),
(206,1009,'Knee Treatment',5500),
(207,1011,'Brain Scan',6500),
(208,1013,'Child Vaccination',2000),
(209,1014,'Skin Therapy',3000),
(210,1016,'Neurology Consultation',5000),
(211,1017,'Fracture Treatment',8000),
(212,1019,'Brain Scan',6200),
(213,1020,'Joint Therapy',4500),
(214,1005,'Child Checkup',1800),
(215,1018,'Heart Checkup',7000);

INSERT INTO bills VALUES
(301,1,1001,'2025-12-20',3700,'Paid'),
(302,2,1002,'2026-01-05',7500,'Paid'),
(303,4,1004,'2026-01-10',8500,'Paid'),
(304,6,1006,'2026-01-15',4400,'Paid'),
(305,7,1007,'2026-01-18',3800,'Paid'),
(306,9,1009,'2026-01-22',6600,'Paid'),
(307,11,1011,'2026-01-27',8000,'Paid'),
(308,1,1013,'2026-02-01',2800,'Paid'),
(309,2,1014,'2026-02-03',3900,'Paid'),
(310,4,1016,'2026-02-08',6400,'Paid'),
(311,5,1017,'2026-02-10',9100,'Paid'),
(312,7,1019,'2026-02-15',7600,'Paid'),
(313,8,1020,'2026-02-18',5600,'Paid'),
(314,5,1005,'2026-01-12',2600,'Unpaid'),
(315,6,1018,'2026-02-12',8500,'Unpaid');

INSERT INTO payments VALUES
(401,301,'UPI',3700,'Paid'),
(402,302,'Credit Card',7500,'Paid'),
(403,303,'UPI',8500,'Paid'),
(404,304,'Cash',4400,'Paid'),
(405,305,'UPI',3800,'Paid'),
(406,306,'Debit Card',6600,'Paid'),
(407,307,'UPI',8000,'Paid'),
(408,308,'Cash',2800,'Paid'),
(409,309,'UPI',3900,'Paid'),
(410,310,'Credit Card',6400,'Paid'),
(411,311,'UPI',9100,'Paid'),
(412,312,'Debit Card',7600,'Paid'),
(413,313,'UPI',5600,'Paid'),
(414,314,'UPI',0,'Pending'),
(415,315,'Cash',4000,'Partial');

-- PART 1
-- 1
select * FROM patients;

-- 2
select * FROM doctors;

-- 3
select * FROM patients WHERE city = 'Hyderabad';

-- 4
SELECT * FROM doctors
WHERE department_id =
(	SELECT department_id FROM departments
	WHERE department_name='Cardiology'  );

-- 5
SELECT * FROM appointments WHERE appointment_date > '2026-01-01';

-- 6 
SELECT * FROM appointments WHERE appointment_status = 'Cancelled';

-- 7
SELECT * FROM bills WHERE total_amount > 5000;

-- 8
SELECT * FROM payments where payment_mode = 'UPI';

-- 9
SELECT * FROM patients where age between 30 and 50;

-- 10
SELECT * FROM doctors WHERE consultation_fee > 800;

-- PART 2
-- 11
SELECT count(*) as tot_patients FROM patients;

-- 12
SELECT count(*) as tot_doctors FROM doctors;

-- 13
SELECT COUNT(*) as tot_appointments FROM appointments;

-- 14
SELECT avg(consultation_fee) as average_fee FROM doctors;

-- 15
SELECT max(treatment_cost) as highest FROM treatments;

-- 16
SELECT sum(total_amount) AS tot_billing FROM bills;

-- 17
SELECT sum(paid_amount) as tot_paid FROM payments;

-- 18
SELECT city, count(*) as tot_patients
FROM patients
group by city;

-- 19
SELECT specialization, count(*) as tot_doctors
FROM doctors
group by specialization;

-- 20
SELECT appointment_status, count(*) as tot_appointments
FROM appointments
group by appointment_status;

-- PART 3
-- 21
SELECT p.patient_name, a.appointment_date, a.appointment_status
FROM patients p
join appointments a on p.patient_id = a.patient_id;

-- 22
SELECT d.doctor_name, dp.department_name
FROM doctors d
join departments dp on d.department_id = dp.department_id;

-- 23
SELECT p.patient_name, d.doctor_name, a.appointment_date
FROM appointments a
join patients p on a.patient_id = p.patient_id
join doctors d on a.doctor_id = d.doctor_id;

-- 24
SELECT a.appointment_id, t.treatment_name, t.treatment_cost
FROM appointments a
join treatments t on a.appointment_id = t.appointment_id;

-- 25
SELECT b.bill_id, p.patient_name, b.total_amount
FROM bills b
join patients p on b.patient_id = p.patient_id;

-- 26
SELECT b.bill_id, p.payment_mode, 
	p.paid_amount, p.payment_status
FROM bills b
join payments p on b.bill_id = p.bill_id;

-- 27
SELECT
	p.patient_name,
	d.doctor_name,
	dp.department_name,
	a.appointment_date,
	a.appointment_status,
	t.treatment_name,
	t.treatment_cost,
	b.total_amount,
	pay.payment_status
FROM appointments a
join patients p on a.patient_id = p.patient_id
join doctors d on a.doctor_id = d.doctor_id
join departments dp on d.department_id = dp.department_id
left join treatments t on a.appointment_id = t.appointment_id
left join bills b on a.appointment_id = b.appointment_id
left join payments pay on b.bill_id = pay.bill_id;

-- PART 4
-- 28
SELECT doctor_id, count(*) as tot_appointments
FROM appointments
group by doctor_id;

-- 29
SELECT dp.department_name, count(*) as tot_appointments
FROM appointments a
join doctors d on a.doctor_id = d.doctor_id
join departments dp on d.department_id = dp.department_id
group by dp.department_name;

-- 30
SELECT dp.department_name, sum(b.total_amount) as revenue
FROM departments dp
join doctors d on dp.department_id = d.department_id
join appointments a on d.doctor_id = a.doctor_id
join bills b on a.appointment_id = b.appointment_id
group by dp.department_name;

-- 31
SELECT treatment_name, sum(treatment_cost) as tot_cost
FROM treatments
 group by treatment_name;

-- 32
SELECT p.city, sum(b.total_amount) as tot_billing
FROM patients p
join bills b on p.patient_id = b.patient_id
group by p.city;

-- 33
SELECT d.doctor_name, count(*) as tot_appointments
FROM doctors d
join appointments a on d.doctor_id = a.doctor_id
group by d.doctor_name 
having count(*) > 2;

-- 34
SELECT dp.department_name, sum(b.total_amount) as revenue
FROM departments dp
join doctors d on dp.department_id = d.department_id
join appointments a on d.doctor_id = a.doctor_id
join bills b on a.appointment_id = b.appointment_id
group by dp.department_name
having sum(b.total_amount) > 20000;

-- 35
SELECT city, count(*) as tot_patients
FROM patients
group by city
having count(*) > 2;

-- 36
SELECT * FROM patients
WHERE patient_id in
(	SELECT patient_id FROM appointments );

-- 37
SELECT * FROM patients
WHERE patient_id not in
(	SELECT patient_id FROM appointments );

-- 38
SELECT * FROM doctors
WHERE doctor_id not in
(	SELECT doctor_id FROM appointments );

-- 39
SELECT * FROM bills
WHERE total_amount >
( SELECT avg(total_amount) FROM bills  );

-- 40
SELECT p.patient_name, b.total_amount
FROM patients p
join bills b on p.patient_id = b.patient_id
WHERE b.total_amount =
(	SELECT MAX(total_amount) FROM bills );

-- 41
SELECT * FROM doctors
WHERE consultation_fee >
(	SELECT avg(consultation_fee) FROM doctors );

-- 42
SELECT distinct p.patient_name
FROM patients p
join appointments a on p.patient_id = a.patient_id
join doctors d on a.doctor_id = d.doctor_id
join departments dp on d.department_id = dp.department_id
WHERE dp.department_name = 'Cardiology';

-- 43
SELECT * FROM bills WHERE bill_status = 'Unpaid';

-- 44
SELECT * FROM appointments
WHERE appointment_id in
( SELECT appointment_id FROM treatments );

-- 45
SELECT p.patient_name, sum(b.total_amount) as tot_billing
FROM patients p
join bills b on p.patient_id = b.patient_id
group by p.patient_id,p.patient_name
having sum(b.total_amount) >
(	SELECT avg(patient_total)
	FROM
	(	SELECT SUM(total_amount) as patient_total 
		FROM bills group by patient_id
	) avg_table
);

-- PART 6
-- 46
SELECT a.*
FROM appointments a
left join treatments t on a.appointment_id = t.appointment_id
WHERE t.appointment_id is NULL;

-- 47
SELECT b.* FROM bills b
left join payments p on b.bill_id = p.bill_id
WHERE p.bill_id is NULL;

-- 48
SELECT * FROM payments
WHERE paid_amount is NULL OR paid_amount = 0;

-- 49
SELECT a.appointment_id, a.appointment_status, b.bill_id
FROM appointments a
join bills b on a.appointment_id = b.appointment_id
WHERE a.appointment_status = 'Cancelled';

-- 50
SELECT b.bill_id, b.total_amount, p.paid_amount
FROM bills b
join payments p on b.bill_id = p.bill_id
WHERE p.payment_status = 'Paid' and p.paid_amount < b.total_amount;

-- 51
SELECT d.* FROM doctors d
left join departments dp
on d.department_id = dp.department_id
WHERE dp.department_id is NULL;

-- 52
SELECT a.*
FROM appointments a
left join patients p on a.patient_id = p.patient_id
left join doctors d on a.doctor_id = d.doctor_id
WHERE p.patient_id is NULL or d.doctor_id is NULL;

-- Report 1
select
    p.patient_name, p.city,
    count(distinct a.appointment_id) as total_appointments,
    coalesce(sum(distinct b.total_amount),0) as total_bill_amount,
    coalesce(sum(pay.paid_amount),0) as total_paid_amount,
    coalesce(sum(distinct b.total_amount),0)
      - coalesce(sum(pay.paid_amount),0) as pending_amount
from patients p
left join appointments a on p.patient_id = a.patient_id
left join bills b on p.patient_id = b.patient_id
left join payments pay on b.bill_id = pay.bill_id
group by p.patient_id, p.patient_name, p.city;

-- coalesce(expression, value_if_null)
-- coalesce(null,0) return 0
-- coalesce(500,0) return 500
