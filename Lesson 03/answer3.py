print("Tính nghiệm của phương trình bậc 2")

print("***Cách 1***")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
# Tính delta
delta = b**2 - 4*a*c
# Kiểm tra giá trị của delta và tính nghiệm tương ứng
if delta > 0:
    x1 = (-b + (delta)**0.5) / (2*a)
    x2 = (-b - (delta)**0.5) / (2*a)
    print("Nghiệm phương trình là x1 =", x1, "và x2 =", x2)
elif delta == 0:
    x1 = -b / (2*a)
    print("Nghiệm phương trình là x1 = x2 =", x1)
else:
    print("Phương trình không có nghiệm thực.")

print()
print("***Cách 2***")
import math
# Nhập các hệ số của phương trình từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
def giai_phuong_trinh_bac_2(a, b, c):
    # Tính delta
    delta = b**2 - 4*a*c
    # Kiểm tra giá trị của delta
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return "Nghiệm phương trình là x1 = {:.2f} và x2 = {:.2f}".format(x1, x2)
    elif delta == 0:
        x1 = -b / (2*a)
        return "Nghiệm phương trình là x1 = x2 = {:.2f}".format(x1)
    else:
        return "Phương trình không có nghiệm thực."

# Gọi hàm giai_phuong_trinh_bac_2 và hiển thị kết quả
ket_qua = giai_phuong_trinh_bac_2(a, b, c)
print(ket_qua)
