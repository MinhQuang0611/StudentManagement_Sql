import pyodbc
import tkinter as tk

# Kết nối đến cơ sở dữ liệu SQL Server
server='DESKTOP-HRTE7HR\\SQLEXPRESS'
database ='QUANLYSINHVIEN'
username =''
password=''

Connection_String=f'DRIVER={{SQL SERVER}};SERVER={server};DATABASE={database};UID={username};password={password}'
conn = pyodbc.connect(Connection_String)

# Hàm để thực hiện truy vấn và hiển thị dữ liệu lên giao diện
def display_data():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Sinhvien')
    rows = cursor.fetchall()
    
    # Xóa dữ liệu cũ trong ListBox
    listbox.delete(0, tk.END)
    
    # Hiển thị dữ liệu mới từ kết quả truy vấn
    for row in rows:
        listbox.insert(tk.END, row)

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Hiển thị dữ liệu từ SQL Server")

# Tạo một ListBox để hiển thị dữ liệu
listbox = tk.Listbox(root, width=100)
listbox.pack(padx=10, pady=20)

# Tạo một nút để kích hoạt hiển thị dữ liệu
button = tk.Button(root, text="Hiển thị dữ liệu", command=display_data)
button.pack(pady=5)

# Chạy ứng dụng
root.mainloop()
