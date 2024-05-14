import streamlit as st
import pyodbc

# Kết nối đến cơ sở dữ liệu
server = 'DESKTOP-HRTE7HR\\SQLEXPRESS'
database = 'QUANLYSINHVIEN'
username = ''
password = ''
conn = pyodbc.connect(f'DRIVER={{SQL SERVER}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# Hàm thực hiện truy vấn và trả về kết quả
def execute_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

# Thực hiện truy vấn SQL và hiển thị kết quả trên Streamlit
def main():
    st.title('Ứng dụng quản lý sinh viên')

    # Hiển thị dữ liệu từ bảng SinhVien
    st.subheader('Danh sách sinh viên')
    rows = execute_query('SELECT * FROM SinhVien')
    st.write(rows)

    # Hiển thị biểu mẫu để thêm sinh viên mới
    st.subheader('Thêm sinh viên mới')
    ma_sv = st.text_input('Mã sinh viên')
    ho_ten = st.text_input('Họ tên')
    ngay_sinh = st.date_input('Ngày sinh')
    # Thêm các trường thông tin khác tại đây

    if st.button('Thêm sinh viên'):
        # Thực hiện thêm sinh viên vào cơ sở dữ liệu
        query = f"INSERT INTO SinhVien (MaSV, HoTen, NgaySinh) VALUES ('{ma_sv}', '{ho_ten}', '{ngay_sinh}')"
        execute_query(query)
        st.success('Thêm sinh viên thành công!')

if __name__ == '__main__':
    main()
