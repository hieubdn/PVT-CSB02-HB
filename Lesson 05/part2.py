# Bài 1:
for i in range(3, 13):
    print(i)
# Bài 2:
n = int(input("Nhập một số n (n > 0): "))
if n > 0:
    for i in range(n + 1):
        print(i)
else:
    print("Lỗi! Số n phải lớn hơn 0.")
# Bài 3:
n = int(input("Nhập một số n (n > 0): "))
if n > 0:
    i = 1
    while i <= n:
        print(i)
        i += 2
else:
    print("Lỗi! Số n phải lớn hơn 0.")
# Bài 4:
import turtle
so_canh = int(input("Nhập số cạnh của đa giác bạn muốn: "))
pen = turtle.Turtle() # Tạo một đối tượng Turtle
goc = 360 / so_canh  # Tính góc của mỗi cạnh dựa trên số cạnh
# Vẽ đa giác
for i in range(so_canh):
    pen.forward(100)  # Độ dài cạnh, có thể điều chỉnh
    pen.left(goc)
turtle.done() # Hiển thị cửa sổ Turtle cho đến khi người dùng đóng nó
