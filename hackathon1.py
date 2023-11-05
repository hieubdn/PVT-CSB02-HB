# # ***Phần 1***
# #  Bài 1: 
# ten = input("Nhập họ & tên của bạn: ")
# print(f"Họ & Tên: {ten}")
# # Bài 2:
# inp = input("Nhập một chuỗi: ")
# inp_upper = inp.upper()
# print("Chuỗi chữ hoa là: ", inp_upper)
# # Bài 3:
# so_nhap = float(input("Nhập một số: "))
# binh_phuong = so_nhap ** 2
# print(f"Bình phương của {so_nhap} là: {binh_phuong}")
# # Bài 4:
# import turtle
# ban_kinh = float(input("Nhập bán kính của hình tròn: "))
# pen = turtle.Turtle() # Tạo một đối tượng Turtle
# pen.circle(ban_kinh) # Vẽ hình tròn
# turtle.done() # Hiển thị cửa sổ Turtle cho đến khi người dùng đóng nó

# # ***Phần 2***
# # Bài 1:
# for i in range(3, 13):
#     print(i)
# # Bài 2:
# n = int(input("Nhập một số n (n > 0): "))
# if n > 0:
#     for i in range(n + 1):
#         print(i)
# else:
#     print("Lỗi! Số n phải lớn hơn 0.")
# # Bài 3:
# n = int(input("Nhập một số n (n > 0): "))
# if n > 0:
#     i = 1
#     while i <= n:
#         print(i)
#         i += 2
# else:
#     print("Lỗi! Số n phải lớn hơn 0.")
# # Bài 4:
# import turtle
# so_canh = int(input("Nhập số cạnh của đa giác bạn muốn: "))
# pen = turtle.Turtle() # Tạo một đối tượng Turtle
# goc = 360 / so_canh  # Tính góc của mỗi cạnh dựa trên số cạnh
# # Vẽ đa giác
# for i in range(so_canh):
#     pen.forward(100)  # Độ dài cạnh, có thể điều chỉnh
#     pen.left(goc)
# turtle.done() # Hiển thị cửa sổ Turtle cho đến khi người dùng đóng nó


# # Phần 3:
# # Bài 1:
# so_nhap = float(input("Nhập một số: "))
# if so_nhap > 13:
#     print(f"{so_nhap} lớn hơn 13.")
# else:
#     print(f"{so_nhap} không lớn hơn 13.")
# # Bài 2:
# so_nhap = int(input("Nhập một số: "))
# if so_nhap % 2 == 0:
#     print(f"{so_nhap} là số chẵn.")
# else:
#     print(f"{so_nhap} không phải là số chẵn.")
# # Bài 3:
# thang = int(input("Nhập một tháng (từ 1 đến 12): "))
# if thang == 2:
#     nam = int(input("Nhập một năm: "))  # Yêu cầu nhập năm để xác định năm nhuận
#     if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
#         print("Tháng 2 có 29 ngày.")
#     else:
#         print("Tháng 2 có 28 ngày.")
# elif thang in [4, 6, 9, 11]:
#     print(f"Tháng {thang} có 30 ngày.")
# elif thang in [1, 3, 5, 7, 8, 10, 12]:
#     # Các tháng còn lại có 31 ngày
#     print(f"Tháng {thang} có 31 ngày.")
# else:
#     print("Tháng không hợp lệ. Nhập tháng từ 1 đến 12.")
# # Phần 4:
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



