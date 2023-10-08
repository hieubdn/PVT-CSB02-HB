# Viết chương trình tính tổng a và b
# với  a,b được nhập từ bàn phím
# a = int(input("Nhập a: "))
# b = int(input("Nhập b: "))
# print(a+b)

# Ví dụ về thư viện Turtle.
# from turtle import *
# right(90)
# forward(100)
# left(90)
# backward(100)
# mainloop()

# ***Ví dụ 1***
import turtle

# Tạo một đối tượng Turtle
t = turtle.Turtle()

# Đặt hình dạng của con rùa thành hình vuông
t.shape("square")

# Vẽ một hình vuông
for _ in range(4):
    t.forward(100)
    t.left(90)
# => shape(shape_name): Định nghĩa - Phương thức này thay đổi hình dạng của hình vẽ của con rùa thành hình dạng được chỉ định bởi shape_name.

# ***Ví dụ 2***
import turtle

# Tạo một đối tượng Turtle
t = turtle.Turtle()

# Di chuyển con rùa về phía trước 100 đơn vị
t.forward(100)

# Đóng cửa sổ đồ họa khi kết thúc
turtle.done()

# => forward(distance): Định nghĩa - Hàm này di chuyển con rùa về phía trước một khoảng cách xác định bởi distance.

# ***Ví dụ 3***
import turtle

# Tạo một đối tượng Turtle
t = turtle.Turtle()

# Xoay con rùa sang trái 90 độ
t.left(90)

# Đóng cửa sổ đồ họa khi kết thúc
turtle.done()
# =>left(angle): Định nghĩa - Hàm này xoay con rùa sang trái một góc xác định bởi angle (đơn vị là độ).

# ***ví dụ 4***
import turtle

# Tạo một đối tượng Turtle
t = turtle.Turtle()

# Xoay con rùa sang phải 45 độ
t.right(45)

# Đóng cửa sổ đồ họa khi kết thúc
turtle.done()
# => right(angle): Định nghĩa - Hàm này xoay con rùa sang phải một góc xác định bởi angle (đơn vị là độ).

#  ***Ví dụ 5***
import turtle

# Tạo một đối tượng Turtle
t = turtle.Turtle()

# Đặt màu của bút vẽ thành đỏ
t.pencolor("red")

# Vẽ một đường thẳng đỏ
t.forward(100)

# Đóng cửa sổ đồ họa khi kết thúc
turtle.done()
# => pencolor(color): Định nghĩa - Hàm này thay đổi màu của bút vẽ của con rùa thành màu được chỉ định bởi color.

# ***Ví dụ 6***
import turtle

# Tạo một đối tượng Turtle
t = turtle.Turtle()

# Đặt độ dày của bút vẽ thành 2
t.pensize(2)

# Vẽ một đường thẳng với bút có độ dày là 2
t.forward(100)

# Đóng cửa sổ đồ họa khi kết thúc
turtle.done()
# => pensize(width): Định nghĩa - Hàm này thay đổi kích thước của bút vẽ của con rùa thành độ dày được chỉ định bởi width.
