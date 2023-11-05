# # 1/ Viết chương trình tìm số lớn hơn trong 3 số nhập từ người dùng nhập.
# # 2/ Viết chương trình tính chỉ số BMI, in ra tình trạng sức khoẻ của người dùng
# # 3/ Viết chương trình tính nghiệm của phương trình bậc 2
# # 4/ Viết chương trình check số người dùng nhập vào là số dương, số âm hay số 0
# # 5/ Viết chương trình xác định một năm có phải năm nhuận không
# # Năm nhuận: là năm chia hết cho 4. Trong trường hợp năm chia hết cho 100 thì phải chia hết cho 400.
# # *******************************************************************************************************
# # Câu 1
# lst = []
# c = int(input("Nhap so c"))
# d = int(input("Nhap so d"))
# e = int(input("Nhap so e"))
# lst.append(c)
# lst.append(d)
# lst.append(e)
# t = lst[0]
# for i in range(len(lst)):
#     # lst= [-5, 10, 9, -3, 4]
#     if lst[i] > t:
#          t = lst[i]
# print(t)
# # Câu 2
# print("Tính chỉ số BMI")
# w = float(input("Nhập số cân nặng (Tính kilogam): "))
# h = float(input("Nhập số chiều cao (Tính theo mét): "))
# BMI = w/(h*h)
# if BMI <= 18.5:
#     print(f"Bạn đang gặp phải tình trạng thiếu cân với chỉ số BMI là: {BMI}")
# elif BMI <= 24.9:
#     print(f"Bạn đang sở hữu cân nặng khỏe mạnh với chỉ số BMI là: {BMI}")
# elif BMI <= 29.9:
#     print(f"Bạn đang trong tình trạng thừa cân với chỉ số BMI là: {BMI}")
# else:
#     print(f"chỉ số BMI là: {BMI}, Bạn đang bị béo phì và tình trạng này có thể khiến bạn gặp rất nhiều vấn đề về sức khỏe cũng như trong sinh hoạt")
# print()
# # Câu 3:
# print("Tính nghiệm của phương trình bậc 2")

# print("***Cách 1***")
# a = float(input("Nhập hệ số a: "))
# b = float(input("Nhập hệ số b: "))
# c = float(input("Nhập hệ số c: "))
# # Tính delta
# delta = b**2 - 4*a*c
# # Kiểm tra giá trị của delta và tính nghiệm tương ứng
# if delta > 0:
#     x1 = (-b + (delta)**0.5) / (2*a)
#     x2 = (-b - (delta)**0.5) / (2*a)
#     print("Nghiệm phương trình là x1 =", x1, "và x2 =", x2)
# elif delta == 0:
#     x1 = -b / (2*a)
#     print("Nghiệm phương trình là x1 = x2 =", x1)
# else:
#     print("Phương trình không có nghiệm thực.")

# print()
# print("***Cách 2***")
# import math
# # Nhập các hệ số của phương trình từ người dùng
# a = float(input("Nhập hệ số a: "))
# b = float(input("Nhập hệ số b: "))
# c = float(input("Nhập hệ số c: "))
# def giai_phuong_trinh_bac_2(a, b, c):
#     # Tính delta
#     delta = b**2 - 4*a*c
#     # Kiểm tra giá trị của delta
#     if delta > 0:
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b - math.sqrt(delta)) / (2*a)
#         return "Nghiệm phương trình là x1 = {:.2f} và x2 = {:.2f}".format(x1, x2)
#     elif delta == 0:
#         x1 = -b / (2*a)
#         return "Nghiệm phương trình là x1 = x2 = {:.2f}".format(x1)
#     else:
#         return "Phương trình không có nghiệm thực."

# # Gọi hàm giai_phuong_trinh_bac_2 và hiển thị kết quả
# ket_qua = giai_phuong_trinh_bac_2(a, b, c)
# print(ket_qua)

# # Câu 5:
# nam = int(input("nhap năm: "))
# if nam % 4 == 0 and nam % 100 != 0:
#         print("nam nhuan")
# if nam % 100 == 0 and nam % 400 == 0:
#         print("nam nhuan")
# else:
#         print("khong phai nam nhuan")
nam = int(input("nam nhuan :   "))

if nam % 4 ==0 :
    if nam % 100 == 0 and nam % 400 == 0 :
        print("nam nhuan")
    elif nam % 100 == 0 and nam % 400 != 0 :
        print("ko phai nam nhuan")
    else :
        print("nam nhuan")
else:
    print("khong phai nam nhuan")