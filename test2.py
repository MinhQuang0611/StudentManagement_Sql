
import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



server='DESKTOP-HRTE7HR\\SQLEXPRESS'
database ='QUANLYSINHVIEN'
username =''
password=''

Connection_String=f'DRIVER={{SQL SERVER}};SERVER={server};DATABASE={database};UID={username};password={password}'
conn = pyodbc.connect(Connection_String)
def display_student_data():
    second_window = tk.Tk()
    second_window.title("Thông tin sinh viên")

    app_label = tk.Label(second_window, text="Hệ thống quản lý sinh viên", fg="#06a099", width=40)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack()

    tree = ttk.Treeview(second_window)
    tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

    tree.heading("1", text="Mã Sinh Viên")
    tree.heading("2", text="Họ Và Tên ")
    tree.heading("3", text="Ngày Sinh")
    tree.heading("4", text="Giới Tính")
    tree.heading("5", text="Địa Chỉ")
    tree.heading("6", text="Số điện thoại")
    tree.heading("7", text="Email")
    tree.heading("8", text="Mã lớp")

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM SinhVien;")
    i = 1
    for row in cursor:
        tree.insert('', 'end', text=f"Sinh Viên thứ {i}", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        i+= 1
    tree.pack()
    second_window.mainloop()
def display_class_data():
    second_window = tk.Tk()
    second_window.title("Hiển thị kết quả")

    app_label = tk.Label(second_window, text="Hệ thống quản lý sinh viên", fg="#06a099", width=40)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack()

    tree = ttk.Treeview(second_window)
    tree["columns"] = ("1", "2", "3", "4")

    tree.heading("1", text="Mã lớp")
    tree.heading("2", text="Tên lớp ")
    tree.heading("3", text="Niên khóa")
    tree.heading("4", text="Mã Khoa")

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Lop;")
    i = 1
    for row in cursor:
        tree.insert('', 'end', text=f"Lớp thứ {i}", values=(row[0], row[1], row[2], row[3]))
        i+= 1
    tree.pack()
    second_window.mainloop()

def display_department_data():
    second_window = tk.Tk()
    second_window.title("Hiển thị kết quả")

    app_label = tk.Label(second_window, text="Hệ thống quản lý sinh viên", fg="#06a099", width=40)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack()

    tree = ttk.Treeview(second_window)
    tree["columns"] = ("1", "2", "3", "4")

    tree.heading("1", text="Mã Khoa")
    tree.heading("2", text="Tên Khoa ")

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Khoa;")
    i = 1
    for row in cursor:
        tree.insert('', 'end', text=f"Khoa thứ {i}", values=(row[0], row[1]))
        i+= 1
    tree.pack()
    second_window.mainloop()

def display_course_data():
    second_window = tk.Tk()
    second_window.title("Hiển thị kết quả")

    app_label = tk.Label(second_window, text="Hệ thống quản lý sinh viên", fg="#06a099", width=40)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack()

    tree = ttk.Treeview(second_window)
    tree["columns"] = ("1", "2", "3", "4","5", "6")

    tree.heading("1", text="Mã học phần")
    tree.heading("2", text="Tên học phần ")
    tree.heading("3", text="Số tín chỉ")
    tree.heading("4", text="Giảng viên")
    tree.heading("5", text="Thời gian")
    tree.heading("6", text="Phòng học")
    


    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM HocPhan;")
    i = 1
    for row in cursor:
        tree.insert('', 'end', text=f"{i}", values=(row[0], row[1], row[2], row[3],row[4], row[5]))
        i+= 1
    tree.pack()
    second_window.mainloop()

def display_course_grade_data():
    second_window = tk.Tk()
    second_window.title("Hiển thị kết quả")

    app_label = tk.Label(second_window, text="Hệ thống quản lý sinh viên", fg="#06a099", width=40)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack()

    tree = ttk.Treeview(second_window)
    tree["columns"] = ("1", "2", "3")

    tree.heading("1", text="Mã sinh viên")
    tree.heading("2", text="Mã học phần ")
    tree.heading("3", text="Điểm học phần")


    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM DiemHocPhan;")
    i = 1
    for row in cursor:
        tree.insert('', 'end', text=f"{i}", values=(row[0], row[1], row[2]))
        i+= 1
    tree.pack()
    second_window.mainloop()
def display_extracurricular_activitiess_data():
    second_window = tk.Tk()
    second_window.title("Hiển thị kết quả")

    app_label = tk.Label(second_window, text="Hệ thống quản lý sinh viên", fg="#06a099", width=40)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack()

    tree = ttk.Treeview(second_window)
    tree["columns"] = ("1", "2", "3", '4', '5')

    tree.heading("1", text="Mã hoạt động")
    tree.heading("2", text="Tên hoạt động ")
    tree.heading("3", text="Mô tả ")
    tree.heading("4", text="Thời gian tổ chức ")
    tree.heading("5", text="Địa điểm ")


    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM HoatDongNgoaiKhoa;")
    i = 1
    for row in cursor:
        tree.insert('', 'end', text=f"{i}", values=(row[0], row[1], row[2],row[3], row[4]))
        i+= 1
    tree.pack()
    second_window.mainloop()
def display_students_extracurricular_activitiess_data():
    second_window = tk.Tk()
    second_window.title("Hiển thị kết quả")

    app_label = tk.Label(second_window, text="Hệ thống quản lý sinh viên", fg="#06a099", width=40)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack()

    tree = ttk.Treeview(second_window)
    tree["columns"] = ("1", "2", "3", '4', '5')

    tree.heading("1", text="Mã sinh viên ")
    tree.heading("2", text="Mã hoạt động")

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM SinhVien_HoatDongNgoaiKhoa;")
    i = 1
    for row in cursor:
        tree.insert('', 'end', text=f"{i}", values=(row[0], row[1]))
        i+= 1
    tree.pack()
    second_window.mainloop()

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
def add_class(ma_lop_entry, ten_lop_entry, nien_khoa_entry, ma_khoa_entry):
    ma_lop = ma_lop_entry.get()
    ten_lop = ten_lop_entry.get()
    nien_khoa = nien_khoa_entry.get()
    ma_khoa = ma_khoa_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Lop (MaLop, TenLop, NienKhoa, Makhoa)
            VALUES (?,?,?,?)
                ''', ma_lop, ten_lop, nien_khoa, ma_khoa)
        conn.commit()
        messagebox.showinfo('Thông báo', 'Thêm lớp thành công!')
    except Exception as e:
        messagebox.showerror('Lỗi', f'Không thể thêm lớp : {e}')
    finally:
        cursor.close()
def update_class(ma_lop_entry, ten_lop_entry, nien_khoa_entry, ma_khoa_entry):
    ma_lop = ma_lop_entry.get()
    ten_lop = ten_lop_entry.get()
    nien_khoa = nien_khoa_entry.get()
    ma_khoa = ma_khoa_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Lop
            SET TenLop = ? , NienKhoa = ? , MaKhoa = ?
            WHERE Malop = ?
          
            ''', ten_lop, nien_khoa, ma_khoa, ma_lop)
        conn.commit()
        messagebox.showinfo('Thông báo', 'Cập nhật thông tin lớp thành công!')
    except Exception as e:
        messagebox.showerror('Lỗi', f'Không thể cập nhật thông tin lớp : {e}')
    finally:
        cursor.close()       
def delete_class(ma_lop_entry):
    ma_lop = ma_lop_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM Lop
            WHERE MaLop = ?
        ''', ma_lop)
        
        conn.commit()
        messagebox.showinfo('Thông báo', 'Xóa lớp thành công!')
    except Exception as e:
        messagebox.showerror('Lỗi', f'Không thể xóa lớp : {e}')
    finally:
        cursor.close()
def add_department(ma_khoa_entry, ten_khoa_entry):
    ma_khoa = ma_khoa_entry.get()
    ten_khoa = ten_khoa_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Khoa (Makhoa, TenKhoa)
            VALUES (?, ?)
            ''', ma_khoa, ten_khoa
        )
        conn.commit()
        messagebox.showinfo('thông báo', 'Thêm khoa thành công!')
    except Exception as e :
        messagebox.showerror('Lỗi', f'Không thể thêm khoa: {e}')
    finally:
        cursor.close()
def update_department(ma_khoa_entry, ten_khoa_entry):
    ma_khoa = ma_khoa_entry.get()
    ten_khoa = ten_khoa_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Khoa
            SET TenKhoa = ?
            WHERE Makhoa = ?
            ''', ten_khoa, ma_khoa
        )
        conn.commit()
        messagebox.showinfo('thông báo', 'Cập nhật thông tin khoa thành công!')
    except Exception as e :
        messagebox.showerror('Lỗi', f'Không thể cập nhật thông tin khoa: {e}')
    finally:
        cursor.close()
def delete_department(ma_khoa_entry):
    ma_khoa = ma_khoa_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM Khoa
            WHERE Makhoa = ?

        ''', ma_khoa
        )
        conn.commit()
        messagebox.showinfo('thông báo', 'Xóa khoa thành công!')
    except Exception as e :
        messagebox.showerror('Lỗi', f'Không thể Xóa thông tin khoa: {e}')
    finally:
        cursor.close()

def add_course(ma_hoc_phan_entry, ten_hoc_phan_entry, so_tin_chi_entry, giang_vien_entry, thoi_gian_entry, phong_hoc_entry):
    ma_hoc_phan = ma_hoc_phan_entry.get()
    ten_hoc_phan = ten_hoc_phan_entry.get()
    so_tin_chi = so_tin_chi_entry.get()
    giang_vien = giang_vien_entry.get()
    thoi_gian = thoi_gian_entry.get()
    phong_hoc = phong_hoc_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Hocphan(MaHocPhan, TenHocPhan, SoTinChi, GiangVien, ThoiGian, PhongHoc)
            VALUES (?,?,?,?,?,?)
                       ''', ma_hoc_phan, ten_hoc_phan, so_tin_chi, giang_vien, thoi_gian, phong_hoc)
        conn.commit()
        messagebox.showinfo('thông báo', 'Thêm học phần thành công')
    except Exception as e :
        messagebox.showerror('lỗi', f'Không thể thêm học phần: {e}')    
    finally:
        cursor.close()
def update_course(ma_hoc_phan_entry, ten_hoc_phan_entry, so_tin_chi_entry, giang_vien_entry, thoi_gian_entry, phong_hoc_entry):
    ma_hoc_phan = ma_hoc_phan_entry.get()
    ten_hoc_phan = ten_hoc_phan_entry.get()
    so_tin_chi = so_tin_chi_entry.get()
    giang_vien = giang_vien_entry.get()
    thoi_gian = thoi_gian_entry.get()
    phong_hoc = phong_hoc_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Hocphan
            SET TenHocPhan = ?, SoTinChi = ?, GiangVien = ?, ThoiGian = ?, PhongHoc = ?
            WHERE MaHocPhan = ?
                       ''',  ten_hoc_phan, so_tin_chi, giang_vien, thoi_gian, phong_hoc, ma_hoc_phan)
        conn.commit()
        messagebox.showinfo('thông báo', 'Cập nhật học phần thành công')
    except Exception as e :
        messagebox.showerror('lỗi', f'Không thể cập nhật học phần: {e}')    
    finally:
        cursor.close()
def delete_course(ma_hoc_phan_entry):
    ma_hoc_phan = ma_hoc_phan_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM HocPhan
            WHERE MaHocPhan = ?
                    
                    ''', ma_hoc_phan)
        conn.commit()
        messagebox.showinfo('Thông báo', 'Xóa học phần thành công!')
    except Exception as e:
        messagebox.showerror('Lỗi', f'Không thể xóa học phần : {e}')
    finally:
        cursor.close()
def add_grade_course(ma_sv_entry, ma_hoc_phan_entry, diem_hoc_phan_entry):
    ma_sv = ma_sv_entry.get()
    ma_hoc_phan = ma_hoc_phan_entry.get()
    diem_hoc_phan = diem_hoc_phan_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO DiemHocPhan (MaSV, MaHocPhan, DiemHocPhan)
            VALUES (?, ?, ?)
            ''', ma_sv, ma_hoc_phan, diem_hoc_phan
        )
        conn.commit()
        messagebox.showinfo('thông báo', 'Thêm điểm thành công!')
    except Exception as e :
        messagebox.showerror('Lỗi', f'Không thể thêm điểm: {e}')
    finally:
        cursor.close()
def update_grade_course(ma_sv_entry, ma_hoc_phan_entry, diem_hoc_phan_entry):
    ma_sv = ma_sv_entry.get()
    ma_hoc_phan = ma_hoc_phan_entry.get()
    diem_hoc_phan = diem_hoc_phan_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE DiemHocPhan
            SET DiemHocPhan = ?
            WHERE MaSV = ? , MaHocPhan = ? 
            ''', diem_hoc_phan,  ma_sv, ma_hoc_phan
        )
        conn.commit()
        messagebox.showinfo('thông báo', 'cập nhật điểm thành công!')
    except Exception as e :
        messagebox.showerror('Lỗi', f'Không thể cập nhật điểm: {e}')
    finally:
        cursor.close()
def delete_grade_course(ma_sv_entry, ma_hoc_phan_entry):
    ma_sv = ma_sv_entry.get()
    ma_hoc_phan = ma_hoc_phan_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM  DiemHocPhan            
            WHERE MaSV = ?, MaHocPhan = ? 
                       ''', ma_sv, ma_hoc_phan)
        conn.commit()
        messagebox.showinfo('thông báo', 'Xóa điểm thành công!')
    except Exception as e :
        messagebox.showerror('Lỗi', f'Không thể xóa điểm: {e}')
    finally:
        cursor.close()
def add_extracurricular_activitiess(ma_hoat_dong_entry, ten_hoat_dong_entry, mo_ta_entry, thoi_gian_to_chuc_entry, dia_diem_entry):
    ma_hoat_dong = ma_hoat_dong_entry.get()
    ten_hoat_dong = ten_hoat_dong_entry.get()
    mo_ta = mo_ta_entry.get()
    thoi_gian_to_chuc = thoi_gian_to_chuc_entry.get()
    dia_diem = dia_diem_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO HoatDongNgoaiKhoa (MaHoatDong, TenHoatDong, MoTa, ThoiGianToChuc, DiaDiem)
            VALUES (?, ?, ?, ?, ?)
        ''',ma_hoat_dong, ten_hoat_dong, mo_ta, thoi_gian_to_chuc, dia_diem)
        
        conn.commit()
        messagebox.showinfo('Thông báo', 'Thêm hoạt động thành công!')
    except Exception as e:
        messagebox.showerror('Lỗi', f'Không thể thêm hoạt đông: {e}')
    finally:
        cursor.close()
def update_extracurricular_activitiess(ma_hoat_dong_entry, ten_hoat_dong_entry, mo_ta_entry, thoi_gian_to_chuc_entry, dia_diem_entry):
    ma_hoat_dong = ma_hoat_dong_entry.get()
    ten_hoat_dong = ten_hoat_dong_entry.get()
    mo_ta = mo_ta_entry.get()
    thoi_gian_to_chuc = thoi_gian_to_chuc_entry.get()
    dia_diem = dia_diem_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE HoatDongNgoaiKhoa
            SET TenHoatDong = ?, MoTa = ?, ThoiGianToChuc = ?, DIaDiem = ?
            WHERE MaHoatDong = ?
        ''', ten_hoat_dong, mo_ta, thoi_gian_to_chuc, dia_diem, ma_hoat_dong)
        
        conn.commit()
        messagebox.showinfo('Thông báo', 'cập nhật hoạt động thành công!')
    except Exception as e:
        messagebox.showerror('Lỗi', f'Không thể cập nhật hoạt đông: {e}')
    finally:
        cursor.close()
def delete_extracurricular_activitiesss(ma_hoat_dong_entry):
    ma_hoat_dong = ma_hoat_dong_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM HoatDongNgoaiKhoa
            WHERE MaHoatDong = ?
        ''', ma_hoat_dong)
        
        conn.commit()
        messagebox.showinfo('Thông báo', 'Xóa hoạt động thành công!')
    except Exception as e:
        messagebox.showerror('Lỗi', f'Không thể xóa hoạt động : {e}')
    finally:
        cursor.close()



def add_student_extracurricular_activitiesss(ma_sv_entry, ma_hoat_dong_entry):
    ma_sv = ma_sv_entry.get()
    ma_hoat_dong = ma_hoat_dong_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO SinhVien_HoatDongNgoaiKhoa (MaSV, MaHoatDong)
            VALUES (?, ?)
            
                ''', ma_sv, ma_hoat_dong)
        conn.commit()
        messagebox.showinfo('Thông báo', 'Thêm thành công!')
    except Exception as e:
        messagebox.showerror('Lỗi', f'Không thể thêm : {e}')
    finally:
        cursor.close()

def delete_student_extracurricular_activitiesss(ma_sv_entry, ma_hoat_dong_entry):
    ma_sv = ma_sv_entry.get()
    ma_hoat_dong = ma_hoat_dong_entry.get()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM SinhVien_HoatDongNgoaiKhoa
            WHERE MaSv = ?, MaHoatDong = ?
            
                ''', ma_sv, ma_hoat_dong)
        conn.commit()
        messagebox.showinfo('Thông báo', 'Xóa thành công!')
    except Exception as e:
        messagebox.showerror('Lỗi', f'Không thể Xóa : {e}')
    finally:
        cursor.close()
def student_table():
    second_window = tk.Tk()
    second_window.title("Thông tin sinh viên")

    app_label = tk.Label(second_window, text="Hệ thống quản lý sinh viên", fg="#06a099", width=40)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack()

    form_frame = tk.Frame(second_window)
    form_frame.pack(side=tk.LEFT, padx=20, pady=10)
    tk.Label(form_frame, text='Mã sinh viên:').pack(anchor='w')
    entry_ma_sv = tk.Entry(form_frame)
    entry_ma_sv.pack(anchor='w')

    tk.Label(form_frame, text='Họ tên:').pack(anchor='w')
    entry_ho_ten = tk.Entry(form_frame)
    entry_ho_ten.pack(anchor='w')

    tk.Label(form_frame, text='Ngày sinh:').pack(anchor='w')
    entry_ngay_sinh = tk.Entry(form_frame)
    entry_ngay_sinh.pack(anchor='w')

    tk.Label(form_frame, text='Giới tính:').pack(anchor='w')
    entry_gioi_tinh = tk.Entry(form_frame)
    entry_gioi_tinh.pack(anchor='w')

    tk.Label(form_frame, text='Địa chỉ:').pack(anchor='w')
    entry_dia_chi = tk.Entry(form_frame)
    entry_dia_chi.pack(anchor='w')

    tk.Label(form_frame, text='Số điện thoại:').pack(anchor='w')
    entry_so_dien_thoai = tk.Entry(form_frame)
    entry_so_dien_thoai.pack(anchor='w')

    tk.Label(form_frame, text='Email:').pack(anchor='w')
    entry_email = tk.Entry(form_frame)
    entry_email.pack(anchor='w')

    tk.Label(form_frame, text='Mã lớp:').pack(anchor='w')
    entry_ma_lop = tk.Entry(form_frame)
    entry_ma_lop.pack(anchor='w')


    button_frame = tk.Frame(second_window)
    button_frame.pack(side=tk.RIGHT, padx=20, pady=10)

    tk.Button(button_frame, text='Thêm sinh viên', command=lambda: add_student(entry_ma_sv, entry_ho_ten, entry_ngay_sinh, entry_gioi_tinh, entry_dia_chi, entry_so_dien_thoai, entry_email, entry_ma_lop)).pack(fill=tk.X)
    tk.Button(button_frame, text='Cập nhật thông tin sinh viên', command=lambda: update_student(entry_ma_sv, entry_ho_ten, entry_ngay_sinh, entry_gioi_tinh, entry_dia_chi, entry_so_dien_thoai, entry_email, entry_ma_lop)).pack(fill=tk.X)
    tk.Button(button_frame, text='Xóa sinh viên', command=lambda: delete_student(entry_ma_sv)).pack(fill=tk.X)
def class_table():
    second_window = tk.Tk()
    second_window.title("Thông tin lớp")

    app_label = tk.Label(second_window, text="Hệ thống quản lý sinh viên", fg="#06a099", width=40)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack()
    form_frame = tk.Frame(second_window)
    form_frame.pack(side=tk.LEFT, padx=20, pady=10)
    tk.Label(form_frame, text='Mã lớp:').pack(anchor='w')
    entry_ma_lop = tk.Entry(form_frame)
    entry_ma_lop.pack(anchor='w')

    tk.Label(form_frame, text='Tên lớp:').pack(anchor='w')
    entry_ten_lop = tk.Entry(form_frame)
    entry_ten_lop.pack(anchor='w')

    tk.Label(form_frame, text='Niên khóa:').pack(anchor='w')
    entry_nien_khoa = tk.Entry(form_frame)
    entry_nien_khoa.pack(anchor='w')

    tk.Label(form_frame, text='Mã khoa:').pack(anchor='w')
    entry_ma_khoa = tk.Entry(form_frame)
    entry_ma_khoa.pack(anchor='w')

    button_frame = tk.Frame(second_window)
    button_frame.pack(side=tk.RIGHT, padx=20, pady=10)

    tk.Button(button_frame, text='Thêm lớp', command=lambda: add_class(entry_ma_lop, entry_ten_lop, entry_nien_khoa, entry_ma_khoa)).pack(fill=tk.X)
    tk.Button(button_frame, text='Cập nhật thông tin lớp', command=lambda: update_class(entry_ma_lop, entry_ten_lop, entry_nien_khoa, entry_ma_khoa)).pack(fill=tk.X)
    tk.Button(button_frame, text='Xóa lớp', command=lambda: delete_class(entry_ma_lop)).pack(fill=tk.X)

def department_table():
    second_window = tk.Tk()
    second_window.title("Thông tin Ngành")

    app_label = tk.Label(second_window, text="Hệ thống quản lý sinh viên", fg="#06a099", width=40)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack()
    form_frame = tk.Frame(second_window)
    form_frame.pack(side=tk.LEFT, padx=20, pady=10)

    tk.Label(form_frame, text='Mã khoa:').pack(anchor='w')
    entry_ma_khoa = tk.Entry(form_frame)
    entry_ma_khoa.pack(anchor='w')

    tk.Label(form_frame, text='Tên khoa:').pack(anchor='w')
    entry_ten_khoa = tk.Entry(form_frame)
    entry_ten_khoa.pack(anchor='w')

    button_frame = tk.Frame(second_window)
    button_frame.pack(side=tk.RIGHT, padx=20, pady=10)
    tk.Button(button_frame, text='Thêm khoa', command=lambda: add_department(entry_ma_khoa, entry_ten_khoa)).pack(fill=tk.X)
    tk.Button(button_frame, text='Cập nhật thông tin khoa', command=lambda: update_department(entry_ma_khoa, entry_ten_khoa)).pack(fill=tk.X)
    tk.Button(button_frame, text='Xóa khoa', command=lambda: delete_department(entry_ma_khoa)).pack(fill=tk.X)


def course_table():
    second_window = tk.Tk()
    second_window.title('Thông tin học phần')
    app_label = tk.Label(second_window, text="Hệ thống quản lý sinh viên", fg="#06a099", width=40)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack()
    form_frame = tk.Frame(second_window)
    form_frame.pack(side=tk.LEFT, padx=20, pady=10)

    tk.Label(form_frame, text='Mã học phần:').pack(anchor='w')
    entry_ma_hoc_phan = tk.Entry(form_frame)
    entry_ma_hoc_phan.pack(anchor='w')

    tk.Label(form_frame, text='Tên học phần:').pack(anchor='w')
    entry_ten_hoc_phan = tk.Entry(form_frame)
    entry_ten_hoc_phan.pack(anchor='w')

    tk.Label(form_frame, text='Số tín chỉ:').pack(anchor='w')
    entry_so_tin_chi = tk.Entry(form_frame)
    entry_so_tin_chi.pack(anchor='w')

    tk.Label(form_frame, text='Giảng viên:').pack(anchor='w')
    entry_giang_vien = tk.Entry(form_frame)
    entry_giang_vien.pack(anchor='w')

    tk.Label(form_frame, text='Thời gian:').pack(anchor='w')
    entry_thoi_gian = tk.Entry(form_frame)
    entry_thoi_gian.pack(anchor='w')

    tk.Label(form_frame, text='Phòng học:').pack(anchor='w')
    entry_phong_hoc = tk.Entry(form_frame)
    entry_phong_hoc.pack(anchor='w')

    button_frame = tk.Frame(second_window)
    button_frame.pack(side=tk.RIGHT, padx=20, pady=10)

    tk.Button(button_frame, text='Thêm học phần', command=lambda: add_course(entry_ma_hoc_phan, entry_ten_hoc_phan, entry_so_tin_chi, entry_giang_vien, entry_thoi_gian, entry_phong_hoc)).pack(fill=tk.X)
    tk.Button(button_frame, text='Cập nhật học phần', command=lambda: update_course(entry_ma_hoc_phan, entry_ten_hoc_phan, entry_so_tin_chi, entry_giang_vien, entry_thoi_gian, entry_phong_hoc)).pack(fill=tk.X)
    tk.Button(button_frame, text='Xóa học phần', command=lambda: delete_course(entry_ma_hoc_phan)).pack(fill=tk.X)

def grade_course_table():
    second_window = tk.Tk()
    second_window.title('Thông tin điểm học phần')
    app_label = tk.Label(second_window, text="Hệ thống quản lý sinh viên", fg="#06a099", width=40)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack()
    form_frame = tk.Frame(second_window)
    form_frame.pack(side=tk.LEFT, padx=20, pady=10)

    tk.Label(form_frame, text='Mã sinh viên:').pack(anchor='w')
    entry_ma_sv = tk.Entry(form_frame)
    entry_ma_sv.pack(anchor='w')

    tk.Label(form_frame, text='Mã học phần:').pack(anchor='w')
    entry_ma_hoc_phan = tk.Entry(form_frame)
    entry_ma_hoc_phan.pack(anchor='w')

    tk.Label(form_frame, text='Điểm học phần:').pack(anchor='w')
    entry_diem_hoc_phan = tk.Entry(form_frame)
    entry_diem_hoc_phan.pack(anchor='w')

    button_frame = tk.Frame(second_window)
    button_frame.pack(side=tk.RIGHT, padx=20, pady=10)

    tk.Button(button_frame, text='Thêm điểm học phần', command=lambda: add_grade_course(entry_ma_sv, entry_ma_hoc_phan, entry_diem_hoc_phan)).pack(fill=tk.X)
    tk.Button(button_frame, text='Cập nhật điểm học phần', command=lambda: update_grade_course(entry_ma_sv, entry_ma_hoc_phan, entry_diem_hoc_phan)).pack(fill=tk.X)
    tk.Button(button_frame, text='Xóa điểm học phần', command=lambda: delete_grade_course(entry_ma_sv, entry_ma_hoc_phan)).pack(fill=tk.X)

def extracurricular_activities_table():
    second_window = tk.Tk()
    second_window.title('Thông tin hoạt động ngoại khóa')
    app_label = tk.Label(second_window, text="Hệ thống quản lý sinh viên", fg="#06a099", width=40)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack()
    form_frame = tk.Frame(second_window)
    form_frame.pack(side=tk.LEFT, padx=20, pady=10)
    tk.Label(form_frame, text='Điểm học phần:').pack(anchor='w')
    entry_diem_hoc_phan = tk.Entry(form_frame)
    entry_diem_hoc_phan.pack(anchor='w')

    tk.Label(form_frame, text='Mã hoạt động:').pack(anchor='w')
    entry_ma_hoat_dong = tk.Entry(form_frame)
    entry_ma_hoat_dong.pack(anchor='w')

    tk.Label(form_frame, text='Tên hoạt động:').pack(anchor='w')
    entry_ten_hoat_dong = tk.Entry(form_frame)
    entry_ten_hoat_dong.pack(anchor='w')

    tk.Label(form_frame, text='Mô tả:').pack(anchor='w')
    entry_mo_ta = tk.Entry(form_frame)
    entry_mo_ta.pack(anchor='w')

    tk.Label(form_frame, text='Thời gian tổ chức:').pack(anchor='w')
    entry_thoi_gian_to_chuc = tk.Entry(form_frame)
    entry_thoi_gian_to_chuc.pack(anchor='w')

    tk.Label(form_frame, text='Địa điểm:').pack(anchor='w')
    entry_dia_diem = tk.Entry(form_frame)
    entry_dia_diem.pack(anchor='w')
    button_frame = tk.Frame(second_window)
    button_frame.pack(side=tk.RIGHT, padx=20, pady=10)
    tk.Button(button_frame, text='Thêm hoạt động', command=lambda: add_extracurricular_activitiess(entry_ma_hoat_dong, entry_ten_hoat_dong, entry_mo_ta, entry_thoi_gian_to_chuc, entry_dia_diem)).pack(fill=tk.X)
    tk.Button(button_frame, text='Cập nhật hoạt động', command=lambda: update_extracurricular_activitiess(entry_ma_hoat_dong, entry_ten_hoat_dong, entry_mo_ta, entry_thoi_gian_to_chuc, entry_dia_diem)).pack(fill=tk.X)
    tk.Button(button_frame, text='Xóa hoạt động', command=lambda: delete_extracurricular_activitiesss(entry_ma_hoat_dong)).pack(fill=tk.X)

def student_extracurricular_activities_table():
    second_window = tk.Tk()
    second_window.title('Thông tin hoạt động ngoại khóa')
    app_label = tk.Label(second_window, text="Hệ thống quản lý sinh viên", fg="#06a099", width=40)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack()
    form_frame = tk.Frame(second_window)
    form_frame.pack(side=tk.LEFT, padx=20, pady=10)
    tk.Label(form_frame, text='Mã sinh viên:').pack(anchor='w')
    entry_ma_sv = tk.Entry(form_frame)
    entry_ma_sv.pack(anchor='w')
    tk.Label(form_frame, text='Mã hoạt động:').pack(anchor='w')
    entry_ma_hoat_dong = tk.Entry(form_frame)
    entry_ma_hoat_dong.pack(anchor='w')

    button_frame = tk.Frame(second_window)
    button_frame.pack(side=tk.RIGHT, padx=20, pady=10)
    tk.Button(button_frame, text='Thêm sinh viên tham gia hoạt động', command=lambda: add_student_extracurricular_activitiesss(entry_ma_sv, entry_ma_hoat_dong)).pack(fill=tk.X)
    tk.Button(button_frame, text='Xóa sinh viên tham gia hoạt động', command=lambda: delete_student_extracurricular_activitiesss(entry_ma_sv, entry_ma_hoat_dong)).pack(fill=tk.X)


def create_main_window():
    root = tk.Tk()
    root.title('Quản lý sinh viên')
    app_label = tk.Label(root, text="Hệ thống quản lý sinh viên", fg="#06a099", width=30)
    app_label.config(font=("Sylfaen", 30))
    app_label.pack(pady=10)

    left_button_frame = tk.Frame(root)
    left_button_frame.pack(side=tk.LEFT, padx=20, pady=20)
    right_button_frame = tk.Frame(root)
    right_button_frame.pack(side=tk.RIGHT, padx=20, pady=10)

    tk.Button(left_button_frame, text='Chỉnh sửa thông tin sinh viên', command=lambda: student_table()).pack(fill=tk.X)
    tk.Button(left_button_frame, text='Chỉnh sửa thông tin lớp', command=lambda: class_table()).pack(fill=tk.X)
    tk.Button(left_button_frame, text='Chỉnh sửa thông tin khoa', command=lambda: department_table()).pack(fill=tk.X)
    tk.Button(left_button_frame, text='Chỉnh sửa thông tin học phần', command=lambda: course_table()).pack(fill=tk.X)
    tk.Button(left_button_frame, text='Chỉnh sửa điểm học phần', command=lambda: grade_course_table()).pack(fill=tk.X)
    tk.Button(left_button_frame, text='Chỉnh sửa thông tin hoạt động', command=lambda: extracurricular_activities_table()).pack(fill=tk.X)
    tk.Button(left_button_frame, text='Chỉnh sửa thông tin sinh viên tham gia hoạt động', command=lambda: student_extracurricular_activities_table()).pack(fill=tk.X)


    tk.Button(right_button_frame, text=' Thông tin sinh viên', command=lambda: display_student_data()).pack(fill=tk.X)
    tk.Button(right_button_frame, text=' Thông tin lớp', command=lambda: display_class_data()).pack(fill=tk.X)
    tk.Button(right_button_frame, text=' Thông tin khoa', command=lambda: display_department_data()).pack(fill=tk.X)
    tk.Button(right_button_frame, text=' Thông tin học phần', command=lambda: display_course_data()).pack(fill=tk.X)
    tk.Button(right_button_frame, text=' Thông tin điểm học phần', command=lambda: display_course_grade_data()).pack(fill=tk.X)
    tk.Button(right_button_frame, text=' Thông tin hoạt động ngoại khóa', command=lambda: display_extracurricular_activitiess_data()).pack(fill=tk.X)
    tk.Button(right_button_frame, text=' Thông tin sinh viên tham gia hoạt động', command=lambda: display_students_extracurricular_activitiess_data()).pack(fill=tk.X)
    root.mainloop()
create_main_window()