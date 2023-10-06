-- Tạo cơ sở dữ liệu
CREATE DATABASE BankDatabase;
GO
-- Sử dụng cơ sở dữ liệu mới tạo
USE BankDatabase;
GO

-- Tạo bảng Users (Người dùng)
CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50) UNIQUE NOT NULL,
    Password NVARCHAR(255) NOT NULL, 
    Email NVARCHAR(100) UNIQUE NOT NULL,
    FullName NVARCHAR(100)
);
GO

-- Tạo bảng Accounts (Tài khoản)
CREATE TABLE Accounts (
    AccountID INT PRIMARY KEY IDENTITY(1,1),
    AccountNumber NVARCHAR(20) UNIQUE NOT NULL,
    AccountName NVARCHAR(100) NOT NULL,
    Balance DECIMAL(18, 2) DEFAULT 0.0,
    UserID INT FOREIGN KEY REFERENCES Users(UserID)
);
GO

-- Tạo bảng Transactions (Giao dịch)
CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY IDENTITY(1,1),
    TransactionType NVARCHAR(50) NOT NULL,
    Amount DECIMAL(18, 2) NOT NULL,
    TransactionDate DATETIME NOT NULL DEFAULT GETDATE(),
    AccountID INT FOREIGN KEY REFERENCES Accounts(AccountID)
);
GO

-- Thêm dữ liệu vào bảng Users
INSERT INTO Users (Username, Password, Email, FullName)
VALUES
    ('tvnam', '0605', 'tranvannam@gmail.com', N'Trần Văn Nam'),
    ('vxquang', '0111', 'voxuanquang@gmai', N'Võ Xuân Quang'),
    ('paquan', '1710', 'phamanhquan@gmail.com', N'Phạm Anh Quân');
GO

-- Thêm dữ liệu vào bảng Accounts
INSERT INTO Accounts (AccountNumber, AccountName, Balance, UserID)
VALUES
    ('060503', 'Savings Account', 5000.00, 1), -- Tài khoản của User 1
    ('011103', 'Checking Account', 2500.00, 2), -- Tài khoản của User 2
    ('171003', 'Savings Account', 10000.00, 3); -- Tài khoản của User 3
GO
--UPDATE Accounts
--SET AccountName = N'Phạm Anh Quân'
--WHERE AccountNumber = '171003';

select * from Users
select * from Accounts
SELECT *
FROM Transactions
WHERE AccountID = 1;

SELECT FullName, Balance FROM Users u JOIN Accounts a ON u.UserID = a.UserID WHERE u.UserID = 1;

-- Trừ tiền từ tài khoản 1
UPDATE Accounts
SET Balance = Balance - 500.00
WHERE AccountID = 1;

-- Cộng tiền vào tài khoản 2
UPDATE Accounts
SET Balance = Balance + 500.00
WHERE AccountID = 2;



-- Tạo giao dịch nhận tiền vào tài khoản 3
-- Cộng tiền vào tài khoản 3
UPDATE Accounts
SET Balance = Balance + 1000.00
WHERE AccountID = 3;
