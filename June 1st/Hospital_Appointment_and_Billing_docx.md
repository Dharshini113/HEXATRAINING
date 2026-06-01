Hospital Capstone Database Project

Database Design :::  

    Patients – patient information.
    Departments – hospital department details.
    Doctors – doctor information and specialization.
    Appointments – patient appointment records.
    Treatments – treatment details and costs.
    Bills – billing information.
    Payments – payment details.


Table Relationships :::  

    One patient can book many appointments.
    One doctor can handle many appointments.
    One department can have many doctors.
    One appointment can have a treatment record.
    One appointment can generate a bill.
    One bill can have a payment record.

Primary Keys :::  

    patients → patient_id
    departments → department_id
    doctors → doctor_id
    appointments → appointment_id
    treatments → treatment_id
    bills → bill_id
    payments → payment_id

Relationships :::  

----(Foreign Keys)-----

    doctors.department_id → departments.department_id
    appointments.patient_id → patients.patient_id
    appointments.doctor_id → doctors.doctor_id
    treatments.appointment_id → appointments.appointment_id
    bills.patient_id → patients.patient_id
    bills.appointment_id → appointments.appointment_id
    payments.bill_id → bills.bill_id


Key Insights from Reports :::  

    Patients can be analyzed based on city, age, and gender.
    Doctors are categorized by specialization and department.
    Appointment reports help track scheduled, completed, and cancelled appointments.
    Department-wise and doctor-wise appointment counts can be generated.
    Treatment costs help identify high-value medical services.
    Hospital revenue can be analyzed using billing records.
    Paid, unpaid, and partial payments can be monitored.
    Unpaid bills can be identified for follow-up actions.
    Payment methods such as UPI, Cash, Credit Card, and Debit Card can be analyzed.
    Revenue reports help identify top-performing departments.

The database helps in managing hospital operations and generating useful patient, appointment, treatment, billing, and payment reports.
