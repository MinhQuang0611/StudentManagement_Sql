# StudentManagement_Sql
Mọi người tải file SQLQuery1 về đổi 2 cái đường dẫn thành đường dẫn lưu file trong máy của mình
USE master;
GO

CREATE DATABASE QUANLYSINHVIEN ON 

Hai đường dẫn này nhá
(FILENAME = 'D:\Program Files\SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\QUANLYSINHVIEN.mdf'), 
(FILENAME = 'D:\Program Files\SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\QUANLYSINHVIEN_log.ldf')


FOR ATTACH;
GO
