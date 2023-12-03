print("Tính chỉ số BMI")
w = float(input("Nhập số cân nặng (Tính kilogam): "))
h = float(input("Nhập số chiều cao (Tính theo mét): "))
BMI = w/(h*h)
if BMI <= 18.5:
    print(f"Bạn đang gặp phải tình trạng thiếu cân với chỉ số BMI là: {BMI}")
elif BMI <= 24.9:
    print(f"Bạn đang sở hữu cân nặng khỏe mạnh với chỉ số BMI là: {BMI}")
elif BMI <= 29.9:
    print(f"Bạn đang trong tình trạng thừa cân với chỉ số BMI là: {BMI}")
else:
    print(f"chỉ số BMI là: {BMI}, Bạn đang bị béo phì và tình trạng này có thể khiến bạn gặp rất nhiều vấn đề về sức khỏe cũng như trong sinh hoạt")
print()