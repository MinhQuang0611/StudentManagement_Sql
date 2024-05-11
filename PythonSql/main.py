import pyodbc
import pandas as pd 
import tkinter as tk
from tkinter import messagebox


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