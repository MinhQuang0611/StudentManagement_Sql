import pyodbc
import pandas as pd 
import tkinter as tk
from tkinter import messagebox

#tk.Button(root, text='Bảng thông tin sinh viên', command= lambda: display_student_data(), width=30, height=2).grid(row=9, column=0)


server='DESKTOP-HRTE7HR\\SQLEXPRESS'
database ='QUANLYSINHVIEN'
username =''
password=''

Connection_String=f'DRIVER={{SQL SERVER}};SERVER={server};DATABASE={database};UID={username};password={password}'
try:
    conn = pyodbc.connect(Connection_String)
    query ='SELECT *FROM Sinhvien '
    df_sanpham = pd.read_sql(query,conn)
    print(df_sanpham)
except pyodbc.Error as e :
    print(f'Error: {e}')
finally:
    if conn:
        conn.close()    