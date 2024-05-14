
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


root = tk.Tk()
root.title('Quản lý Sinh viên')

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

tk.Label(root, text='Tên lớp').grid(row=8, column=0)
entry_ten_lop = tk.Entry(root)
entry_ten_lop.grid(row=8, column=1)

tk.Label(root, text='Niên khóa').grid(row=9, column=0)
entry_nien_khoa = tk.Entry(root)
entry_nien_khoa.grid(row=9, column=1)

tk.Label(root, text='Mã khoa').grid(row=10, column=0)
entry_ma_khoa = tk.Entry(root)
entry_ma_khoa.grid(row=10, column=1)

tk.Label(root, text = 'Tên Khoa').grid(row = 11, column = 0)
entry_ten_khoa = tk.Entry(root)
entry_ten_khoa.grid(row = 11, column=1)

tk.Label(root, text='Mã học phần:').grid(row=12, column=0)
entry_ma_hoc_phan = tk.Entry(root)
entry_ma_hoc_phan.grid(row=12, column=1)

tk.Label(root, text='Tên học phần').grid(row=13, column=0)
entry_ten_hoc_phan = tk.Entry(root)
entry_ten_hoc_phan.grid(row=13, column=1)

tk.Label(root, text='Số tín chỉ :').grid(row=14, column=0)
entry_so_tin_chi = tk.Entry(root)
entry_so_tin_chi.grid(row=14, column=1)

tk.Label(root, text='Giảng viên').grid(row=15, column=0)
entry_giang_vien = tk.Entry(root)
entry_giang_vien.grid(row=15, column=1)

tk.Label(root, text='Thời gian').grid(row=16, column=0)
entry_thoi_gian = tk.Entry(root)
entry_thoi_gian.grid(row=16, column=1)

tk.Label(root, text='Phòng học').grid(row=17, column=0)
entry_phong_hoc = tk.Entry(root)
entry_phong_hoc.grid(row=17, column=1)

tk.Label(root, text='Điểm học phần ').grid(row=18, column=0)
entry_diem_hoc_phan = tk.Entry(root)
entry_diem_hoc_phan.grid(row=18, column=1)

tk.Label(root, text = 'Mã hoạt động').grid(row = 19, column = 0)
entry_ma_hoat_dong = tk.Entry(root)
entry_ma_hoat_dong.grid(row = 19, column=1)

tk.Label(root, text='Tên hoạt động').grid(row=20, column=0)
entry_ten_hoat_dong = tk.Entry(root)
entry_ten_hoat_dong.grid(row=20, column=1)

tk.Label(root, text='Mô tả ').grid(row=21, column=0)
entry_mo_ta = tk.Entry(root)
entry_mo_ta.grid(row=21, column=1)

tk.Label(root, text='Thời gian tổ chức').grid(row=22, column=0)
entry_thoi_gian_to_chuc = tk.Entry(root)
entry_thoi_gian_to_chuc.grid(row=22, column=1)

tk.Label(root, text = 'Địa điểm').grid(row = 23, column = 0)
entry_dia_diem= tk.Entry(root)
entry_dia_diem.grid(row = 23, column=1)




tk.Button(root, text='Bảng thông tin sinh viên', command= lambda: display_student_data()).grid(row=0, column=2)
tk.Button(root, text='Bảng thông tin lớp', command= lambda: display_class_data()).grid(row=1, column=2)
tk.Button(root, text='Bảng thông tin khoa', command= lambda: display_department_data()).grid(row=2, column=2)
tk.Button(root, text='Bảng thông tin học phần', command= lambda: display_course_data()).grid(row=3, column=2)
tk.Button(root, text='Bảng thông tin điểm học phần', command= lambda: display_course_grade_data()).grid(row=4, column=2)
tk.Button(root, text='Bảng thông tin hoạt động ngoại khóa', command= lambda: display_extracurricular_activitiess_data()).grid(row=5, column=2)


tk.Button(root, text='Thêm sinh viên', command=lambda: add_student(entry_ma_sv, entry_ho_ten, entry_ngay_sinh, entry_gioi_tinh, entry_dia_chi, entry_so_dien_thoai, entry_email, entry_ma_lop)).grid(row=6, column=2)
tk.Button(root, text='Cập nhật thông tin sinh viên', command=lambda: update_student(entry_ma_sv, entry_ho_ten, entry_ngay_sinh, entry_gioi_tinh, entry_dia_chi, entry_so_dien_thoai, entry_email, entry_ma_lop)).grid(row=7, column=2)
tk.Button(root, text='Xóa sinh viên', command=lambda: delete_student(entry_ma_sv)).grid(row=8, column=2)


tk.Button(root, text='Thêm lớp', command=lambda: add_class(entry_ma_lop, entry_ten_lop, entry_nien_khoa, entry_ma_khoa)).grid(row=9, column=2)
tk.Button(root, text='Cập nhật thông tin lớp', command=lambda: update_class(entry_ma_lop, entry_ten_lop, entry_nien_khoa, entry_ma_khoa)).grid(row=10, column=2)
tk.Button(root, text='Xóa lớp', command=lambda: delete_class(entry_ma_lop)).grid(row=11, column=2)


tk.Button(root, text='Thêm khoa', command=lambda: add_department(entry_ma_khoa, entry_ten_khoa)).grid(row=12, column=2)
tk.Button(root, text='Cập nhật thông tin khoa', command=lambda: update_department(entry_ma_khoa, entry_ten_khoa)).grid(row=13, column=2)
tk.Button(root, text='Xóa khoa', command=lambda: delete_department(entry_ma_khoa)).grid(row=14, column=2)


tk.Button(root, text='Thêm Học phần ', command=lambda: add_course(entry_ma_hoc_phan,entry_ten_hoc_phan, entry_so_tin_chi, entry_giang_vien, entry_thoi_gian,entry_phong_hoc )).grid(row=15, column=2)
tk.Button(root, text='Cập nhật Học phần', command=lambda: update_course(entry_ma_hoc_phan,entry_ten_hoc_phan, entry_so_tin_chi, entry_giang_vien, entry_thoi_gian,entry_phong_hoc  )).grid(row=16, column=2)
tk.Button(root, text='Xóa Học phần', command=lambda: delete_course(entry_ma_hoc_phan)).grid(row=17, column=2)


tk.Button(root, text='Thêm điểm học phần', command=lambda: add_grade_course(entry_ma_sv, entry_ma_hoc_phan, entry_diem_hoc_phan)).grid(row=18, column=2)
tk.Button(root, text='Cập nhật điểm học phần', command=lambda: update_grade_course(entry_ma_sv, entry_ma_hoc_phan, entry_diem_hoc_phan)).grid(row=19, column=2)
tk.Button(root, text='Xóa điểm học phần', command=lambda: delete_grade_course(entry_ma_sv, entry_ma_hoc_phan)).grid(row=20, column=2)


tk.Button(root, text='Thêm hoạt động', command=lambda:add_extracurricular_activitiess(entry_ma_hoat_dong, entry_ten_hoat_dong, entry_mo_ta, entry_thoi_gian_to_chuc, entry_dia_diem)).grid(row=21, column=2)
tk.Button(root, text='Cập nhật hoạt động', command=lambda:update_extracurricular_activitiess(entry_ma_hoat_dong, entry_ten_hoat_dong, entry_mo_ta, entry_thoi_gian_to_chuc, entry_dia_diem)).grid(row=22, column=2)
tk.Button(root, text='Xóa hoạt động', command=lambda: delete_extracurricular_activitiesss(entry_ma_hoat_dong)).grid(row=23, column=2)


tk.Button(root, text='Thêm sinh viên tham gia hoạt động', command=lambda: add_student_extracurricular_activitiesss(entry_ma_sv, entry_ma_hoat_dong)).grid(row=24, column=0)
tk.Button(root, text='Xóa sinh viên tham gia hoạt động', command=lambda: delete_student_extracurricular_activitiesss(entry_ma_sv, entry_ma_hoat_dong)).grid(row=24, column=2)


root.mainloop()

