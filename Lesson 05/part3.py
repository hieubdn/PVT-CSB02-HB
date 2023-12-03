# Bài 1:
so_nhap = float(input("Nhập một số: "))
if so_nhap > 13:
    print(f"{so_nhap} lớn hơn 13.")
else:
    print(f"{so_nhap} không lớn hơn 13.")
# Bài 2:
so_nhap = int(input("Nhập một số: "))
if so_nhap % 2 == 0:
    print(f"{so_nhap} là số chẵn.")
else:
    print(f"{so_nhap} không phải là số chẵn.")
# Bài 3:
thang = int(input("Nhập một tháng (từ 1 đến 12): "))
if thang == 2:
    nam = int(input("Nhập một năm: "))  # Yêu cầu nhập năm để xác định năm nhuận
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("Tháng 2 có 29 ngày.")
    else:
        print("Tháng 2 có 28 ngày.")
elif thang in [4, 6, 9, 11]:
    print(f"Tháng {thang} có 30 ngày.")
elif thang in [1, 3, 5, 7, 8, 10, 12]:
    # Các tháng còn lại có 31 ngày
    print(f"Tháng {thang} có 31 ngày.")
else:
    print("Tháng không hợp lệ. Nhập tháng từ 1 đến 12.")