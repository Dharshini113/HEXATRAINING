create database Smart_Home_Energy_Usage;
use Smart_Home_Energy_Usage;

-- ROOMS TABLE
CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_name VARCHAR(100) NOT NULL UNIQUE
);

-- DEVICES TABLE
CREATE TABLE devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    device_name VARCHAR(100) NOT NULL,
    device_type VARCHAR(50),
    room_id INT NOT NULL,
    status ENUM('ON','OFF','IDLE') DEFAULT 'OFF', 
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

-- ENERGY LOGS TABLE
CREATE TABLE energy_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    device_id INT NOT NULL,
    log_date DATE NOT NULL,
    log_timestamp DATETIME NOT NULL,
    energy_kwh DECIMAL(10,2) NOT NULL CHECK (energy_kwh >= 0),
    FOREIGN KEY (device_id) REFERENCES devices(device_id)
);

INSERT INTO rooms (room_name) VALUES
('Living Room'),
('Kitchen'),
('Bedroom 1'),
('Bedroom 2'),
('Utility');

INSERT INTO devices (device_name, device_type, room_id, status) VALUES
('Living Room AC', 'AC', 1, 'ON'),
('Smart Plug - TV', 'Smart Plug', 1, 'OFF'),
('Kitchen Fridge', 'Fridge', 2, 'ON'),
('Kitchen Microwave', 'Microwave', 2, 'OFF'),
('Bedroom 1 AC', 'AC', 3, 'ON'),
('Bedroom 1 Light', 'Light', 3, 'OFF'),
('Bedroom 2 Light', 'Light', 4, 'IDLE'),
('Washing Machine', 'Washing Machine', 5, 'OFF'),
('Geyser - Utility', 'Water Heater', 5, 'ON');

INSERT INTO energy_logs (device_id, log_date, log_timestamp, energy_kwh) VALUES
(1, '2026-06-15', '2026-06-15 08:00:00', 1.20),
(1, '2026-06-15', '2026-06-15 20:00:00', 2.50),
(1, '2026-06-16', '2026-06-16 08:00:00', 1.10),
(3, '2026-06-15', '2026-06-15 00:00:00', 0.80),
(3, '2026-06-16', '2026-06-16 00:00:00', 0.85),
(5, '2026-06-15', '2026-06-15 22:00:00', 1.75),
(5, '2026-06-16', '2026-06-16 22:00:00', 1.90),
(6, '2026-06-15', '2026-06-15 19:00:00', 0.10),
(7, '2026-06-15', '2026-06-15 19:30:00', 0.15),
(8, '2026-06-16', '2026-06-16 10:00:00', 1.50),
(9, '2026-06-15', '2026-06-15 06:00:00', 2.00),
(9, '2026-06-16', '2026-06-16 06:00:00', 2.10);

INSERT INTO energy_logs (device_id, log_date, log_timestamp, energy_kwh) VALUES
(1, CURDATE(), NOW(), 5.75);

SELECT * FROM rooms;

SELECT * FROM devices;

SELECT * FROM energy_logs;

SELECT * FROM energy_logs WHERE device_id = 1;

UPDATE energy_logs SET energy_kwh = 1.30
WHERE log_id = 1;

UPDATE devices SET status = 'OFF'
WHERE device_id = 1;

DELETE FROM energy_logs WHERE log_id = 8;

SELECT d.device_name, SUM(e.energy_kwh) AS total_kwh
FROM energy_logs e
JOIN devices d ON e.device_id = d.device_id
GROUP BY d.device_name
ORDER BY total_kwh DESC;

SELECT device_name, device_type FROM devices WHERE status = 'ON';

DELIMITER $$

CREATE PROCEDURE GetRoomEnergyUsage()
BEGIN
    SELECT
        r.room_id,
        r.room_name,
        SUM(el.energy_kwh) AS total_energy_kwh
    FROM rooms r
    JOIN devices d ON r.room_id = d.room_id
    JOIN energy_logs el ON d.device_id = el.device_id
    GROUP BY r.room_id, r.room_name
    ORDER BY r.room_id;
END $$

DELIMITER ;
CALL GetRoomEnergyUsage();