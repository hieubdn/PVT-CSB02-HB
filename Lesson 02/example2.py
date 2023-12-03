# chuyển đổi dola sang VND
dola = float(input("Nhap so tien: "))
VND = dola * 24385
print("$"+ str(dola) + "quy doi ra duoc" + str(VND)+ "đ" )
# Đoán số
import random
a = 0
b = random.randint(0,100)

while True:
    n = int(input("Nhập số dự đoán: "))
    a = a + 1
    if n < b:
        print("Thấp hơn")
    elif n > b:
        print("Lớn hơn")
    else: 
        print(f"Đúng! Số lần dự đoán là {a}")