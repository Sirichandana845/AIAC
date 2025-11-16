CREATE TABLE e_mp(
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(15),
    HireDate DATE,
    Salary DECIMAL(10,2),
    DepartmentID INT,
    JobTitle VARCHAR(100),
    Active BOOLEAN DEFAULT true
);
INSERT INTO e_mp (FirstName, LastName, Email, Phone, HireDate, Salary, DepartmentID, JobTitle)
VALUES 
('John', 'Smith', 'john.smith@email.com', '555-0101', '2022-01-15', 65000.00, 1, 'Software Engineer'),
('Mary', 'Johnson', 'mary.j@email.com', '555-0102', '2022-02-01', 70000.00, 2, 'Project Manager'),
('David', 'Brown', 'david.b@email.com', '555-0103', '2022-03-10', 55000.00, 1, 'Developer'),
('Sarah', 'Wilson', 'sarah.w@email.com', '555-0104', '2022-04-20', 62000.00, 3, 'Business Analyst'),
('Michael', 'Davis', 'michael.d@email.com', '555-0105', '2022-05-05', 68000.00, 2, 'Senior Developer');

select * from e_mp;