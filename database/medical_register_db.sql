-- Run the following code to create the medical_register database

CREATE DATABASE medical_register;
USE medical_register;

-- Lists personal information of all doctors on the medical register
CREATE TABLE doctors (
    gmc_number CHAR(8) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    dob DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F'))
);

-- Lists dates related to medical registration
CREATE TABLE dates (
	doctor_gmc_number CHAR(8) PRIMARY KEY,
    registration_date DATE,
    last_date_of_revalidation DATE,
    FOREIGN KEY (doctor_gmc_number) REFERENCES doctors(gmc_number)
);

-- Population of tables with mock data
INSERT INTO doctors
(gmc_number, first_name, last_name, dob, gender)
VALUES
('12345678', 'nicola', 'heston', '1996-07-05', 'F'),
('87654321', 'rupert', 'davis', '1979-08-26', 'M'),
('49827905', 'leo', 'collins', '1993-02-16', 'M'),
('22345667', 'chantal', 'roberts', '2000-05-10', 'F'),
('95893000', 'sam', 'bridgerton', '1994-09-19','M'),
('88894728', 'rachel', 'anton', '1998-01-29', 'F'),
('11124982', 'sally', 'taylor', '1986-03-21', 'F'),
('58393759', 'tim', 'jones', '1984-11-15', 'M');

INSERT INTO dates
(doctor_gmc_number, registration_date, last_date_of_revalidation)
VALUES
('12345678', '2018-05-10', '2023-09-24'),
('87654321', '2007-04-23', '2018-01-18'),
('49827905', '2019-08-20', '2024-08-24'),
('22345667', '2024-02-02', '2024-02-02'),
('95893000', '2023-07-07', '2023-07-07'),
('88894728', '2020-04-24', '2020-04-24'),
('11124982', '2009-11-14', '2017-03-10'), 
('58393759', '2015-10-06', '2020-10-17');

-- To see all table contents
SELECT * FROM doctors;
SELECT * FROM dates;