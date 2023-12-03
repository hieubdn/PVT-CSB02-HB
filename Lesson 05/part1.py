#  Bài 1: 
ten = input("Nhập họ & tên của bạn: ")
print(f"Họ & Tên: {ten}")
# Bài 2:
inp = input("Nhập một chuỗi: ")
inp_upper = inp.upper()
print("Chuỗi chữ hoa là: ", inp_upper)
# Bài 3:
so_nhap = float(input("Nhập một số: "))
binh_phuong = so_nhap ** 2
print(f"Bình phương của {so_nhap} là: {binh_phuong}")
# Bài 4:
import turtle
ban_kinh = float(input("Nhập bán kính của hình tròn: "))
pen = turtle.Turtle() # Tạo một đối tượng Turtle
pen.circle(ban_kinh) # Vẽ hình tròn
turtle.done() # Hiển thị cửa sổ Turtle cho đến khi người dùng đóng nó