
import pyodbc
import pandas as pd 
import tkinter as tk
from tkinter import messagebox


server='DESKTOP-HRTE7HR\\SQLEXPRESS'
database ='QUANLYSINHVIEN'
username =''
password=''

Connection_String=f'DRIVER={{SQL SERVER}};SERVER={server};DATABASE={database};UID={username};password={password}'
conn = pyodbc.connect(Connection_String)
def display_student_data():
    root = tk.Tk()
    root.title("Thông tin Sinh Viên")
    listbox = tk.Listbox(root, width=100)
    listbox.pack(padx=10, pady=20)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Sinhvien')
    rows = cursor.fetchall()

    listbox.delete(0, tk.END)
    
    for row in rows:
        listbox.insert(tk.END, row)
def display_class_data():
    root = tk.Tk()
    root.title("Thông tin Lớp")
    listbox = tk.Listbox(root, width=100)
    listbox.pack(padx=10, pady=20)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Lop')
    rows = cursor.fetchall()

    listbox.delete(0, tk.END)
    
    for row in rows:
        listbox.insert(tk.END, row)
def display_department_data():
    root = tk.Tk()
    root.title("Thông tin Khoa")
    listbox = tk.Listbox(root, width=100)
    listbox.pack(padx=10, pady=20)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Khoa')
    rows = cursor.fetchall()

    listbox.delete(0, tk.END)
    
    for row in rows:
        listbox.insert(tk.END, row)
def display_course_data():
    root = tk.Tk()
    root.title("Thông tin Học phần")
    listbox = tk.Listbox(root, width=100)
    listbox.pack(padx=10, pady=20)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Hocphan')
    rows = cursor.fetchall()

    listbox.delete(0, tk.END)
    
    for row in rows:
        listbox.insert(tk.END, row)
def display_course_grade_data():
    root = tk.Tk()
    root.title("Thông tin Điểm học phần")
    listbox = tk.Listbox(root, width=100)
    listbox.pack(padx=10, pady=20)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM DiemHocPhan')
    rows = cursor.fetchall()

    listbox.delete(0, tk.END)
    
    for row in rows:
        listbox.insert(tk.END, row)
def display_extracurricular_activitiess_data():
    root = tk.Tk()
    root.title("Thông tin Hoạt động ngoại khóa")
    listbox = tk.Listbox(root, width=100)
    listbox.pack(padx=10, pady=20)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM HoatDongNgoaiKhoa')
    rows = cursor.fetchall()

    listbox.delete(0, tk.END)
    
    for row in rows:
        listbox.insert(tk.END, row)



def add_student(ma_sv_entry, ho_ten_entry, ngay_sinh_entry, gioi_tinh_entry, dia_chi_entry, so_dien_thoai_entry, email_entry, ma_lop_entry):
    ma_sv = ma_sv_entry.get()
    ho_ten = ho_ten_entry.get()
    ngay_sinh = ngay_sinh_entry.get()  
    gioi_tinh = gioi_tinh_entry.get()  
    dia_chi = dia_chi_entry.get()  
    so_dien_thoai = so_dien_thoai_entry.get() 
    email = email_entry.get()  
    ma_lop = ma_lop_entry.get() 
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO SinhVien (MaSV, HoTen, NgaySinh, GioiTinh, DiaChi, SoDienThoai, Email, MaLop)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', ma_sv, ho_ten, ngay_sinh, gioi_tinh, dia_chi, so_dien_thoai, email, ma_lop)
        
        conn.commit()
        messagebox.showinfo('Thông báo', 'Thêm sinh viên thành công!')
    except Exception as e:
        messagebox.showerror('Lỗi', f'Không thể thêm sinh viên: {e}')
    finally:
        cursor.close()

def update_student(ma_sv_entry, ho_ten_entry, ngay_sinh_entry, gioi_tinh_entry, dia_chi_entry, so_dien_thoai_entry, email_entry, ma_lop_entry):
    ma_sv = ma_sv_entry.get()
    ho_ten = ho_ten_entry.get()
    ngay_sinh = ngay_sinh_entry.get()  
    gioi_tinh = gioi_tinh_entry.get()  
    dia_chi = dia_chi_entry.get()  
    so_dien_thoai = so_dien_thoai_entry.get() 
    email = email_entry.get()  
    ma_lop = ma_lop_entry.get() 
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE SinhVien
            SET HoTen = ?, NgaySinh = ?, GioiTinh = ?, DiaChi = ?, SoDienThoai = ?, Email = ?, MaLop = ?
            WHERE MaSV = ?
        ''', ho_ten, ngay_sinh, gioi_tinh, dia_chi, so_dien_thoai, email, ma_lop, ma_sv)
        
        conn.commit()
        messagebox.showinfo('Thông báo', 'Cập nhật sinh viên thành công!')
    except Exception as e:
        messagebox.showerror('Lỗi', f'Không thể cập nhật sinh viên: {e}')
    finally:
        cursor.close()

def delete_student(ma_sv_entry):
    ma_sv = ma_sv_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM SinhVien
            WHERE MaSV = ?
        ''', ma_sv)
        
        conn.commit()
        messagebox.showinfo('Thông báo', 'Xóa sinh viên thành công!')
    except Exception as e:
        messagebox.showerror('Lỗi', f'Không thể xóa sinh viên: {e}')
    finally:
        cursor.close()



root = tk.Tk()
root.title('Quản lý Sinh viên')



tk.Label(root, text='Mã sinh viên:').grid(row=0, column=0)
entry_ma_sv = tk.Entry(root)
entry_ma_sv.grid(row=0, column=1)

tk.Label(root, text='Họ tên:').grid(row=1, column=0)
entry_ho_ten = tk.Entry(root)
entry_ho_ten.grid(row=1, column=1)

tk.Label(root, text='Ngày sinh:').grid(row=2, column=0)
entry_ngay_sinh = tk.Entry(root)
entry_ngay_sinh.grid(row=2, column=1)

tk.Label(root, text='Giới tính:').grid(row=3, column=0)
entry_gioi_tinh = tk.Entry(root)
entry_gioi_tinh .grid(row=3, column=1)

tk.Label(root, text='Địa chỉ:').grid(row=4, column=0)
entry_dia_chi = tk.Entry(root)
entry_dia_chi.grid(row=4, column=1)

tk.Label(root, text='Số điện thoại').grid(row=5, column=0)
entry_so_dien_thoai = tk.Entry(root)
entry_so_dien_thoai.grid(row=5, column=1)

tk.Label(root, text='Email:').grid(row=6, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=6, column=1)

tk.Label(root, text='Mã lớp').grid(row=7, column=0)
entry_ma_lop = tk.Entry(root)
entry_ma_lop.grid(row=7, column=1)

tk.Button(root, text='Thêm sinh viên', command=lambda: add_student(entry_ma_sv, entry_ho_ten, entry_ngay_sinh, entry_gioi_tinh, entry_dia_chi, entry_so_dien_thoai, entry_email, entry_ma_lop)).grid(row=8, column=0)
tk.Button(root, text='Cập nhật thông tin sinh viên', command=lambda: update_student(entry_ma_sv, entry_ho_ten, entry_ngay_sinh, entry_gioi_tinh, entry_dia_chi, entry_so_dien_thoai, entry_email, entry_ma_lop)).grid(row=8, column=1)
tk.Button(root, text='Xóa sinh viên', command=lambda: delete_student(entry_ma_sv)).grid(row=8, column=2)
tk.Button(root, text='Bảng thông tin sinh viên', command= lambda: display_student_data()).grid(row=9, column=0)
tk.Button(root, text='Bảng thông tin lớp', command= lambda: display_class_data()).grid(row=9, column=1)
tk.Button(root, text='Bảng thông tin khoa', command= lambda: display_department_data()).grid(row=9, column=2)
tk.Button(root, text='Bảng thông tin học phần', command= lambda: display_course_data()).grid(row=10, column=0)
tk.Button(root, text='Bảng thông tin điểm học phần', command= lambda: display_course_grade_data()).grid(row=10, column=1)
tk.Button(root, text='Bảng thông tin hoạt động ngoại khóa', command= lambda: display_extracurricular_activitiess_data()).grid(row=10, column=2)




root.mainloop()

