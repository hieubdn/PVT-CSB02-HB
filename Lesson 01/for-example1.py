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
