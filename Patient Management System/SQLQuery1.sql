--Creating a new database
CREATE DATABASE patients_db
--Use the new database
USE patients_db

CREATE TABLE patients (
patientId INT PRIMARY KEY, 
patientName VARCHAR(50), 
gender VARCHAR(5), 
age INT, 
bloodGroup VARCHAR(5)
);

CREATE PROCEDURE validateID(@id INT)
AS
BEGIN
	SELECT *
	FROM patients
	WHERE patientId = @id
END;

CREATE PROCEDURE insertPatient(@id INT, @name VARCHAR(50), @gender VARCHAR(5), @age INT, @bloodGroup VARCHAR(5))
AS
BEGIN
	INSERT INTO patients VALUES (@id, @name, @gender, @age, @bloodGroup)
END;

CREATE PROCEDURE search(@id INT)
AS
BEGIN
	SELECT *
	FROM patients
	WHERE patientId = @id
END;

CREATE PROCEDURE deletePatient(@id INT)
AS
BEGIN
	DELETE
	FROM patients
	WHERE patientId = @id
END;

SELECT * FROM patients

SELECT * FROM patients WHERE patientId = 152

EXEC deletePatient 142

TRUNCATE TABLE patients