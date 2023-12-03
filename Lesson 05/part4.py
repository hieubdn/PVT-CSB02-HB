danh_sach_tai_khoan = {}
while True:
    print("== Registration ==")
    ten_dang_nhap = input("Username: ")
    
    # Kiểm tra mật khẩu
    mat_khau = input("Password: ")
    while len(mat_khau) < 8 or not any(char.isdigit() for char in mat_khau):
        print("Mật khẩu không đủ mạnh. Yêu cầu ít nhất 8 ký tự và phải chứa ít nhất 1 chữ số.")
        mat_khau = input("Re-enter Password: ")
    # Kiểm tra xem mật khẩu và nhập lại mật khẩu có giống nhau
    nhap_lai_mat_khau = input("Re-enter Password: ")
    if mat_khau != nhap_lai_mat_khau:
        print("Mật khẩu không khớp. Vui lòng nhập lại.")
        continue
    # Kiểm tra email
    email = input("Email: ")
    while '@' not in email or '.' not in email:
        print("Email không hợp lệ. Vui lòng nhập lại.")
        email = input("Re-enter Email: ")
    tiep_tuc = input("Tiếp tục đăng ký (yes/no)? ")
    
    if tiep_tuc.lower() == 'yes':
        danh_sach_tai_khoan[ten_dang_nhap] = {'mat_khau': mat_khau, 'email': email}
        print("Registered successfully.")
    elif tiep_tuc.lower() == 'no':
        break