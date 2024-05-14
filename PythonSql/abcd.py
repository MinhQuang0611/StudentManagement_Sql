import pyodbc
import tkinter as tk

# Kết nối đến cơ sở dữ liệu SQL Server
server='DESKTOP-HRTE7HR\\SQLEXPRESS'
database ='QUANLYSINHVIEN'
username =''
password=''

Connection_String=f'DRIVER={{SQL SERVER}};SERVER={server};DATABASE={database};UID={username};password={password}'
conn = pyodbc.connect(Connection_String)

def display_data():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Sinhvien')
    rows = cursor.fetchall()

    listbox.delete(0, tk.END)
    
    for row in rows:
        listbox.insert(tk.END, row)

root = tk.Tk()
root.title("Hiển thị dữ liệu từ SQL Server")

listbox = tk.Listbox(root, width=100)
listbox.pack(padx=10, pady=20)

button = tk.Button(root, text="Hiển thị dữ liệu", command=display_data)
button.pack(pady=5)

root.mainloop()
