# Viết chương trình tính điểm số của HS
diem = float(input("Nhập số điểm: "))
if diem >= 8:
    print(" Học sinh Giỏi")
elif diem >= 6.5:
    print("Học sinh khá")
elif diem >= 5:
    print("Học sinh trung bình")
else:
    print ("Học sinh yếu")

a = input("so a")
b = input("so b")
print(a+b)
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
# Viết bảng cửu chương
print("Bảng cửu chương")
for i in range(2,10):
    for j in range(1,11):
        result = i * j
        print(i, "*", j, "=", result)
# Tính tổng số chẳn từ 0 đến n
n = int(input("nhap n: "))
sum = 0
for i in range(0, n+1):
    if i % 2 == 0:
        sum = sum + i
        i = i+1
print(sum)

# heloo